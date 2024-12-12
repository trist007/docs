
.. image:: images/asm-logo.jpg
   :width: 100

Assembly
#########

* Assembly tips

.. list-table:: MASM Data Types
   :widths: 25 25 50
   :header-rows: 1

   * - Type
     - Size
     - Description
   * - byte (db)
     - 1
     - 1-byte memory operand, unsigned (generic integer)
   * - sbyte
     - 1
     - 1-byte memory operand, unsigned (generic integer)
   * - word (dw)
     - 2
     - 2-byte memory operand, unsigned (generic integer)
   * - sword
     - 2
     - 2-byte memory operand, signed integer
   * - dword (dd)
     - 4
     - 4-byte memory operand, unsigned (generic integer)
   * - sdword
     - 4
     - 4-byte memory operand, signed integer
   * - qword (dq)
     - 8
     - 8-byte memory operand, unsigned (generic integer)
   * - sqword
     - 8
     - 8-byte memory operand, signed integer
   * - tbyte (dt)
     - 10
     - 10-byte memory operand, unsigned (generic integer or BCD)
   * - oword
     - 16
     - 16-byte memory operand, unsigned (generic integer)
   * - real4
     - 4
     - 4-byte single-precision floating-point memory operand
   * - real8
     - 8
     - 8-byte double-precision floating-point memory operand
   * - real10
     - 10
     - 10-byte extended-precision floating-point memory operand
   * - proc
     - N/A
     - Procedure label (associated with PROC directive)
   * - label:
     - N/A
     - Statement label (any identifier immediately followed by a :)
   * - constant
     - Varies
     - Constant declaration (equate) using = or EQU directive
   * - text
     - N/A
     - Textual substitution using macro or TEXTEQU directive





