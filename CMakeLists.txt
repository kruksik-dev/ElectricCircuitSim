
cmake_minimum_required(VERSION 3.10)

project(ElectricalSim LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(pybind11 REQUIRED)

include_directories(src/include)

set(SOURCES 
    src/src/sinusoidal_generator.cpp
    src/src/square_wave_generator.cpp
    src/src/circuit_rl.cpp
    src/src/pybind_module.cpp
)

pybind11_add_module(electriccircuitsim MODULE ${SOURCES})

target_compile_definitions(electriccircuitsim
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
