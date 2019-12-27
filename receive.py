#!/usr/bin/env python
import socket
import numpy as np
import cv2 as cv
import pyaudio
import sys
import threading
from time import sleep
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "server_output.wav"
WIDTH = 2


p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)


#bind
addr = ("127.0.0.1", 8080)
buf = 8192
width = 640
height = 480
code = b'start'
num_of_chunks = width * height * 3 / buf

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)
    print ('Connected by', addr)
    while True:
        chunks = []
        start = False
        while len(chunks) < num_of_chunks:
            chunk, _ = s.recvfrom(buf)
            if start:
                chunks.append(chunk)
            elif chunk.startswith(code):
                start = True

        byte_frame = b''.join(chunks)

        frame = np.frombuffer(
            byte_frame, dtype=np.uint8).reshape(height, width, 3)
        
        #i=0
        #while i<1500:
           # print(frame)
            #print(len(frame))
            #print(i)
            #i+=1
        
        cv.imshow('recv', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
        #while True:
           # soundData, addr = s.recvfrom(CHUNK * CHANNELS * 2)
           # stream.write(soundData, CHUNK)


s.close()
stream.close()
p.terminate()
cv.destroyAllWindows()
