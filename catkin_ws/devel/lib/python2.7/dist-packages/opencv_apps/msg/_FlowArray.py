# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from opencv_apps/FlowArray.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import opencv_apps.msg

class FlowArray(genpy.Message):
  _md5sum = "fe292dca56eb3673cd698ea9ef841962"
  _type = "opencv_apps/FlowArray"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Flow[] flow

================================================================================
MSG: opencv_apps/Flow
Point2D point
Point2D velocity

================================================================================
MSG: opencv_apps/Point2D
float64 x
float64 y


"""
  __slots__ = ['flow']
  _slot_types = ['opencv_apps/Flow[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       flow

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FlowArray, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.flow is None:
        self.flow = []
    else:
      self.flow = []

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
      length = len(self.flow)
      buff.write(_struct_I.pack(length))
      for val1 in self.flow:
        _v1 = val1.point
        _x = _v1
        buff.write(_struct_2d.pack(_x.x, _x.y))
        _v2 = val1.velocity
        _x = _v2
        buff.write(_struct_2d.pack(_x.x, _x.y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.flow is None:
        self.flow = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.flow = []
      for i in range(0, length):
        val1 = opencv_apps.msg.Flow()
        _v3 = val1.point
        _x = _v3
        start = end
        end += 16
        (_x.x, _x.y,) = _struct_2d.unpack(str[start:end])
        _v4 = val1.velocity
        _x = _v4
        start = end
        end += 16
        (_x.x, _x.y,) = _struct_2d.unpack(str[start:end])
        self.flow.append(val1)
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
      length = len(self.flow)
      buff.write(_struct_I.pack(length))
      for val1 in self.flow:
        _v5 = val1.point
        _x = _v5
        buff.write(_struct_2d.pack(_x.x, _x.y))
        _v6 = val1.velocity
        _x = _v6
        buff.write(_struct_2d.pack(_x.x, _x.y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.flow is None:
        self.flow = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.flow = []
      for i in range(0, length):
        val1 = opencv_apps.msg.Flow()
        _v7 = val1.point
        _x = _v7
        start = end
        end += 16
        (_x.x, _x.y,) = _struct_2d.unpack(str[start:end])
        _v8 = val1.velocity
        _x = _v8
        start = end
        end += 16
        (_x.x, _x.y,) = _struct_2d.unpack(str[start:end])
        self.flow.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2d = struct.Struct("<2d")
