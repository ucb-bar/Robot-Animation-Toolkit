import socket
import struct
import time

import numpy as np


class UnrealTCPAdapter:
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
        
        print("connected by", addr)
        
        last_t = 0
        start_t = time.time()
        
        times = []
        positions = []
        
        while True:
            try:
                conn.settimeout(1)
                buffer = conn.recv(1024)
            except TimeoutError:
                conn.close()
                break
            
            
            
            # print(len(buffer))
            header = buffer[:12]
            data = buffer[12:]
            timestamp, n_transforms = struct.unpack(">QL", header)
            
            for i in range(n_transforms):
                transform = data[i*28:(i+1)*28]
                x, y, z, rx, ry, rz, rw = struct.unpack(">fffffff", transform)
        
            
            print(timestamp, x, y, z)
            if time.time() - start_t < 2:
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
        

if __name__ == "__main__":
    adapter = UnrealTCPAdapter("0.0.0.0", 8000)
    adapter.run()
    adapter.close()
