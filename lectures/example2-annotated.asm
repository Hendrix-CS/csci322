// x = 50
@50  // A-instruction
D=A  // C-instruction: x=D, y=A, output y
@x
M=D

// while (x > 0) { x--; }
(LOOP)
@x
MD=M-1
@LOOP
D;JGT
