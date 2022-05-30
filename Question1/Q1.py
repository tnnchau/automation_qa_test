# -*- coding: utf-8 -*-
"""
Created on Mon May 30 21:21:53 2022

@author: chaus
"""
from Toyota import Toyota
from BMW import BMW

if __name__ == "__main__":
    toyotaCar = Toyota()
    bmwCar = BMW()
    
    toyotaCar.run()
    bmwCar.run()