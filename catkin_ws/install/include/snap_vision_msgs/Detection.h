// Generated by gencpp from file snap_vision_msgs/Detection.msg
// DO NOT EDIT!


#ifndef SNAP_VISION_MSGS_MESSAGE_DETECTION_H
#define SNAP_VISION_MSGS_MESSAGE_DETECTION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <snap_vision_msgs/BoundingBox.h>

namespace snap_vision_msgs
{
template <class ContainerAllocator>
struct Detection_
{
  typedef Detection_<ContainerAllocator> Type;

  Detection_()
    : label()
    , bbox()
    , confidence(0.0)  {
    }
  Detection_(const ContainerAllocator& _alloc)
    : label(_alloc)
    , bbox(_alloc)
    , confidence(0.0)  {
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _label_type;
  _label_type label;

   typedef  ::snap_vision_msgs::BoundingBox_<ContainerAllocator>  _bbox_type;
  _bbox_type bbox;

   typedef float _confidence_type;
  _confidence_type confidence;




  typedef boost::shared_ptr< ::snap_vision_msgs::Detection_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::snap_vision_msgs::Detection_<ContainerAllocator> const> ConstPtr;

}; // struct Detection_

typedef ::snap_vision_msgs::Detection_<std::allocator<void> > Detection;

typedef boost::shared_ptr< ::snap_vision_msgs::Detection > DetectionPtr;
typedef boost::shared_ptr< ::snap_vision_msgs::Detection const> DetectionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::snap_vision_msgs::Detection_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::snap_vision_msgs::Detection_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::snap_vision_msgs::Detection_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::snap_vision_msgs::Detection_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::snap_vision_msgs::Detection_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::snap_vision_msgs::Detection_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::snap_vision_msgs::Detection_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::snap_vision_msgs::Detection_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::snap_vision_msgs::Detection_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c998c292bb59f9fe1e85550795cdc57f";
  }

  static const char* value(const ::snap_vision_msgs::Detection_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc998c292bb59f9feULL;
  static const uint64_t static_value2 = 0x1e85550795cdc57fULL;
};

template<class ContainerAllocator>
struct DataType< ::snap_vision_msgs::Detection_<ContainerAllocator> >
{
  static const char* value()
  {
    return "snap_vision_msgs/Detection";
  }

  static const char* value(const ::snap_vision_msgs::Detection_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::snap_vision_msgs::Detection_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string label\n\
BoundingBox bbox\n\
float32 confidence\n\
\n\
================================================================================\n\
MSG: snap_vision_msgs/BoundingBox\n\
float32 x\n\
float32 y\n\
float32 width\n\
float32 height\n\
";
  }

  static const char* value(const ::snap_vision_msgs::Detection_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::snap_vision_msgs::Detection_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.label);
      stream.next(m.bbox);
      stream.next(m.confidence);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct Detection_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::snap_vision_msgs::Detection_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::snap_vision_msgs::Detection_<ContainerAllocator>& v)
  {
    s << indent << "label: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.label);
    s << indent << "bbox: ";
    s << std::endl;
    Printer< ::snap_vision_msgs::BoundingBox_<ContainerAllocator> >::stream(s, indent + "  ", v.bbox);
    s << indent << "confidence: ";
    Printer<float>::stream(s, indent + "  ", v.confidence);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SNAP_VISION_MSGS_MESSAGE_DETECTION_H
