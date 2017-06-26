"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""

import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.1.243",
                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
                        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    for x in range(11, 1, -1):
        a = [x / 10, x / 10, x / 10]
        print(a)
        client.send_message("/filter", a)
        time.sleep(0.15)
    for x in range(1, 11, 1):
        a = [x / 10, x / 10, x / 10]
        print(a)
        client.send_message("/filter", a)
        time.sleep(0.15)