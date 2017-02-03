import RPi.GPIO as GPIO
import time

from subprocess import call

PIN_MODE = GPIO.BCM
DEBOUNCE_DELAY = 0.05


class SwitchMonitor:
    gpio = None
    services = []
    services_start = []
    services_stop = []

    def __init__(self, monitor_gpio):
        self.gpio = monitor_gpio

        GPIO.setmode(PIN_MODE)
        GPIO.setup(self.gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def manage_service(self, service_name, start_order=-1, stop_order=-1):
        self.services.append((service_name, start_order, stop_order))

    def set_service_order(self):
        self.set_start_order()
        self.set_stop_order()

    def set_start_order(self):
        for group in sorted(self.services, key=lambda order: order[1]):
            service_name = group[0]
            self.services_start.append(service_name)

    def set_stop_order(self):
        for group in sorted(self.services, key=lambda order: order[2]):
            service_name = group[0]
            self.services_stop.append(service_name)

    def verify_started(self):
        for service in self.services_start:
            print("Starting {:s} if not already started".format(service))
            call(["systemctl", "start", service])

    def verify_stopped(self):
        for service in self.services_stop:
            print("Stopping {:s} if not already stopped".format(service))
            call(["systemctl", "stop", service])

    def read_gpio(self):
        value = GPIO.input(self.gpio)
        print("Read value: {:d}".format(value))
        return value

    def wait_for_change(self, edge):
        try:
            print("Edge {:d}".format(edge))
            GPIO.wait_for_edge(self.gpio, edge)
        except KeyboardInterrupt:
            GPIO.cleanup()

    def run(self):
        self.set_service_order()

        while True:
            value = self.read_gpio()

            if value:
                self.verify_stopped()
                edge = GPIO.FALLING
            else:
                self.verify_started()
                edge = GPIO.RISING

            self.wait_for_change(edge)

            # Sleep momentarily to debounce
            time.sleep(DEBOUNCE_DELAY)
