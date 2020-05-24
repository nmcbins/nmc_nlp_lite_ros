#!/usr/bin/env python

#2020.5.13 this is the nmc_nlp_lite ROS package main file.
#import roslib  #for listner
#import sys  #for listener 
import rospy #for talker & listner 
from std_msgs.msg import String #for talker & listner 
from nmc_nlp_lite.srv import nmcNLP,nmcNLPResponse

import nmcbins

pub = rospy.Publisher('nmc_nlp_out', String, queue_size=10)
rospy.init_node('nmc_nlp', anonymous=True)  # 'nmc_nlp' as node name is overwritten by the name specified in nmc_nlp_lite.launch file.
nmcbins.setQid("p7INVIHYDQM")
text_to_process = 'a male b'

def callback_subscriber(data):
	rospy.loginfo(rospy.get_caller_id() + "  nmc_nlp server received: %s", data.data)
	b=nmcbins.normalize(text_to_process)
	rospy.loginfo(b)
	msg = rospy.get_caller_id() + "  relay relay relay" + data.data
	pub.publish(msg)

def callback_service(req):
	b=nmcbins.normalize(req.binsInputSentence)
	return nmcNLPResponse("bins_input:"+req.binsInputSentence + "\n bins_output:" + b)

def listener():
    #rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("nmc_nlp_in", String, callback_subscriber)
    rospy.Service("nmc_nlp_service",nmcNLP, callback_service)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()