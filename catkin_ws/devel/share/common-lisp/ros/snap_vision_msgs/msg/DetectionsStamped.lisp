; Auto-generated. Do not edit!


(cl:in-package snap_vision_msgs-msg)


;//! \htmlinclude DetectionsStamped.msg.html

(cl:defclass <DetectionsStamped> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (detections
    :reader detections
    :initarg :detections
    :type (cl:vector snap_vision_msgs-msg:Detection)
   :initform (cl:make-array 0 :element-type 'snap_vision_msgs-msg:Detection :initial-element (cl:make-instance 'snap_vision_msgs-msg:Detection))))
)

(cl:defclass DetectionsStamped (<DetectionsStamped>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectionsStamped>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectionsStamped)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name snap_vision_msgs-msg:<DetectionsStamped> is deprecated: use snap_vision_msgs-msg:DetectionsStamped instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <DetectionsStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader snap_vision_msgs-msg:header-val is deprecated.  Use snap_vision_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'detections-val :lambda-list '(m))
(cl:defmethod detections-val ((m <DetectionsStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader snap_vision_msgs-msg:detections-val is deprecated.  Use snap_vision_msgs-msg:detections instead.")
  (detections m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectionsStamped>) ostream)
  "Serializes a message object of type '<DetectionsStamped>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'detections))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'detections))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectionsStamped>) istream)
  "Deserializes a message object of type '<DetectionsStamped>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'detections) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'detections)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'snap_vision_msgs-msg:Detection))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectionsStamped>)))
  "Returns string type for a message object of type '<DetectionsStamped>"
  "snap_vision_msgs/DetectionsStamped")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectionsStamped)))
  "Returns string type for a message object of type 'DetectionsStamped"
  "snap_vision_msgs/DetectionsStamped")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectionsStamped>)))
  "Returns md5sum for a message object of type '<DetectionsStamped>"
  "a51185277c0105cae82104e7b230d2a6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectionsStamped)))
  "Returns md5sum for a message object of type 'DetectionsStamped"
  "a51185277c0105cae82104e7b230d2a6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectionsStamped>)))
  "Returns full string definition for message of type '<DetectionsStamped>"
  (cl:format cl:nil "Header header~%Detection[] detections~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: snap_vision_msgs/Detection~%string label~%BoundingBox bbox~%float32 confidence~%~%================================================================================~%MSG: snap_vision_msgs/BoundingBox~%float32 x~%float32 y~%float32 width~%float32 height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectionsStamped)))
  "Returns full string definition for message of type 'DetectionsStamped"
  (cl:format cl:nil "Header header~%Detection[] detections~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: snap_vision_msgs/Detection~%string label~%BoundingBox bbox~%float32 confidence~%~%================================================================================~%MSG: snap_vision_msgs/BoundingBox~%float32 x~%float32 y~%float32 width~%float32 height~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectionsStamped>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'detections) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectionsStamped>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectionsStamped
    (cl:cons ':header (header msg))
    (cl:cons ':detections (detections msg))
))
