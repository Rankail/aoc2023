cmake_minimum_required(VERSION 3.26)
project(cpp)

set(CMAKE_CXX_STANDARD 20)

foreach(DAY RANGE 1 25)
    if(DAY LESS 10)
        add_executable("0${DAY}-Part1" "0${DAY}/p1.cpp" "utils.cpp")
        add_executable("0${DAY}-Part2" "0${DAY}/p2.cpp" "utils.cpp")
    else()
        add_executable("${DAY}-Part1" "${DAY}/p1.cpp" "utils.cpp")
        add_executable("${DAY}-Part2" "${DAY}/p2.cpp" "utils.cpp")
    endif()
endforeach()
