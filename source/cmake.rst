
.. image:: images/cmake-logo.jpg
   :width: 100

CMake
######

* Be sure to set a C or CXX Standard

..  code-block:: cpp
    
    set(CMAKE_CXX_STANDARD          17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
    set(CMAKE_CXX_EXTENSIONS        OFF)
    set(CMAKE_BUILD_TYPE debug)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++20")

CMake build options
-----------------------------------------------------

* Specify a specific compiler

.. code-block:: cpp

    cmake -DCMAKE_CXX_COMPILER=/usr/bin/clang++
    cmake -DCMAKE_C_COMPILER=/usr/bin/gcc

* use Debug mode to see verbose output

.. code-block:: cpp

    cmake -DCMAKE_BUILD_TYPE=Debug ../

* conditional files
.. code-block:: cpp

    set(TRANTOR_TLS_PROVIDER "None")
    if(TRANTOR_USE_TLS STREQUAL "openssl" OR TRANTOR_USE_TLS STREQUAL "")
      find_package(OpenSSL)
      if(OpenSSL_FOUND)
        target_link_libraries(${PROJECT_NAME} PRIVATE OpenSSL::SSL OpenSSL::Crypto)
        target_compile_definitions(${PROJECT_NAME} PRIVATE USE_OPENSSL)
        set(TRANTOR_TLS_PROVIDER "OpenSSL")

        set(TRANTOR_SOURCES ${TRANTOR_SOURCES} trantor/net/inner/tlsprovider/OpenSSLProvider.cc
                            trantor/utils/crypto/openssl.cc
        )
      elseif(TRANTOR_USE_TLS STREQUAL "openssl")
        message(FATAL_ERROR "Requested OpenSSL TLS provider but OpenSSL was not found")
      endif()
    endif()
