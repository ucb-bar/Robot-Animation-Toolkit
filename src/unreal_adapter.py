import socket
import struct
import time

import numpy as np

class UnrealTCPServer:
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.addr, self.port))
        
        self.sock.listen(4)
        self.sock.settimeout(0.1)
        
        
    def run(self):
        print("server started.")
        connected = False
        while not connected:
            try:
                conn, addr = self.sock.accept()
                connected = True
            except:
                pass
            
        # conn.recv(len(b"\r\n\r\n\x00\x00\x00\x00\x00\x00\x00\x00"))
        
        print("connected by", addr)
        
        last_t = 0
        start_t = time.time()
        
        times = []
        positions = []
        
        while True:
            try:
                conn.settimeout(1)
                buffer = conn.recv(20)
            except TimeoutError:
                conn.close()
                break
            
            
            
            # print(len(buffer))
            
            timestamp, x, y, z = struct.unpack(">Qfff", buffer)
            
            
            if time.time() - start_t < 2:
                print("passing")
                continue
            
            times.append(timestamp)
            positions.append([x, y, z])
        
        times = np.array(times)
        positions = np.array(positions)
        
        print("saving...")
        
        # store to npy file
        data = np.hstack([times[:, None], positions])
        np.save("data.npy", data)
         

    def send(self, data):
        self.sock.sendall(data)
    
    def recv(self):
        return self.sock.recv(1024)
    
    def close(self):
        self.sock.close()
        


server = UnrealTCPServer("0.0.0.0", 8000)

server.run()

server.close()
