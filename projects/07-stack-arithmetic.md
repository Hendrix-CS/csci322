---
layout: work
type: Project
num: 7
worktitle: "VM I: Stack Arithmetic"
---

* **Description**: Complete [Project 7 on
      nand2tetris.org](https://www.nand2tetris.org/project07).

* **What to turn in**: Turn in all files necessary for running your
  VM-to-Hack translator.

* **Specification**: To get credit for this project, you must complete
  a working VM-to-Hack translator and pass the provided tests
  (`SimpleAdd.tst`, `StackTest.tst`, `BasicTest.tst`,
  `PointerTest.tst`, `StaticTest.tst`).
* **SUGGESTED STRATEGY**
  * Output each VM source instruction as a comment in the assembly code.
    * This makes debugging much easier, as it gives some structure and
      organization to the generated assembly.
  * Start by setting the stack pointer to the start of the stack.
  * Implement `push constant`
  * Implement `add`
  * Pass `SimpleAdd`
  * Implement `sub`, `push static`, and `pop static` 
  * Pass `StaticTest`
  * Implement `eq`, `lt`, `gt`, `and`, `or`, `not`, and `neg`
  * Pass `StackTest`
  * Implement the remaining segments
  * Pass `BasicTest`
  * Pass `PointerTest`
