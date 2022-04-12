---
layout: work
type: Project
num: 11
worktitle: "Projects 10/11 B,C,D guide"
---

To complete Projects 10/11 B,C,D you will finish the compiler in
stages. At each stage, only implement parsing and code generation for
the productions sufficient for completing the given test case.  For a
complete list of grammar productions, see the table of "The Jack
grammar" in your textbook (in the 2nd edition, Figure 10.5 on page
201).

Some of these test cases are included in the nand2tetris
distribution. Others are custom test cases we provide; the titles of
custom test cases include hyperlinks to the ZIP files containing their
source code in Jack.

Project 10/11B
==============

[Three](Three.zip)
------------------

To compile [Three](Three.zip), you need to generate code for the following symbols:

- `class`
- `subroutineDec` (ignore `parameterList`)
- `subroutineBody` (functions only)
- `statements`
- `doStatement`
- `returnStatement` (may ignore return value)
- `subroutineCall` (functions only)
- `expressionList`
- `expression`
- `term` (specifically `integerConstant`)

Seven
-----

To compile Seven, you need to generate code for the following additional symbols:

- `term` (parenthesized expressions)
- `op` (specifically `+` and `*`)

Project 10/11C
==============

[AlphaWhere](AlphaWhere.zip)
----------------------------

To compile [AlphaWhere](AlphaWhere.zip), you need to generate code
for the following additional symbols:

- `varDec`
- `letStatement` (ignore arrays)
- `ifStatement`
- `term` (specifically `true`, `false`, and `varName` for locals)
- `op` (specifically `-` and `<`)

Note: You will need to create a symbol table data structure to keep
track of your local variables.

[AlphaShow](AlphaShow.zip)
--------------------------

To compile [AlphaShow](AlphaShow.zip), you need to generate code for
the following additional symbols:

- `varDec` (specifically, more than one variable of the same type on a line)
- `whileStatement`
- `term` (specifically the `~` unary operator)
- `op` (specifically `>`)

[Factorial](Factorial.zip)
--------------------------

To compile [Factorial](Factorial.zip), you need to generate code for
the following additional symbols:

- `subroutineDec` (with `paramaterList`)
- `returnStatement` (with return expression)
- `term` (specifically, `varName` for arguments and `stringConstant`)
- `op` (specifically `=`)

ConvertToBin
------------

NOTE: The provided ConvertToBin is difficult to use. We recommend
using this modified version ([Main.jack](ConvertToBin/Main.jack)),
which uses keyboard input and prints to the screen, rather than
relying on RAM hacking. Note that it prints its binary result with the
least significant bit on the left (reversed in comparison to how you
would typically write a binary number).

To compile ConvertToBin, you need to generate code for the following additional symbols:

- `varDec` (specifically multiple var declarations of different data types)
- `letStatement` (specifically modification of parameter values)
- `subroutineDec` (with `paramaterList` that has multiple parameters)
- `op` (specifically `&`)

Project 10/11D
==============

Average
-------

To compile Average, you need to generate code for the following additional symbols:

- `letStatement` (with arrays)
- `term` (specifically `varName` with array lookup)
- `op` (specifically division)

ComplexArray
------------

In theory, ComplexArray should compile if Average compiles. It is a
much tougher test case, though. Make sure that the destination of the
expression in a let statement does not have `THAT` inadvertently
overwritten.

Square
------

To compile Square, the compiler should be completely finished, except
for static variables. Pay particular attention to the following:

- `classVarDec` (fields only, although statics are not difficult to handle at the same time)
- `subroutineCall` (for methods)
    - this will need to be the first argument.
    - Be especially careful when calling a method from another method in the same class.
- `subroutineBody` (for constructors and methods)
    - Constructors will need to allocate memory for the new object.
    - For constructors, this needs to be a local variable.
    - For methods, this should be the first argument.
    - For both methods and constructors, this segment needs to be
      properly set up at the start of the body.

Pong
----

To compile Pong, the compiler should handle static class variables, unary `-`, and binary `|`.
