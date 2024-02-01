// (LOOP)
// @KBD
// D=M
// @LOOP
// 0;JMP

// forever {
(FOREVER)

//     draw pixels at 20000 + KBD
@KBD
D=M
@20000
A=D+A
M=-1

// }
@FOREVER
0;JMP
