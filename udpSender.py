import socket
import struct
import time
import numpy as np
import zlib

UDP_IP = "127.0.0.1"
UDP_PORT = 25042

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

g = 180 # starting angle
while True:
    R = np.array([[np.cos(np.deg2rad(g)), -np.sin(np.deg2rad(g)), 0],
                  [np.sin(np.deg2rad(g)), np.cos(np.deg2rad(g)), 0],
                  [0, 0, 1]],np.double)
    data = R.flatten().tolist()
    crc = zlib.crc32(R.tobytes())
    #crc = 0#~crc & 0xffffffff
    data.append(crc)
    message = struct.pack('@9dI', *data)
    sock.sendto(message, (UDP_IP, UDP_PORT))
    print(f'sent message: {data}')
    time.sleep(0.1)
    g += 1
    if g > 180:
        g = -180


