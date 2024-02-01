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

//   sum += i
@i
D=M
@sum
M=M+D

//   i += 1
@i
M=M+1

// }
@LOOP
0;JMP

(END)

@END
0;JMP