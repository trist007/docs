
.. image:: images/c++-logo.png
   :width: 100

C++
###

* cannot do in-class data member initialization

..  code-block:: cpp

    SQLite::Database db{"../darkterminal.db", SQLite::OPEN_READWRITE | SQLite::OPEN_CREATE};

.. list-table:: C++ and Assembly Language Types
   :widths: 25 25 25
   :header-rows: 1

   * - C++ Type
     - Size (in bytes)
     - Assembly language type
   * - char
     - 1
     - sbyte
   * - signed char
     - 1
     - sbyte
   * - unsigned char
     - 1
     - byte
   * - short int
     - 2
     - sword
   * - short unsigned
     - 2
     - word
   * - int
     - 4
     - sdword
   * - long int
     - 4
     - sdword
   * - long unsigned
     - 4
     - dword
   * - long int
     - 8
     - sqword
   * - long unsigned
     - 8
     - qword
   * - __int64
     - 8
     - sqword
   * - unsigned __int64
     - 8
     - qword
   * - Float
     - 4
     - real4
   * - double
     - 8
     - real8
   * - pointer for example, void *
     - 8
     - qword

