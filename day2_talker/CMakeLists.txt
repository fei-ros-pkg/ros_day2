cmake_minimum_required(VERSION 2.8.3)
project(day2_talker)
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs)

catkin_python_setup()

catkin_package(CATKIN_DEPENDS roscpp rospy std_msgs)

include_directories(${catkin_INCLUDE_DIRS})
add_executable(talker_node src/talker_node.cpp)
target_link_libraries(talker_node ${catkin_LIBRARIES})

install(TARGETS talker_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(PROGRAMS
  scripts/talker_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

