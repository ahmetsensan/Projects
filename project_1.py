# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:38:06 2019

@author: Ahmet Şensan
"""

#%%  Example 
    
#1640. yil == 17. yuzyil
#109. yil == 2. yuzyil
# 200. yil == 20. yuzyil

#metod yazın 
    #input integer yillar
    #output yuzyil
    

def year2century(year):
    """
    year to century
    """
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    
    elif(len(str_year) == 3):
        
        if(str_year[1:3] == "00"):
            return int(str_year[0])
        else:
            return int(str_year[0]) +1
    else:
        if (str_year[2:4 == "00"]):
            return int (str_year[:2])
        else:
            return int (str_year[:2])+1