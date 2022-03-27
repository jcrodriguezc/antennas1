import math
from urllib.request import AbstractHTTPHandler


def num_zones(): 
    zones = input("Enter the number of zones to analyze: ")
    while type(zones)!=int:
        try:
            zones = int(zones)
            while zones <1:
                zones = input("The number of zones must be an integer greater than 0, try again: ")
        except:
            zones = input("The number of zones must be an integer greater than 0, try again: ")            
    return zones

def m2_zone():
    m2_zone = input("Enter de area of the zone (m2): ")
    while type(m2_zone)!=float:
        try:
            m2_zone = float(m2_zone)
            if m2_zone >0:
                return m2_zone
            else:
                m2_zone = input("The area most be a number greater than 0, try again: ")    
        except:
            m2_zone = input("The area most be a number greater tha 0, try again: ")    

def previus_antennas():
    previus_antennas = input("Enter the number of antennas installed in the area ")
    while type(previus_antennas)!=int:
        try:
            previus_antennas = int(previus_antennas)
            while previus_antennas < 0:
                previus_antennas = input("The quantity must be an integer greater than 0: ")
        except:
            previus_antennas = input("The quantity must be an integer greater than 0:  ")
    return previus_antennas

def type_antenna():     
    type_new_antenna = str.lower(input("Enter the type of new antennas to install (a,b,c,d,e): "))
    while type_new_antenna != "a" and type_new_antenna != "b" and type_new_antenna != "c" and type_new_antenna != "d" and type_new_antenna != "e":
        type_new_antenna= str.lower(input("Antenna type is not within options (a,b,c,d,e), Try again: "))    
    return type_new_antenna

def coverage_antennas(type_antenna):  
    coverage_new_antennas={"a":33600, "b":48900, "c":17000, "d":21000, "e":42600}
    type_new_antenna = type_antenna
    coverage_antenna = coverage_new_antennas[type_new_antenna]        
    return coverage_antenna

def new_antennas():
    antenna_coverage = 8400
    zones = num_zones()
    antennas_for_type = {"total":0,"a":0,"b":0,"c":0, "d":0, "e":0}    
    for i in range (zones):        
        area = m2_zone()
        antennas = previus_antennas()       
        type_new_antenna = type_antenna()
        coverage_new_antenna = coverage_antennas(type_new_antenna)        
        current_coverage = antenna_coverage * antennas               
        area_to_be_covered = area - current_coverage
        if area_to_be_covered<0:
            area_to_be_covered=0        
        new_antennas = math.ceil(area_to_be_covered/coverage_new_antenna) 
        antennas_for_type[type_new_antenna]=antennas_for_type[type_new_antenna]+new_antennas
        antennas_for_type["total"]=antennas_for_type["total"]+new_antennas        
    return antennas_for_type
        
def percentage():
    total_antennas = new_antennas()
    total_antennas["a"] = round(total_antennas["a"]*100/total_antennas["total"],2)
    total_antennas["b"] = round(total_antennas["b"]*100/total_antennas["total"],2)
    total_antennas["c"] = round(total_antennas["c"]*100/total_antennas["total"],2)
    total_antennas["d"] = round(total_antennas["d"]*100/total_antennas["total"],2)
    total_antennas["e"] = round(total_antennas["e"]*100/total_antennas["total"],2)  
    return print("Total ", total_antennas["total"], "antennas - ", "a ",total_antennas["a"],"% - ","b ",total_antennas["b"],"% - ", "c ", total_antennas["c"], "% - ","d ",total_antennas["d"], "% - ","e ",total_antennas["e"])

percentage()