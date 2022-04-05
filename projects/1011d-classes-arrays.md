---
layout: work
type: Project
num: 10/11C
worktitle: "Compiler IV: Classes and Arrays"
due: Monday, April 18
---

* **Description**: Write a complete, working compiler which passes the
  tests `Average`, `ComplexArray`, `Square`, and `Pong`.  See the
  [project 11 guide](11-guide.html) for details.

* **Due**: {{page.due}} @5pm.

* **What to turn in**: Turn in all files necessary for running your
  compiler (including the tokenizer, etc).  Your compiler can be
  written in any language you wish.

* **Specification**: To get credit for this project, you must
  - Complete a working compiler which accepts the name of a `.jack` file as a
    command-line argument and outputs a corresponding `.vm` file with
    the same base name. (For example, `foo.jack` should become
    `foo.vm`.)
  - Your compiler *must also* accept the name of a directory, in which
    case it should compile each `.vm` file found within the directory.
  - For each of the following tests, your compiler must
    output a `.vm` file which *behaves* identically to the one produced
    by the `JackCompiler` provided with your book.  Note that unlike
    some previous projects, you do *not* have to produce a `.vm` file
    which is literally identical to the one produced by the book's
    compiler.

      - [Average](11-guide.html#Average)
      - [ComplexArray](11-guide.html#ComplexArray)
      - [Square](11-guide.html#Square)
      - [Pong](11-guide.html#Pong)
