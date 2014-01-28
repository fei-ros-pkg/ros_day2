#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter', String)
    rospy.init_node('talker_py')
    count = 0
    while not rospy.is_shutdown():
        str = "this is message number %d" % count
        rospy.loginfo(str)
        pub.publish(String(str))
        rospy.sleep(1.0)
        count += 1


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

