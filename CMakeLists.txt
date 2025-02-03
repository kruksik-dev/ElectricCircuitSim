cmake_minimum_required(VERSION 3.15)

project(ElectricalSim LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(PYBIND11_FINDPYTHON ON)

# Znalezienie Pythona i pybind11
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

# Pliki źródłowe
set(SOURCES 
    src/cpp/src/sinusoidal_generator.cpp
    src/cpp/src/square_wave_generator.cpp
    src/cpp/src/circuit_rl.cpp
)

# Utworzenie biblioteki statycznej
add_library(electric STATIC ${SOURCES})
set_target_properties(electric PROPERTIES POSITION_INDEPENDENT_CODE ON)

# Tworzenie modułu Pythona
pybind11_add_module(_electric_sim MODULE src/cpp/src/pybind_module.cpp WITH_SOABI)
target_link_libraries(_electric_sim PRIVATE pybind11::headers)
target_link_libraries(_electric_sim PRIVATE electric)

# Opcjonalnie: Definicje kompilacji, jeśli potrzebne
target_compile_definitions(_electric_sim PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
install(TARGETS _electric_sim DESTINATION circuit_simulator/core)

option(ENABLE_TESTING "Enable testing" OFF)
if(ENABLE_TESTING)
    message(STATUS "🔹 Testy włączone! Konfiguruję GTest...")

    find_package(GTest REQUIRED)

    enable_testing()

    set(TEST_SOURCES tests/test_electric_sim.cpp)

    add_executable(test_electric_sim ${TEST_SOURCES})
    target_link_libraries(test_electric_sim PRIVATE electric GTest::gtest_main)

    include(GoogleTest)
    gtest_discover_tests(test_electric_sim)
else()
    message(STATUS "⚠️ Testy wyłączone - pomijam konfigurację GTest.")
endif()
