"""
  Lesson 7 - hover above oriented roundel sign
"""
import sys
import os
import inspect

ARDRONE2_ROOT = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"..")))
if ARDRONE2_ROOT not in sys.path:
    sys.path.insert(0, ARDRONE2_ROOT) # access to drone source without installation

from ardrone2 import ARDrone2, ManualControlException

def hoverAboveRoundel( drone, timeout=10.0 ):
    startTime = drone.time
    maxSpeed = 0.3
    while drone.time - startTime < timeout:
        sx, sy, sz, sa = 0.0, 0.0, 0.0, 0.0
        if drone.visionTag:
            # xc[i], yc[i]: X and Y coordinates of detected tag or oriented roundel #i inside the picture,
            # with (0; 0) being the top-left corner, and (1000; 1000) the right-bottom corner regardless
            # the picture resolution or the source camera
            x, y = drone.visionTag[0][:2]
            sx = maxSpeed * (500-y)/500.0
            sy = maxSpeed * (500-x)/500.0
            print sx
        drone.moveXYZA( sx, sy, sz, sa )
    drone.hover(0.1) # stop motion


def testLesson7( drone ):
    try:
        drone.startVideo( record=True, highResolution=False )
        drone.setVideoChannel( front=False )
        drone.takeoff()
        hoverAboveRoundel( drone )
    except ManualControlException, e:
        print "ManualControlException"
    if drone.ctrlState == 3: # CTRL_FLYING=3 ... i.e. stop the current motion
        drone.hover(0.1)
    drone.land()
    drone.stopVideo()
    print "Battery", drone.battery



if __name__ == "__main__":
    import launcher
    launcher.launch( sys.argv, ARDrone2, testLesson7 )


# vim: expandtab sw=4 ts=4

