---
layout: work
type: Project
num: 2
worktitle: Boolean arithmetic
due: Wednesday, 26 January
---

* **Description**:
    - Complete [Project 2 on
      nand2tetris.org](https://www.nand2tetris.org/project02).
    - Additionally, implement an `Or16Way` chip, using the files
      linked below (you can download them and place them in the same
      folder as the other project 2 files).  You may find this chip
      helpful in completing the rest of the project.
        - [`Or16Way.hdl`](../static/Or16Way.hdl)
        - [`Or16Way.cmp`](../static/Or16Way.cmp)
        - [`Or16Way.tst`](../static/Or16Way.tst)
    - In particular, I suggest you first complete `HalfAdder`,
      `FullAdder`, `Add16`, `Inc16`, and `ALU-nostat`
      (`ALU-nostat.tst` is just a test file for `ALU.hdl` which
      ignores the `zr` and `ng` output bits); then implement
      `Or16Way`, and finally finish the `zr` and `ng` output bits for
      `ALU` and test with `ALU.tst`.

* **What to turn in**: Turn in all your `.hdl` files, one for each
  chip, including `Or16Way.hdl`.  There should be 6 in all
  (`HalfAdder`, `FullAdder`, `Add16`, `Inc16`, `Or16Way`, `ALU`).

* **Specification**: To get credit for this project, you must complete
  all 6 chips and pass the tests for each.

* **Due**: {{page.due}} @5pm.
