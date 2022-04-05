# zoom client

import socket
import threading
import time
import os
import sys
import cv2


class ZoomClient:
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('localhost', port))
        self.running = True
        self.video_path = cv2.VideoCapture(0)

    def run(self):
        while self.running:
            print('Client started at port:', self.port)
            try:
                data = self.sock.recv(1024)
                if data:
                    print('Received data:', data)
                    if data == b'STOP':
                        self.running = False
                        self.sock.close()
                        print('Client stopped')
                        sys.exit()
                    elif data == b'START':
                        print('Start receiving video')
                        self.receive_video()
                    else:
                        print('Unknown command')
            except KeyboardInterrupt:
                self.running = False
                self.sock.close()
                print('Client stopped')
                sys.exit()

    def receive_video(self):
        while self.running:
            ret, frame = self.video_path
            if ret:
                self.sock.send(frame)
                time.sleep(0.1)
            else:
                print('Video ended')
                self.running = False


if __name__ == '__main__':
    port = int(sys.argv[1])
    client = ZoomClient(port)
    client.run()
