// x = 50
@50  // A-instruction
D=A  // C-instruction: x=D, y=A, output y
@x
M=D

// x = x + 4
@4
D=A
@x
M=D+M

// Only things that can go on the right of the = are operations
// the ALU can do.  e.g.  we can't say D=D+4.
