
.. image:: images/make-logo.jpg
   :width: 100

make
####

* The first target is always the default target
* List Makefile targets the easy way

.. code-block:: cpp

   make help

* List Makefile targets the hard way

.. code-block:: cpp

   make -qp |
    awk -F':' '/^[a-zA-Z0-9][^$#\/\t=]*:([^=]|$)/ {split($1,A,/ /);for(i in A)print A[i]}' |
    sort -u

* example Makefile (be sure to use tabs intead of spaces :set noexpandtab)

.. code-block:: cpp

   snazzle.tab.c snazzle.tab.h: snazzle.y
        bison -d snazzle.y

   lex.yy.c: snazzle.l snazzle.tab.h
        flex snazzle.l

   snazzle: lex.yy.c snazzle.tab.c snazzle.tab.h
        g++ snazzle.tab.c lex.yy.c -o snazzle

   clean:
        rm -rf snazzle snazzle.tab.c lex.yy.c

