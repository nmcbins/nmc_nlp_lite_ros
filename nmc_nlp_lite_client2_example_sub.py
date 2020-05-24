#!/usr/bin/env python

#Example code nmc_nlp_lite_client2_example_sub.py:  
# For asynchronous use of ROS node "nmc_nlp_lite", use this subscriber to receive processing result.

import rospy
from nmc_nlp_lite.msg import nmcNLPMsg

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "  I heard %s", data.binsSentence)
	# add business logic here.

def nmc_nlp_lite_listener():
    rospy.init_node('nmc_nlp_lite_listener', anonymous=True)
    rospy.Subscriber("nmc_nlp_out", nmcNLPMsg, callback)
    rospy.spin()

if __name__ == '__main__':
    nmc_nlp_lite_listener()