
// x = 50
@50   // A-instruction: load 50 into A register.
D=A   // Take value from A register (and send it through ALU)
      // and store in D register.
@x    // assembler will automatically assign variable
      // x to memory location 16.
M=D   // Store value in D register in RAM at location
      // with address in A register.

// x = x + 4
@4
D=A
@x
M=D+M
