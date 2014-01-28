cmake_minimum_required(VERSION 2.8.3)
project(day2_client)
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs day2_service)

catkin_python_setup()

catkin_package(CATKIN_DEPENDS roscpp rospy std_msgs day2_service)

include_directories(${catkin_INCLUDE_DIRS})

add_executable(client_node src/client_node.cpp)

target_link_libraries(client_node ${catkin_LIBRARIES})

install(TARGETS client_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(PROGRAMS
  scripts/client_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

