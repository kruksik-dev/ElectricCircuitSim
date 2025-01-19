# Minimalna wymagana wersja CMake
cmake_minimum_required(VERSION 3.10)

# Nazwa projektu
project(ElectricalSim LANGUAGES CXX)

# Ustawienie standardu C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Znajdź bibliotekę pybind11
find_package(pybind11 REQUIRED)

# Ścieżki do plików nagłówkowych
include_directories(cpp/include)

# Źródła projektu
set(SOURCES 
    cpp/src/sinusoidal_generator.cpp
    cpp/src/square_wave_generator.cpp
    cpp/src/circuit_rl.cpp
    cpp/src/pybind_module.cpp
)

# Tworzenie modułu Pythonowego
pybind11_add_module(electrical_sim ${SOURCES})

# Opcjonalne: dodaj dodatkowe flagi kompilatora
target_compile_options(electrical_sim PRIVATE -Wall -Wextra -O2)
