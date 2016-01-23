// Generated by gencpp from file snap_vision_msgs/DetectorResponse.msg
// DO NOT EDIT!


#ifndef SNAP_VISION_MSGS_MESSAGE_DETECTORRESPONSE_H
#define SNAP_VISION_MSGS_MESSAGE_DETECTORRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <snap_vision_msgs/Error.h>

namespace snap_vision_msgs
{
template <class ContainerAllocator>
struct DetectorResponse_
{
  typedef DetectorResponse_<ContainerAllocator> Type;

  DetectorResponse_()
    : error()  {
    }
  DetectorResponse_(const ContainerAllocator& _alloc)
    : error(_alloc)  {
    }



   typedef  ::snap_vision_msgs::Error_<ContainerAllocator>  _error_type;
  _error_type error;




  typedef boost::shared_ptr< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> const> ConstPtr;

}; // struct DetectorResponse_

typedef ::snap_vision_msgs::DetectorResponse_<std::allocator<void> > DetectorResponse;

typedef boost::shared_ptr< ::snap_vision_msgs::DetectorResponse > DetectorResponsePtr;
typedef boost::shared_ptr< ::snap_vision_msgs::DetectorResponse const> DetectorResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace snap_vision_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'snap_vision_msgs': ['/home/yongbo/Documents/PennApps/catkin_ws/src/snap_vision_msgs/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fd1abad6def016f6ee32938bdf511479";
  }

  static const char* value(const ::snap_vision_msgs::DetectorResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfd1abad6def016f6ULL;
  static const uint64_t static_value2 = 0xee32938bdf511479ULL;
};

template<class ContainerAllocator>
struct DataType< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "snap_vision_msgs/DetectorResponse";
  }

  static const char* value(const ::snap_vision_msgs::DetectorResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Error error\n\
\n\
\n\
================================================================================\n\
MSG: snap_vision_msgs/Error\n\
# Language independent enum constants\n\
uint16 E_OK                    = 0\n\
uint16 E_MODEL_NOT_UNLOADED    = 1\n\
uint16 E_MODEL_NOT_LOADED      = 2\n\
uint16 E_DETECTOR_NOT_FOUND    = 4\n\
uint16 E_MODEL_NOT_FOUND       = 8\n\
uint16 E_FILE_NOT_FOUND        = 16\n\
uint16 E_STUB                  = 65534\n\
uint16 E_UNKNOWN_ERROR         = 65535\n\
\n\
uint16  err_code\n\
string err_str\n\
";
  }

  static const char* value(const ::snap_vision_msgs::DetectorResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.error);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct DetectorResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::snap_vision_msgs::DetectorResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::snap_vision_msgs::DetectorResponse_<ContainerAllocator>& v)
  {
    s << indent << "error: ";
    s << std::endl;
    Printer< ::snap_vision_msgs::Error_<ContainerAllocator> >::stream(s, indent + "  ", v.error);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SNAP_VISION_MSGS_MESSAGE_DETECTORRESPONSE_H
