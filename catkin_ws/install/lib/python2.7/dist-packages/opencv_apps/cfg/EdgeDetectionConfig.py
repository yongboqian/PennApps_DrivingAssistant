## *********************************************************
## 
## File autogenerated for the edge_detection package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 262, 'description': 'Indicates that the camera_info topic should be subscribed to to get the default input_frame_id. Otherwise the frame from the image message will be used.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'use_camera_info', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 262, 'description': 'Edge Detection Methods', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'edge_type', 'edit_method': "{'enum_description': 'An enum for Edge Detection Mehtods', 'enum': [{'srcline': 42, 'description': 'Sobel Derivatives', 'srcfile': '/home/yongbo/Documents/PennApps/catkin_ws/src/vision_opencv/opencv_apps/cfg/EdgeDetection.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Sobel'}, {'srcline': 43, 'description': 'Laplace Operator', 'srcfile': '/home/yongbo/Documents/PennApps/catkin_ws/src/vision_opencv/opencv_apps/cfg/EdgeDetection.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Laplace'}, {'srcline': 44, 'description': 'Canny Edge Detector', 'srcfile': '/home/yongbo/Documents/PennApps/catkin_ws/src/vision_opencv/opencv_apps/cfg/EdgeDetection.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Canny'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 262, 'description': 'Canny Edge low Threshold', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'canny_low_threshold', 'edit_method': '', 'default': 10, 'level': 0, 'min': 1, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

EdgeDetection_Sobel = 0
EdgeDetection_Laplace = 1
EdgeDetection_Canny = 2