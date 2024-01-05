---
layout: work
type: Project
num: 8
worktitle: "VM II: Program Control"
---

* **Description**: Complete [Project 8 on
      nand2tetris.org](https://www.nand2tetris.org/project08) by
      extending your VM-to-Hack translator from [Project
      7](07-stack-arithmetic.html).

* **What to turn in**: Turn in all files necessary for running your
  VM-to-Hack translator.

* **Specification**: To get credit for this project, you must complete
  a working VM-to-Hack translator and pass the last three tests
  (`NestedCall.tst`, `FibonacciElement.tst`, `StaticsTest.tst`).

    - **NOTE** that the first three tests (`BasicLoop.tst`,
      `FibonacciSeries.tst`, and `SimpleFunction.tst`) will no longer
      work once you change your translator to generate bootstrap
      code.  This is OK.  Just make sure you pass all three tests
      before adding the bootstrap code, then afterwards focus on
      getting the final three tests to work.

      `NestedCall.tst` will work with or without bootstrap code.  The
      last two (`FibonacciElement.tst` and `StaticsTest.tst`) will
      only work with bootstrap code.
