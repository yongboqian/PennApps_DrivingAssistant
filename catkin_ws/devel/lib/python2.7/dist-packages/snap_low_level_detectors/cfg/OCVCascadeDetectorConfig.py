## *********************************************************
## 
## File autogenerated for the snap_low_level_detectors package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 262, 'description': 'Parameter specifying how much the image size is reduced at each image scale', 'max': 3.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'scale_factor', 'edit_method': '', 'default': 1.2, 'level': 0, 'min': 1.05, 'type': 'double'}, {'srcline': 262, 'description': 'Parameter specifying how many neighbors each candidate rectangle should have to retain it.', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_neighbors', 'edit_method': '', 'default': 10, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 262, 'description': 'Minimum possible object width. Objects smaller than that are ignored.', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_width', 'edit_method': '', 'default': 32, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 262, 'description': 'Minimum possible object height. Objects smaller than that are ignored.', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_height', 'edit_method': '', 'default': 32, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 262, 'description': 'Maximum possible object width. Objects larger than that are ignored.', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_width', 'edit_method': '', 'default': 512, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 262, 'description': 'Maximum possible object height. Objects larger than that are ignored.', 'max': 1000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_height', 'edit_method': '', 'default': 512, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 262, 'description': 'Parameter with the same meaning for an old cascade as in the function cvHaarDetectObjects. It is not used for a new cascade.', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flags', 'edit_method': "{'enum_description': 'Mode of operation', 'enum': [{'srcline': 15, 'description': 'No pruning before cascade detection. Not supported anyway for new-style cascades.', 'srcfile': '/home/yongbo/Documents/PennApps/catkin_ws/src/snap_low_level_detectors/cfg/OCVCascadeDetector.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'CV_HAAR_NO_PRUNING'}, {'srcline': 16, 'description': 'Uses Canny edge detector to reject some image regions that contain too few or too much edges and thus can not contain the searched object. The particular threshold values are tuned for face detection and in this case the pruning speeds up the processing', 'srcfile': '/home/yongbo/Documents/PennApps/catkin_ws/src/snap_low_level_detectors/cfg/OCVCascadeDetector.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'CV_HAAR_DO_CANNY_PRUNING'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 0}

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

OCVCascadeDetector_CV_HAAR_NO_PRUNING = 0
OCVCascadeDetector_CV_HAAR_DO_CANNY_PRUNING = 1