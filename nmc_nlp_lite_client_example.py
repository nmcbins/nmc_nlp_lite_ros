#!/usr/bin/env python

#2020.5.24
#Example code nmc_nlp_lite_client_example_sub.py:  
# For synchronous use of ROS node "nmc_nlp_lite" through ROS service call.

import rospy
from nmc_nlp_lite.srv import *
import time
nmcNLPService = rospy.ServiceProxy('nmc_nlp_service', nmcNLP)
binsClientQid = "p7INVIHYDQM"

def call_nmcNLPService(inputString):
    rospy.wait_for_service('nmc_nlp_service')
    try:
        nmcRequest =nmcNLPRequest(binsClientQid,inputString)
        nmcResponse = nmcNLPService(nmcRequest)
        return nmcResponse.binsOutput
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
	testSentence = "a male b"
	while True:
		nmc_nlp_lite_result = call_nmcNLPService(testSentence)
		print "response:" + nmc_nlp_lite_result
		time.sleep(1)