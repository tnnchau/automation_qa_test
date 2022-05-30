# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:50:01 2022

@author: chaus
"""
import time
import threading

class Car(threading.Thread):
    def __init__(self, maxSpeed):
        threading.Thread.__init__(self)
        self._wheels = 4
        self._doors = 5
        self._seats = 5
        self._maxSpeed = maxSpeed
        
    def getWheels(self):
        return self._wheels
    
    def setWheels(self, wheels):
        self._wheels = wheels
        
    def getDoors(self):
        return self._doors
    
    def setDoors(self, doors):
        self._doors = doors

    def getSeats(self):
        return self._seats
    
    def setSeats(self, seats):
        self._seats = seats
        
    def getMaxSpeed(self):
        return self._maxSpeed
    
    def setMaxSpeed(self, maxSpeed):
        self._maxSpeed = maxSpeed
        
    def run(self):
        for i in range(10):
            print("Max Speed: {}".format(self.getMaxSpeed()))
            time.sleep(1)
        print("\n")
            
    def info(self):
        for i in range(10):
            print("Wheels: {}".format(self.getWheels())) 
            print("Doors: {}".format(self.getDoors())) 
            print("Seats: {}".format(self.getSeats()))
        print("\n")
    