cmake_minimum_required(VERSION 3.12)
project(cabac)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(cabac
        CABACTables.cpp
        ContextModel.cpp
        encoderCABAC.cpp
        main.cpp)

add_executable(ac_en
        ac_en.cpp
        )

add_executable(ac_de
        ac_de.cpp
        )