from wonder.controls.fader import Fader

from Adafruit_MAX9744 import MAX9744

import time

min_volume = 20
max_volume = 63
cur_volume = None


def verify_volume():
    values = {}

    # Check the volume multiple times and return the one found most often
    for n in range(10):
        v = int(volume_control.read_value())
        if v in values:
            values[v] += 1
        else:
            values[v] = 0

    # Sort by the count of values found
    ordered_values = sorted(values, key=lambda key: values[key], reverse=True)
    return ordered_values[0]


amp = MAX9744()
volume_control = Fader(Fader.VOLUME_CHANNEL, min=min_volume, max=max_volume)

while True:
    value = int(volume_control.read_value())

    if cur_volume != value:
        # Sometimes the fader/adc freaks out and reports a super high value.  Use this
        # verify function to check the volume multiple times and use the mode of the values
        value = verify_volume()
        amp.set_volume(value)
        print("Volume : {}".format(value))
        cur_volume = value

    time.sleep(0.2)
