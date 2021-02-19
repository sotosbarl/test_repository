#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped 
#we have defined a new msg called stanley that contains 7 floats 
from stanley_control.msg import stanley

#initialise the publisher
coordinates = rospy.Publisher('current_coordinates', stanley, queue_size=100)
pub=stanley()
rospy.init_node('position_provider', anonymous=True)
rate = rospy.Rate(10) # 10hz
#open our file and read the data
f=open('FILENAME.txt')
waypoint_list=f.readlines

def callback(msg):
#firstly get our current position/orientation
    x=msg.pose.pose.position.x
    y=msg.pose.pose.position.y
    yaw=msg.pose.pose.orientation.z
###############################################################
#THIS PART NEEDS TO BE COMPLETED
####################################################################
#then find the nearest waypoint from our list
    for xi in waypoint_list: #and/or yi?
	if abs(xi-x)<0.5:
		min_x=xi
		min_y=yi
		break

#################################################################

#publish the coordinates and we are done!
#position 
stanley.x=x
stanley.y=y
stanley.yaw=yaw
#waypoints
stanley.x_min=x_min
stanley.y_min=y_min
stanley.x_min=x_min_next
stanley.y_min=y_min_next
coordinates.publish(pub)

#initialise the subscriber node
def position_provider():
    rospy.init_node('position_listener', anonymous=True)
    rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped  , callback)
    rospy.spin()

 
if __name__ == '__main__':
    position_provider()

