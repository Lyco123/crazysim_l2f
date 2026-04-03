from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
import cflib.crtp
import time

URI = 'udp://0.0.0.0:19850'

cflib.crtp.init_drivers()

with SyncCrazyflie(URI) as scf:
    with MotionCommander(scf) as mc:
        mc.forward(0.5)
        time.sleep(1)
        mc.turn_left(90)
        time.sleep(1)

