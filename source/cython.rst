
.. image:: images/python-logo.jpg
   :width: 100

Cython
######

* Cython - run C functions in python

printf.pyx

.. code-block:: cpp

   cdef extern from "stdio.h":
        int printf(const char* message, ...)

    def print_hello():
        printf("Hello from Cython!\n")

.. code-block:: cpp
    
   python3 setup.py build_ext --inplace

printf.py

.. code-block:: cpp

   import printf

   printf.print_hello()   

Run it

.. code-block: cpp
   
   python3 printfpy

