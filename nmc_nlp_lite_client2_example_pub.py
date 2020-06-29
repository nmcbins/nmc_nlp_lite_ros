#!/usr/bin/env python
# Copyright (c) 2020 NMC Corp
# This code is licensed under MIT license (see LICENSE.md for details)
#2020.5.24
#Example code nmc_nlp_lite_client2_example_sub.py:  
# For asynchronous use of ROS node "nmc_nlp_lite", use this publisher to send a natural language sentence to be processed.

import rospy
from nmc_nlp_lite.msg import nmcNLPMsg
binsClientQid = "p7INVIHYDQM"

pub = rospy.Publisher('nmc_nlp_in', nmcNLPMsg, queue_size=10)
rospy.init_node('nmc_nlp_lite_talker', anonymous=True)
rate = rospy.Rate(1) # 10hz
while not rospy.is_shutdown():
   hello_str = " BINS done processing ... hello world %s" % rospy.get_time()
   hello_str = "a male b"
   rospy.loginfo(hello_str)
   msg_to_nmc_nlp_lite = nmcNLPMsg()
   msg_to_nmc_nlp_lite.binsSentence = hello_str
   msg_to_nmc_nlp_lite.binsClientQid = binsClientQid
   pub.publish(msg_to_nmc_nlp_lite)
   rate.sleep()