execute_process(COMMAND "/home/yongbo/Documents/PennApps/catkin_ws/build/voice_recog/audio_common/sound_play/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/yongbo/Documents/PennApps/catkin_ws/build/voice_recog/audio_common/sound_play/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
