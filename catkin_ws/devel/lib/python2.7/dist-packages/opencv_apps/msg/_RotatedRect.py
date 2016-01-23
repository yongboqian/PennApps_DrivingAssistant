# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from opencv_apps/RotatedRect.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import opencv_apps.msg

class RotatedRect(genpy.Message):
  _md5sum = "0ae60505c52f020176686d0689b8d390"
  _type = "opencv_apps/RotatedRect"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 angle
Point2D center
Size size

================================================================================
MSG: opencv_apps/Point2D
float64 x
float64 y


================================================================================
MSG: opencv_apps/Size
float64 width
float64 height


"""
  __slots__ = ['angle','center','size']
  _slot_types = ['float64','opencv_apps/Point2D','opencv_apps/Size']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       angle,center,size

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RotatedRect, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.angle is None:
        self.angle = 0.
      if self.center is None:
        self.center = opencv_apps.msg.Point2D()
      if self.size is None:
        self.size = opencv_apps.msg.Size()
    else:
      self.angle = 0.
      self.center = opencv_apps.msg.Point2D()
      self.size = opencv_apps.msg.Size()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_5d.pack(_x.angle, _x.center.x, _x.center.y, _x.size.width, _x.size.height))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.center is None:
        self.center = opencv_apps.msg.Point2D()
      if self.size is None:
        self.size = opencv_apps.msg.Size()
      end = 0
      _x = self
      start = end
      end += 40
      (_x.angle, _x.center.x, _x.center.y, _x.size.width, _x.size.height,) = _struct_5d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_5d.pack(_x.angle, _x.center.x, _x.center.y, _x.size.width, _x.size.height))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.center is None:
        self.center = opencv_apps.msg.Point2D()
      if self.size is None:
        self.size = opencv_apps.msg.Size()
      end = 0
      _x = self
      start = end
      end += 40
      (_x.angle, _x.center.x, _x.center.y, _x.size.width, _x.size.height,) = _struct_5d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_5d = struct.Struct("<5d")
