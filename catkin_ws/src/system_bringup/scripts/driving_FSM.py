#!/usr/bin/env python

########################
##  Driving Assistant High Level State Machine
##  Voice Control
##  Yongbo Qian @ 2015
import sys
import copy
import rospy
import os
import geometry_msgs.msg
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_msgs.msg import Bool
from snap_vision_msgs.msg import *
from numpy import *

class driving_FSM_node():
  
  def __init__(self):      
      print "============ Starting Driving State Machine"
      #import pdb; pdb.set_trace()
      #moveit_commander.roscpp_initialize(sys.argv)
      rospy.init_node('driving_FSM',
                      anonymous=True)
      # Execute this function when shutting down
      rospy.on_shutdown(self.shutdown)
      
      # Set the update rate to 1 second by default
      self.rate = rospy.get_param("~node_rate", 10)
      r = rospy.Rate(self.rate)
      self.state = 'free'
     # self.state_prev = 'free'
      self.attemps = 0.0
      print "Begining FSM"
      # Begin the main loop
      while not rospy.is_shutdown():
           self.FSM()
           r.sleep()

  def FSM(self):
      print self.state
      self.state == 'free'
      if self.state == 'free':
         received_voice = self.listen("/recognizer/output")
         if received_voice.data == 'launch driving buddy':
            self.state = 'driving'
         else:
            self.state = 'free'

      elif self.state == 'driving':
           os.system("rosrun sound_play say.py 'Driving buddy launched, do not drive after drinking, enjoy your trip'")
           rospy.sleep(4)
           
           cmd = "rosservice call /detector_manager_node/load_models 'model_names: ['frontalface']'"
           os.system(cmd)
           cmd2 = "rosservice call /detector_manager_node/load_models 'model_names: ['profileface']'"
           os.system(cmd2)
           self.state = 'feedback'
           os.system("rostopic pub -1 /feedback/activeCmd std_msgs/Bool True")
       
      elif self.state == 'feedback':
           received_voice = self.listen("/recognizer/output")          
           if received_voice.data == 'end trip':
              self.state = 'end'
      elif self.state == 'end':          
         os.system("rosrun sound_play say.py 'trip ends. Have a nice day'")
         self.state = 'free'
         os.system("rostopic pub -1 /feedback/activeCmd std_msgs/Bool False")
         rospy.sleep(3)
         
      
  def listen(self, topic):
      try:
         #import pdb; pdb.set_trace()
         received_voice = rospy.client.wait_for_message(str(topic),String,timeout=1000)
      except Exception, e:
         #os.system("rosrun sound_play say.py 'I cannot hear you'")
         #rospy.sleep(2)
         received_voice = String()
         received_voice.data = None
         #self.state_prev = self.state
         #self.state = 'speech_timeout'
      return received_voice


  def shutdown(self):
      rospy.loginfo("Shutting down search Node...")


      ## When finished shut down 


      ## END_TUTORIAL

      print "============ STOPPING"


if __name__=='__main__':
  try:
    my_node = driving_FSM_node()
  except rospy.ROSInterruptException:
    pass

