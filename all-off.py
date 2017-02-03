from wonder.utils.opc import Client

clear = [(0, 0, 0) for p in range(9*4*6*2)]
client = Client("localhost:7890")
client.put_pixels(clear, channel=0)
