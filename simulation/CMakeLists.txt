# To build:
# mkdir build && cd build
# cmake .. -DCMAKE_PREFIX_PATH=$LOCAL_BUILD
# cmake --build .

cmake_minimum_required(VERSION 3.10)

# set the project name
project(Robot VERSION 3.10)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED False)

# add the executable (name first, followed by cpp files)
add_executable(
    "${PROJECT_NAME}"
    Robot.cpp
)

find_package(raisim CONFIG REQUIRED)
target_link_libraries("${PROJECT_NAME}" raisim::raisim)

# install(FILES Foo.hpp DESTINATION include)
# install(TARGETS "${PROJECT_NAME}" DESTINATION lib)
# install(FILES "${PROJECT_NAME}"Config.cmake DESTINATION lib/cmake/"${PROJECT_NAME}")

# configure file (headers)
# configure_file(
#     header.hpp
#     header.hpp.in
# )

# target_include_directories(
#     "${PROJECT_NAME}" PUBLIC
#     "${PROJECT_BINARY_DIR}"
# )

# Install commands are used when using `cmake install`
# install(TARGETS "${PROJECT_NAME}" DESTINATION bin)  # ${CMAKE_INSTALL_PREFIX}/bin

# https://stackoverflow.com/questions/20746936/what-use-is-find-package-if-you-need-to-specify-cmake-module-path-anyway
# Eigen error:
# https://github.com/opencv/opencv/issues/14868
