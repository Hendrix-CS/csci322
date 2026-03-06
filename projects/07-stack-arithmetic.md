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
  * Begin by implementing `push constant`
  * Next, implement `add`
  * Pass `SimpleAdd`
  * Next, implement `sub`, `push static` and `pop static` 
  * Pass `StaticTest`
  * Now implement the remaining segments
  * Pass `BasicTest`
  * Pass `PointerTest`
* **NOTE**
  * None of the Chapter 7 tests employ `neg`, `not`, `and`, `or`, `eq`, `gt`, and `lt`.
  * It is fine to put those off until Chapter 8.  
