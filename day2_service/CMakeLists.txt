cmake_minimum_required(VERSION 2.8.3)
project(day2_service)
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs message_generation)

catkin_python_setup()

add_service_files(
  FILES
  AddTwoInts.srv
)
generate_messages(DEPENDENCIES std_msgs)
catkin_package(CATKIN_DEPENDS roscpp rospy std_msgs message_runtime)

include_directories(include ${catkin_INCLUDE_DIRS})
add_executable(service_node src/service_node.cpp)
add_dependencies(service_node day2_service_generate_messages_cpp)
target_link_libraries(service_node ${catkin_LIBRARIES})

install(TARGETS service_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
)

install(PROGRAMS
  scripts/service_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

