// sum = 0
@sum
M=0

// i = 1
@i
M=1

(LOOP)
// while (i <= 10) {
@i
D=M
@10
D=D-A
@END
D;JGT

//   if (i is odd) {
@i
D=M
@1
D=A&D   // AND value of i with 1 to keep only the last bit
@ENDIF
D;JEQ

//     sum += i
@i
D=M
@sum
M=M+D

//   }
(ENDIF)

//   i += 1
@i
M=M+1

// }
@LOOP
0;JMP

(END)

@END
0;JMP
