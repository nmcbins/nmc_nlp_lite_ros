#!/usr/bin/env python

#2020.5.13 this is the nmc_nlp_lite ROS package main file.
import rospy #for talker & listner 
from std_msgs.msg import String #for talker & listner 
from nmc_nlp_lite.srv import nmcNLP,nmcNLPResponse
import nmc_bins as nmcbins

pub = rospy.Publisher('nmc_nlp_out', String, queue_size=10)

def callback_for_subscriber(data):
	rospy.loginfo(rospy.get_caller_id() + "  nmc_nlp server received: %s", data.data)
	#nmcbins.setQid(req.binsClientQid)
	b=nmcbins.normalize(data.data)
	rospy.loginfo(b)
	msg = rospy.get_caller_id() + "  relay relay relay" + data.data
	pub.publish(msg)

def callback_for_service(req):
	nmcbins.setQid(req.binsClientQid)
	b=nmcbins.normalize(req.binsInputSentence)
	return nmcNLPResponse("bins_input:"+req.binsInputSentence + "\n bins_output:" + b)

def listener():
    rospy.init_node('nmc_nlp', anonymous=True)  # 'nmc_nlp' as node name is overwritten by the name specified in nmc_nlp_lite.launch file.	
    rospy.Subscriber("nmc_nlp_in", String, callback_for_subscriber)
    rospy.Service("nmc_nlp_service",nmcNLP, callback_for_service)
    rospy.spin()

if __name__ == '__main__':
    listener()