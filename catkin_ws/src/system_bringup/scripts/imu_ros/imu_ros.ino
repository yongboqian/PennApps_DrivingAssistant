#define USE_USBCON
#include <ros.h>
#include <std_msgs/Int32.h>
#include "Wire.h"
#include "SparkFunIMU.h"
#include "SparkFunLSM303C.h"
#include "LSM303CTypes.h"

ros::NodeHandle nh;
std_msgs::Int32 roll_msg;
ros::Publisher roll_val("roll_val", &roll_msg);


LSM303C myIMU;

void setup()
{
  nh.initNode();
  nh.advertise(roll_val);
  Serial.begin(115200);
  //myIMU.begin();
  if (myIMU.begin() != IMU_SUCCESS)
     {
      Serial.println("Failed setup.");
      while(1);
     }
}

void loop()
{
  //Get all parameters
  //Serial.print("\nAccelerometer:\n");
  //Serial.print(" X = ");
  //Serial.println(myIMU.readAccelX(), 4);
//  Serial.print(" Y = ");
//  Serial.println(myIMU.readAccelY(), 4);
//  float f;
//  f = myIMU.readAccelY();
  //int Y = 
  roll_msg.data = (int)myIMU.readAccelY();
  roll_val.publish(&roll_msg);
  nh.spinOnce();
  delay(1000);
}
