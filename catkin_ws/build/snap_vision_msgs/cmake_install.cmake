# Install script for directory: /home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/install")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/snap_vision_msgs/msg" TYPE FILE FILES
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/msg/DescriptorStamped.msg"
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/msg/BoundingBox.msg"
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/msg/Detection.msg"
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/msg/DetectionsStamped.msg"
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/msg/LabeledImage.msg"
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/msg/Error.msg"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/snap_vision_msgs/srv" TYPE FILE FILES
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/srv/Detector.srv"
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/srv/Models.srv"
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/srv/Stream.srv"
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/srv/Params.srv"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/snap_vision_msgs/cmake" TYPE FILE FILES "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/build/snap_vision_msgs/catkin_generated/installspace/snap_vision_msgs-msg-paths.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/devel/include/snap_vision_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/devel/share/common-lisp/ros/snap_vision_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/devel/lib/python2.7/dist-packages/snap_vision_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/devel/lib/python2.7/dist-packages/snap_vision_msgs")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/build/snap_vision_msgs/catkin_generated/installspace/snap_vision_msgs.pc")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/snap_vision_msgs/cmake" TYPE FILE FILES "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/build/snap_vision_msgs/catkin_generated/installspace/snap_vision_msgs-msg-extras.cmake")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/snap_vision_msgs/cmake" TYPE FILE FILES
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/build/snap_vision_msgs/catkin_generated/installspace/snap_vision_msgsConfig.cmake"
    "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/build/snap_vision_msgs/catkin_generated/installspace/snap_vision_msgsConfig-version.cmake"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/snap_vision_msgs" TYPE FILE FILES "/home/yongbo/Documents/PennApps_DrivingAssistant/catkin_ws/src/snap_vision_msgs/package.xml")
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

