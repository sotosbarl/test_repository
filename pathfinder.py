#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
#specify the name of the file (complete path may be a good practice here)
f=open('waypoint_list.txt')


def callback(msg):
# get our current position from amcl
    x=msg.pose.pose.position.x
    y=msg.pose.pose.position.y
#wait for 1.5 secs,then save the current point. Continue with the next point
    rospy.sleep(1.5)
    f.write(x y)
	


def position_provider():
    rospy.init_node('position_listener', anonymous=True)
    rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped  , callback)
    rospy.spin()


if __name__ == '__main__':
    while True:
    	try position_provider()
	except rospy.ROSInterruptException:
		f.close()
