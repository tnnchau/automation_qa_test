# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:14:48 2022

@author: chaus
"""
from Toyota import Toyota
from Car import Car
from BMW import BMW


if __name__ == "__main__":
    toyotaCar = Toyota()
    bmwCar = BMW()
    
    t1=Car(toyotaCar.getMaxSpeed())
    t2=Car(bmwCar.getMaxSpeed())
    
    t1.start()
    t2.start()
