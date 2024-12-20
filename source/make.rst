
.. image:: images/make-logo.jpg
   :width: 100

make
####

* List Makefile targets

.. code-block:: cpp

   make -qp |
    awk -F':' '/^[a-zA-Z0-9][^$#\/\t=]*:([^=]|$)/ {split($1,A,/ /);for(i in A)print A[i]}' |
    sort -u
