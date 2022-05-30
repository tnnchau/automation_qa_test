# -*- coding: utf-8 -*-
"""
Created on Mon May 30 23:46:19 2022

@author: chaus
"""
"""
    The outputs from Q1 and Q2 are different because they are on different threads and the time execution is different from each other
    This allows to implement 2 or more tasks at the same time to faster overall execution
        
    To make Q2 produce order like Q1, we have to wait for the first thread to be finished before the second thread gets started 
"""

from Toyota import Toyota
from Car import Car
from BMW import BMW

if __name__ == "__main__":
    toyotaCar = Toyota()
    bmwCar = BMW()
    
    t1=Car(toyotaCar.getMaxSpeed())
    t1.start()
    t1.join()
    
    t2=Car(bmwCar.getMaxSpeed())
    t2.start()
    t2.join()
