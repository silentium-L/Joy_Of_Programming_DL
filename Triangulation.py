#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

#create references to entities in the SimEnv
env = SimEnvManager.first()

while SimEnv.run_main():
    # main loop to retrieve data from the SimEnv, calculate stuff and send commands back into the SimEnv
    # for example, get current time and display it
    simtime = env.get_sim_time()
    print(f"current time: {simtime} seconds")

	
#cleanup close code
SimEnv.disconnect()
