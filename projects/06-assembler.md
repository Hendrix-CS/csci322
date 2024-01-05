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
      (using the provided CPU emulator) to make sure they work and are
      identical to those produced by the provided assembler.

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
