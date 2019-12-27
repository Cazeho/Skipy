#!/usr/bin/env python
import socket
import numpy as np
import cv2 as cv
import pyaudio
import sys
import threading
import wave
import time

#send audio data
# Pyaudio Initialization
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
#size = 512
######################

#bind
addr = ("127.0.0.1", 8080)
buf = 8192
width = 640
height = 480
cap = cv.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
code = 'start'
code = ('start' + (buf - len(code)) * 'a').encode('utf-8')
##########################
class sound:
    def speak(self, data):
        #while self.mute is False:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            print("you speak {}".format(audio))
            data = stream.read(sample)
            s.sendto(data, addr)
            
            
    def speakStart(self):
        t = threading.Thread(target=self.speak(data))
        t.start()
        
#    def __init__(self,mode=1,name="w1",capture=1):
 #       print (name)
  #      self.name=name
   #     self.mute = False
        
#################
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            s.sendto(code, addr)
            data = frame.tostring()
            for i in range(0, len(data), buf):
                s.sendto(data[i:i+buf], addr)

               # cv.imshow('send', frame)
            #if cv.waitKey(1) & 0xFF == ord('q'):
           # so=sound(1,"test",1)
           # while 1:
             #   m=so.speakStart()
            #    so.speak(m)        #break
        else:
            break
      #  while True:
             #   s.sendto(stream.read(CHUNK), ("127.0.0.1", 8080))
stream.stop_stream()
stream.close()       
p.terminate()
