#import the joy of programming python module pyjop
from pyjop import *
import time

def getway(aObject, aNumber):
    first_left = ["Box", "Cone"]
    second_left = ["Cone"] 
    
    if aNumber == 1:
        if aObject in first_left:
            return 5
        else:
            return -5
    else:
        if aObject in second_left:
            return 5
        else:
            return -5
    

#connect to the current SimEnv
SimEnv.connect()

#create references to entities in the SimEnv
env = SimEnvManager.first()

#initialize
current_scan2 = ""

ConveyorBelt.find("belt0").set_target_speed(4)
ConveyorBelt.find("belt2").set_target_speed(5)
ConveyorBelt.find("belt3").set_target_speed(5)
scanner_1 = RangeFinder.find("scan0")
scanner_2 = RangeFinder.find("scan1")
first_conv = ConveyorBelt.find("belt1")
second_conv = ConveyorBelt.find("belt4")

while SimEnv.run_main():
   
    #bestimmen der ersten Richtung
    if ConveyorBelt.find("belt0").get_is_transporting() == 0:
        ObjectSpawner.find("spawner").spawn()
    
    if first_conv.get_is_transporting() == 0:
        first_conv.set_target_speed(getway(scanner_1.get_rfid_tag(),1))       
    
    if second_conv.get_is_transporting() == 0:
        second_conv.set_target_speed(getway(scanner_2.get_rfid_tag(),2))
    
                                 
                                 
#cleanup close code
SimEnv.disconnect()