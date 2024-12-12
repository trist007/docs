CMake
######

* Be sure to set a C or CXX Standard

..  code-block:: cpp
    
    set(CMAKE_CXX_STANDARD          17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
    set(CMAKE_CXX_EXTENSIONS        OFF)

CMake build options
-----------------------------------------------------

* Specify a specific compiler

.. code-block:: cpp

    cmake -DCMAKE_CXX_COMPILER=/usr/bin/clang++
    cmake -DCMAKE_C_COMPILER=/usr/bin/gcc
