#!/usr/bin/python

from wonder.utils.switch_monitor import SwitchMonitor
import sys


def print_usage():
    print("\nUsage:\n")
    print("\tswitch-monitor pin service")


def load_arguments():
    cli_pin, cli_service = sys.argv[1:3]
    cli_pin = int(cli_pin)

    if not cli_pin:
        print("Missing pin")
        print_usage()
        exit(1)

    if not cli_service:
        print("Missing service name")
        print_usage()
        exit(1)

    return cli_pin, cli_service


if len(sys.argv) != 3:
    print_usage()
    exit(1)

pin, service = load_arguments()

print("Monitoring pin {:d} for service {:s}".format(pin, service))

monitor = SwitchMonitor(pin)
monitor.manage_service(service)

monitor.run()
