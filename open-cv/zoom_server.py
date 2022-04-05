# create a server for video conferencing using sockets
# video is captured by opencv from different clients

import socket
import threading
import cv2
import time
import os
import sys



class ZoomServer:
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(5)
        self.clients = []
        self.threads = []
        self.running = True
        self.video_path = cv2.VideoCapture(0)
        
    def run(self):
        while self.running:
            print('Server started at port:', self.port)
            try:
                client, addr = self.sock.accept()
                self.clients.append(client)
                print('Client connected: ', addr)
                thread = threading.Thread(target=self.handle_client, args=(client, addr))
                self.threads.append(thread)
                thread.start()
            except KeyboardInterrupt:
                self.running = False
                self.sock.close()
                for client in self.clients:
                    client.close()
                for thread in self.threads:
                    thread.join()
                print('Server stopped')
                sys.exit()

    def handle_client(self, client, addr):
        while self.running:
            try:
                data = client.recv(1024)
                if data:
                    print('Received data:', data)
                    if data == b'STOP':
                        self.running = False
                        client.close()
                        self.clients.remove(client)
                        print('Client disconnected: ', addr)
                        break
                    elif data == b'START':
                        print('Start sending video')
                        self.send_video(client)
                    else:
                        print('Unknown command')
            except KeyboardInterrupt:
                self.running = False
                client.close()
                self.clients.remove(client)
                print('Client disconnected: ', addr)
                break

    def send_video(self, client):
        while self.running:
            # forward incoming video from client
            ret, frame = self.video_path
            if ret:
                client.send(frame)
                time.sleep(0.05)
            else:
                print('Video ended')
                break


if __name__ == '__main__':
    server = ZoomServer(8000)
    server.run()

        

        

        