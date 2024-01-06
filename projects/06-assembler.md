---
layout: work
type: Project
num: 6
worktitle: Assembler
---

* **Description**: Complete [Project 6 on
      nand2tetris.org](https://www.nand2tetris.org/project06).

* **What to turn in**: Turn in all files necessary for running your
  assembler.

* **Hints**:

    - Note that the test cases for this project are **not** automated!
      You will need to manually test each of your assembled programs
      to make sure they work and are identical to those produced by
      the provided assembler.  You can run the `.hack` files produced
      by your assembler in the CPU emulator.  To test that the `.hack`
      files output by your assembler are identical to those produced
      by the nand2tetris assembler, see the end of Chapter 6 for an
      explanation of how to use the provided assembler to load both
      the original `.asm` file as well as your assembler's output
      `.hack` file and test that the results are identical.

    - You are strongly encouraged to complete your assembler in
      phases; in each phase, implement just enough to get the
      assembler to work on the next test case.  Do the test cases in
      the following order.  Start by ignoring labels entirely:

        - `Add.asm`
        - `MaxL.asm`
        - `RectL.asm`
        - `PongL.asm`
        - Finally, handle labels and get `Max.asm`, `Rect.asm`, and
          `Pong.asm` to work.

* **Specification**: To get credit for this project, you must complete
  a working assembler program and pass the provided tests (`Add.asm`,
  `Max.asm`, `Rect.asm`, `Pong.asm`): in particular, given these files
  as input, your assembler must produce identical output to that of
  the assembler provided with the nand2tetris software suite.  Note
  that your solution will not officially be tested on the `L` variants
  (`MaxL.asm`, `RectL.asm`, `PongL.asm`) although you are encouraged
  to start with those.

  To facilitate testing, your assembler must accept an assembly file
  name *as a command-line parameter* and automatically write its
  output to a new file with the same name but an extension of `.hack`
  instead of `.asm`.  If you are not sure how to do this, please ask!
