#!/usr/bin/env python

import rospy
import math

from std_msgs.msg import Float64
from math import sin,cos,atan2,sqrt,fabs


#Define a RRBot joint positions publisher for joint controllers.
def rrbot_joint_positions_publisher():

    #Initiate node for controlling joint1 and joint2 positions of robot 1 & 2.
    rospy.init_node('joint_positions_node_rrbot3', anonymous=True)

    #Initiate node for controlling joint1 and joint2 positions of robot 1.

    #Define publishers for each joint position controller commands.

    pub2_j1 = rospy.Publisher('/rrbot3/joint1_position_controller/command', Float64, queue_size=10)
    pub2_j2 = rospy.Publisher('/rrbot3/joint2_position_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(80) #100 Hz

    #While loop to have joints follow a certain position, while rospy is not shutdown.
    i = 0
    while not rospy.is_shutdown():

        #Have each joint follow a sine movement of sin(i/100).
        sine_movement = sin(i/80.)

        #Publish the same sine movement to each joint.
        pub2_j1.publish(sine_movement)
        pub2_j2.publish(sine_movement)

        i = i+1 #increment i

        rate.sleep() #sleep for rest of rospy.Rate(100)


#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
    try: rrbot_joint_positions_publisher()
    except rospy.ROSInterruptException: pass
