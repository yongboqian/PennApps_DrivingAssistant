#!/usr/bin/env python

import sys
import os
import copy
import rospy
import geometry_msgs.msg
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Bool
from snap_vision_msgs.msg import *

class driving_feedback_node():
      
      def __init__(self):

          print "======================Starting feedback"
          rospy.init_node('driving_feedback', anonymous=True)
          rospy.on_shutdown(self.shutdown)
          self.rate = rospy.get_param("~node_rate", 10)
          r = rospy.Rate(self.rate)
          self.active = False
          rospy.Subscriber("~/detector_manager_node/detections", DetectionsStamped, self.DetectionCb)
          rospy.Subscriber("~/feedback/activeCmd", Bool, self.ActiveCb)
          rospy.Subscriber("~/roll_val", String, self.MotionCb)
          self.turning = 0
          rospy.spin()
      
      def ActiveCb(self,data):
          self.active = data.data
          print(self.active)

      def MotionCb(self,data):
          if self.active and data.data:
             direction = data.data
             print(direction)
             if direction == 'l':
                self.turning = 1
             if direction == 'r':
                self.turning = 2
             if direction == 'm':
                self.turning = 0

      def DetectionCb(self,data):
          if data.detections and self.active:
             #print(self.turning)
             print(data.detections[0].label)
             if data.detections[0].label == 'frontalface' and self.turning == 1:
                os.system("rosrun sound_play say.py 'You are turning left, please observe every direction'")
                rospy.sleep(3)
             if data.detections[0].label == 'frontalface' and self.turning == 2:
                os.system("rosrun sound_play say.py 'You are turning right, please observe every direction'")   
                rospy.sleep(2)     
             if data.detections[0].label == 'profileface' and self.turning == 0:
                os.system("rosrun sound_play say.py 'Please focus, look ahead'")
                rospy.sleep(2)
                
      def shutdown(self):
          rospy.loginfo("Shutting down Node...")

if __name__=='__main__':
  try:
    my_node = driving_feedback_node()
  except rospy.ROSInterruptException:
    pass

