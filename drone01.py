import time
from codrone_edu.drone import *

drone = Drone()
drone.pair()

time.sleep(15)

drone.takeoff()

drone.move_forward(55, "in")

drone.turn_degree(-90)

drone.move_forward(27, "in")

drone.turn_degree(0)

drone.move_forward(65, "in")

drone.turn_degree(-90)

drone.move_forward(64, "in")

drone.flip("back")

drone.land()
drone.close()