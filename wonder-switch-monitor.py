from wonder.utils.switch_monitor import SwitchMonitor

WONDER_SWITCH_GPIO = 13

FADECANDY_SERVICE = 'fcserver'
WONDER_SERIVCE = 'wonder-show'

monitor = SwitchMonitor(WONDER_SWITCH_GPIO)
monitor.manage_service(WONDER_SERIVCE, start_order=2, stop_order=1)
monitor.manage_service(FADECANDY_SERVICE, start_order=1, stop_order=2)

monitor.run()
