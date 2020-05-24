#!/usr/bin/env python

#2020.5.13 This is the nmc_nlp_lite ROS package main file.
#2020.5.13 Its main function: a ROS node that accesses a cloud-based light-weight natural language normalization service, which is hosted at www.nmcomputing.com
#  AS a ROS node it can be accessed through a service call, or through publish/subscribe mode.

import rospy #for talker & listner 
from nmc_nlp_lite.srv import nmcNLP,nmcNLPResponse
from nmc_nlp_lite.msg import nmcNLPMsg
import nmc_bins as nmcbins

pub = rospy.Publisher('nmc_nlp_out', nmcNLPMsg, queue_size=10)

def callback_for_subscriber(bins_input):
	msg = rospy.get_caller_id() + "  relay relay relay" + bins_input.binsSentence
	rospy.loginfo(msg)
	nmcbins.setQid(bins_input.binsClientQid)
	bins_response=nmcbins.normalize(bins_input.binsSentence)
	bins_output = nmcNLPMsg()
	bins_output.binsClientQid= bins_input.binsClientQid
	bins_output.binsSentence= bins_response
	pub.publish(bins_output)

def callback_for_service(req):
	nmcbins.setQid(req.binsClientQid)
	bins_response=nmcbins.normalize(req.binsInputSentence)
	return nmcNLPResponse("bins_input:"+req.binsInputSentence + "\n bins_output:" + bins_response)

def listener():
    rospy.init_node('nmc_nlp', anonymous=True)  # 'nmc_nlp' as node name is overwritten by the name specified in nmc_nlp_lite.launch file.	
    rospy.Subscriber("nmc_nlp_in", nmcNLPMsg, callback_for_subscriber)
    rospy.Service("nmc_nlp_service",nmcNLP, callback_for_service)
    rospy.spin()

if __name__ == '__main__':
    listener()