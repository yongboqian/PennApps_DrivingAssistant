#define USE_USBCON
#include <ros.h>
#include <std_msgs/String.h>
#include "Wire.h"
#include "SparkFunIMU.h"
#include "SparkFunLSM303C.h"
#include "LSM303CTypes.h"

ros::NodeHandle nh;
std_msgs::String roll_msg;
ros::Publisher roll_val("roll_val", &roll_msg);

char left[2] = "l";
char right[2] = "r";

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
  //Serial.print(" Z = ");
  //Serial.println(myIMU.readAccelZ(), 4);
  //Serial.print(" Y = ");
  //Serial.println(myIMU.readAccelY(), 4);
//  float f;
//  f = myIMU.readAccelY();
  int Z = (int)myIMU.readAccelZ();
  if (Z<-500){
     roll_msg.data = right;
     roll_val.publish(&roll_msg);
  }
  if (Z > 500){
     roll_msg.data = left;
     roll_val.publish(&roll_msg);
  }
  //roll_msg.data = (int)myIMU.readAccelY();
  
  nh.spinOnce();
  delay(1000);
}
