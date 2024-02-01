// (LOOP)
// @KBD
// D=M
// @LOOP
// 0;JMP

// forever {
(FOREVER)

//   if (key == SPACE) {
@KBD
D=M
@32
D=A-D
@CLEAR
D;JNE

//     draw pixels at 20000
@20000
M=-1

//   }
@ENDIF
0;JMP

//   else {
(CLEAR)

//     clear pixels at 20000
@20000
M=0

//   }
(ENDIF)

// }
@FOREVER
0;JMP
