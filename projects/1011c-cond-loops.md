---
layout: work
type: Project
num: 10/11C
worktitle: "Compiler III: Conditionals and Loops"
due: Monday, April 11
---

* **Description**: Write a compiler which passes the tests
  `AlphaWhere`, `AlphaShow`, `Factorial`, and `ConvertToBin`.  See the
  [project 11 guide](11-guide.html) for details.

* **Due**: {{page.due}} @5pm.

* **What to turn in**: Turn in all files necessary for running your
  compiler (including the tokenizer, etc).  Your compiler can be
  written in any language you wish.

* **Specification**: To get credit for this project, you must complete
  a working compiler which accepts the name of a `.jack` file as a
  command-line argument and outputs a corresponding `.vm` file with
  the same base name. (For example, `foo.jack` should become
  `foo.vm`.)  For each of the following tests, your compiler must
  output a `.vm` file which *behaves* identically to the one produced
  by the `JackCompiler` provided with your book.  Note that unlike
  some previous projects, you do *not* have to produce a `.vm` file
  which is literally identical to the one produced by the book's
  compiler.

    - [AlphaWhere](11-guide.html#AlphaWhere)
    - [AlphaShow](11-guide.html#AlphaShow)
    - [Factorial](11-guide.html#Factorial)
    - [ConvertToBin](11-guide.html#ConvertToBin)
