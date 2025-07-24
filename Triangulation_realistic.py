#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

#create references to entities in the SimEnv
env = SimEnvManager.first()

while SimEnv.run_main():

    #Defining main Objects of use for this Scope
    platform  = MovablePlatform.find("platform")

    # main loop to retrieve data from the SimEnv, calculate stuff and send commands back into the SimEnv
    # for example, get current time and display it
    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")

    #Move Platform to the correct Space
    platform.setTargetLocation(6,0,0)
    platform.setTargetLocation(6,5,0)

    #Function to grab the Barrel from that Point
    getBarrel()

    #Move Platform back
    set_target_location(6,0,0)
    set_target_location(0,0,0)

	
#cleanup close code
SimEnv.disconnect()
