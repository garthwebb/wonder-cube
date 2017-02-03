from wonder.utils.switch_monitor import SwitchMonitor

AUDIO_SWITCH_GPIO = 27
AUDIO_SERVICE = 'audio-player'
VOLUME_SERVICE = 'volume-control'

monitor = SwitchMonitor(AUDIO_SWITCH_GPIO)
monitor.manage_service(AUDIO_SERVICE)
monitor.manage_service(VOLUME_SERVICE)

monitor.run()
