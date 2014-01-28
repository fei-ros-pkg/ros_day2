#!/usr/bin/env python

from day2_service.srv import *
import rospy

def handle_add_two_ints(req):
    rospy.loginfo("request: x=%ld, y=%ld" % (req.a, req.b))
    rospy.loginfo("sending back response: [%ld]" % (req.a+req.b))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server_py')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

