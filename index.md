---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: course-single
---

# <a name="description">Overview</a>

{{ site.description }}

## <a name="goals">Learning Goals</a>

Upon completing this course, you will be able to:

* Describe the hierarchy of abstractions that define a modern computer
  (logic gates, CPU, machine language, assembly, virtual machines,
  high-level languages, operating system).
* Understand and apply basic boolean logical operators.
* Create a digital circuit corresponding to a specification given in boolean logic.
* Create a digital circuit employing clocked memory components.
* Describe how boolean logic, memory circuits, and a clock pulse interact to execute a machine language instruction.
* Write assembly language programs that behave according to a given specification.
* Write programs to translate between levels of abstraction
  (e.g. high-level language to VM, VM to assembly, assembly to machine code).
* Describe how operating systems enable programmers to access a computer's hardware.

## <a name="resources">Resources</a>

{% include resources.html content=site.resources %}

### Troubleshooting

- If you get an error like "Permission denied" when attempting to run
  one of the nand2tetris tools on OSX or Linux, you may need to make
  the `.sh` files executable, by running

      cd nand2tetris/tools
      chmod +x *.sh

  at a terminal prompt.

- If you get an error like "cannot find javaw", you need to install
  Java.  [Visit this page to download and run the appropriate
  installer](https://java.com/en/download/manual.jsp).

<hr />

# <a name="calendar">Calendar</a>


<!-- BEGIN CALENDAR -->

| Date          | Topic                              | Reading    | Deadlines                       |
| --------------|------------------------------------|------------|------------------------------------------------------------|
| **W 21 Jan**  | Boolean Logic Circuits             | Chapter 1  |      
| **F 23 Jan**  | Hardware Description Language      | Appendix A |
|
| **M 26 Jan**  | Boolean Arithmetic                 | Chapter 2  | [Project 1: Boolean logic](projects/01-boolean-logic.html) |
| **W 28 Jan**  | Boolean Arithmetic
| **F 30 Jan**  | Sequential Logic & Memory          | Chapter 3  | [Project 2: Boolean arithmetic](projects/02-boolean-arithmetic.html) 
|
| **M 2 Feb**   | Sequential Logic & Memory          |            |
| **W 4 Feb**   | Machine & Assembly Language        | Chapter 4  | [Project 3: Memory](projects/03-memory.html)
| **F 6 Feb**   | Hack Assembly Examples             |            | Formative Assessment 1
|
| **M 9 Feb**   | Turing Machine CPU                 | Chapter 5  |
| **W 11 Feb**  | More Turing Machine CPU            |            | [Project 4: Machine language](projects/04-machine-language.html)
| **F 13 Feb**  | CPU History                        |            | Formative Assessment 2
|
| **M 16 Feb**  | **NO CLASS: Midwinter Break**
| **W 18 Feb**  | **NO CLASS: Away at conference**
| **F 20 Feb**  | **NO CLASS: Away at conference**   |            | 
|
| **M 23 Feb**  | Assemblers                         | Chapter 6  | [Project 5: Computer architecture](projects/05-computer-architecture.html)
| **W 25 Feb**  | Assemblers
| **F 27 Feb**  | 6502 Architecture
|
| **M 2 March** | Virtual Machines & Stacks          | Chapter 7  | [Project 6: Assembler](projects/06-assembler.html)
| **W 4 March** | VM to Hack Translation
| **F 6 March** | VM to Hack Translation             |            | Formative Assessment 3
|
| **M 9 March** | VM Branching                       | Chapter 8  | [Project 7: VM I: Stack Arithmetic](projects/07-stack-arithmetic.html) 
| **W 11 March**| VM Function Activation Records
| **F 13 March**| Introduction to Jack               | Chapter 9  |
|
| **M 16 March**| **NO CLASS: Off-campus appointment** |          | [Project 8: VM II: Program control](projects/08-program-control.html)
| **W 18 March**| Jack Example: Monotris
| **F 20 March**| Jack work day                      |            | [Project 9: High-level programming](projects/09-high-level.html)
|
| **M 23 March**| **NO CLASS: Spring Break**
| **W 25 March**| **NO CLASS: Spring Break**
| **F 27 March**| **NO CLASS: Spring Break**
|
| **M 30 March**| Tokenizing input                   | Chapter 10
| **W 1 April** | Simple LISP Compiler               |            | Formative Assessment 4
| **F 3 April** | Compiling Jack to VM               | Chapter 11 | [Project 10/11A: Tokenizer](projects/10a-tokenizer.html)
|
| **M 6 April** | Compiling Symbol Tables            |            |
| **W 8 April** | Compiling Conditionals/Loops       |            | [Project 10/11B: Statements](projects/1011b-statements.html)
| **F 10 April**| **NO CLASS: Away at conference**   |            | 
|
| **M 13 April**| Compiling Arrays                   
| **W 15 April**| Compiling Classes/Objects          |            | [Project 10/11C: Conditionals and Loops](projects/1011c-cond-loops.html)
| **F 17 April**| Compiling Classes/Objects
|
| **M 20 April**| OS: Start, Stop, Keyboard, Arrays  | Chapter 12 | [Project 10/11D: Classes and Arrays](projects/1011d-classes-arrays.html)
| **W 22 April**| OS: Strings, Advanced Arithmetic   
| **F 24 April**| OS: Heap                           |            | Formative Assessment 5          
|
| **M 27 April**| OS: Graphics                       |            | [Project 12A: Operating System II](projects/12-OS.html)
| **W 29 April**| OS: Output                       
| **F 1 May**   | Retrospective
|
| *M 4 May*     | *(Reading Day)*                    |            | [Project 12B: Operating System II](projects/12-OS.html)
|               |
| **F 8 May**   | Final Exam Period (8:30-11:30 am)  |            | Formative Assessment: Final

<!--
| Date          | Topic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Reading & Links                                                                                      | Due dates (recommended A schedule)                                         |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **T 16 Jan**  | *No class (snow)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                      |                                                                            |
| **Th 18 Jan** | Boolean logic [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F1%5F18%5F%20intro%2C%20boolean%20logic%2D20240118%5F094810%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](/lectures/2024-01-18-boolean-logic.pdf)                                                                                              | Chapters 1 and 2                                                                                     | [Grading contract and work plan](#grading-contracts) due                   |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Appendix A                                                                                           | [CSCI student info survey](https://forms.gle/VLRVHjUAisWP5R9J8)            |
| *F 19 Jan*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 1: Boolean logic](projects/01-boolean-logic.html)                 |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| **T 23 Jan**  | Boolean arithmetic (no class meeting) [![youtube](icons/youtube.png)](https://youtu.be/5Vv5afGWCdo) [![youtube](icons/youtube.png)](https://www.youtube.com/watch?v=tSLpUCtt8ms)                                                                                                                                                                                                                                                                                                                                             | Chapter 3                                                                                            |                                                                            |
| *W 24 Jan*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 2: Boolean arithmetic](projects/02-boolean-arithmetic.html)       |
| **Th 25 Jan** | Sequential logic & memory [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F1%5F25%5F%20memory%2D20240125%5F094618%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-01-25-memory.pdf)                                                                                                              | Chapter 3                                                                                            |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 29 Jan*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 3: Memory](projects/03-memory.html)                               |
| **T 30 Jan**  | Machine & assembly language [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F1%5F30%5F%20machine%20%2B%20assembly%20language%2D20240130%5F094641%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-01-30-machine-and-assembly.pdf)                                                                 | Chapter 4                                                                                            |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [example.asm](lectures/example.asm)                                                                  |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [example2.asm](lectures/example2.asm)                                                                |                                                                            |
| **Th 1 Feb**  | Hack assembly examples [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F2%5F1%5F%20Assembly%20examples%2D20240201%5F094609%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-02-01-screen-kbd.pdf)                                                                                                 | [screen.asm](lectures/screen.asm)                                                                    |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [kbd.asm](lectures/kbd.asm)                                                                          |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [kbd2.asm](lectures/kbd2.asm)                                                                        |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [sum.asm](lectures/sum.asm)                                                                          |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [sum2.asm](lectures/sum2.asm)                                                                        |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 5 Feb*     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 4: Machine language](projects/04-machine-language.html)           |
| **T 6 Feb**   | Turing machine CPU [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F2%5F6%5F%20Turing%20machine%20CPU%2D20240206%5F094709%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-02-06-Turing-CPU.pdf)                                                                                                  | Chapter 5                                                                                            |                                                                            |
| **Th 8 Feb**  | More Turing machine CPU; CPU history [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F2%5F8%5F%20TM%20%2B%20Hack%20CPU%2C%20CPU%20history%2D20240208%5F094916%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-02-06-Turing-CPU.pdf) [![pdf](icons/pdf.png)](lectures/2024-02-08-CPU-history.pdf) |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 12 Feb*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 5: Computer architecture](projects/05-computer-architecture.html) |
| **T 13 Feb**  | Assembler [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F2%5F13%5F%20Assembler%2D20240213%5F094536%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-02-13-assembler.pdf)                                                                                                                        | Chapter 6                                                                                            |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Assembler.py](lectures/assembler/Assembler.py)                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [example.tm](lectures/assembler/example.tm)                                                          |                                                                            |
| **Th 15 Feb** | 6502 chip [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F2%5F15%5F%20MOS%206502%20chip%2D20240215%5F094741%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-02-15-MOS-6502.pdf)                                                                                                                 |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 19 Feb*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 6: Assembler](projects/06-assembler.html)                         |
| **T 20 Feb**  | Virtual machines + stacks [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F2%5F20%5F%20VM%20arithmetic%2D20240220%5F094536%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-02-20-VM-stack.pdf)                                                                                                   | Chapter 7                                                                                            |                                                                            |
| **Th 22 Feb** | VM to Hack translation [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F2%5F22%5F%20VM%20translation%20I%2D20240222%5F094559%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-02-22-VM.pdf)                                                                                                       | Chapter 8                                                                                            | Grading contract evaluation I due                                          |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 26 Feb*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 7: VM I: Stack Arithmetic](projects/07-stack-arithmetic.html)     |
| **T 27 Feb**  | VM branching & function instructions [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F2%5F27%5F%20VM%20translation%5F%20branching%20%2B%20functions%2D20240227%5F094744%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-02-27-VM-functions.pdf)                                                  | Chapter 8                                                                                            |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [VMfiles.py](lectures/VMfiles.py)                                                                    |                                                                            |
| **Th 29 Feb** | Project work day / open office hours                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 4 Mar*     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 8: VM II: Program control](projects/08-program-control.html)      |
| **T 5 Mar**   | *No class (Dr. Yorgey sick)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                      |                                                                            |
| **Th 7 Mar**  | *No class (Dr. Yorgey sick)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 11 Mar*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 9: High-level programming](projects/09-high-level.html)           |
| **T 12 Mar**  | Introduction to Jack [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F3%5F12%5F%20Introduction%20to%20Jack%2D20240312%5F094625%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-03-12-Jack-intro.pdf)                                                                                             | Chapter 9                                                                                            |                                                                            |
| **Th 14 Mar** | Jack example: Monotris [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F3%5F14%5F%20Jack%20example%5F%20monotris%2D20240314%5F094529%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview)                                                                                                                                                   |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| **T 19 Mar**  | *No class (spring break)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                      |                                                                            |
| **Th 21 Mar** | *No class (spring break)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| **T 26 Mar**  | Tokenizing input [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F3%5F26%5F%20tokenizing%2D20240326%5F094543%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-03-26-tokenizing.pdf)                                                                                                               | Chapter 10                                                                                           |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/Tokenizer.py](lectures/compiler24/Tokenizer.py)                                          |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/Main.py](lectures/compiler24/Main.py)                                                    |                                                                            |
| **Th 28 Mar** | Tokenizer; a simple LISP compiler [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F3%5F28%5F%20more%20tokenizing%2D20240328%5F094552%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview)                                                                                                                                                   | [compiler24/Tokenizer.py](lectures/compiler24/Tokenizer.py)                                          |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/LISPCompiler.py](lectures/compiler24/LISPCompiler.py)                                    |                                                                            |
| *F 29 Mar*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 10/11A: Tokenizer](projects/10a-tokenizer.html)                   |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| **T 2 Apr**   | Compiling Jack to VM [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F4%5F1%5F%20Compilation%2D20240402%5F094516%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopiedShareExpControl%2Eview)                                                                                                                                                        | [compiler24/lisp.txt](lectures/compiler24/lisp.txt)                                                  |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/LISPCompiler.py](lectures/compiler24/LISPCompiler.py)                                    |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/VMWriter.py](lectures/compiler24/VMWriter.py)                                            |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/jack.txt](lectures/compiler24/jack.txt)                                                  |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/jack\_compiler.txt](lectures/compiler24/jack_compiler.txt)                               |                                                                            |
| *W 3 Apr*     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 10/11B: Statements](projects/1011b-statements.html)               |
| **Th 4 Apr**  | Compiling: symbol tables, conditionals, and loops [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F4%5F4%5F%20symbol%20tables%2C%20expressions%2C%20if%2Bwhile%2D20240404%5F094544%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopiedShareExpControl%2Eview)                                                                                      | [compiler24/jack.txt](lectures/compiler24/jack.txt)                                                  | Grading contract evaluation II due                                         |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/jack\_compiler.txt](lectures/compiler24/jack_compiler.txt)                               |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/AlphaWhere.jack](lectures/compiler24/AlphaWhere.jack)                                    |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Chapter 11                                                                                           |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [GO TO statement considered harmful](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf) |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 8 Apr*     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 10/11C: Conditionals and Loops](projects/1011c-cond-loops.html)   |
| **T 9 Apr**   | Compiling arrays [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F4%5F9%5F%20compiling%20arrays%2D20240409%5F094545%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopiedShareExpControl%2Eview)                                                                                                                                                     | [compiler24/Average.jack](lectures/compiler24/Average.jack)                                          |                                                                            |
| **Th 11 Apr** | Compiling classes [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F4%5F11%5F%20compiling%20classes%2D20240411%5F094604%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview)                                                                                                                                                                 | [compiler24/Square/Main.jack](lectures/compiler24/Square/Main.jack)                                  |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/Square/SquareGame.jack](lectures/compiler24/Square/SquareGame.jack)                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/Square/Square.jack](lectures/compiler24/Square/Square.jack)                              |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [compiler24/Pong/PongGame.jack](lectures/compiler24/Pong/PongGame.jack)                              |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 15 Apr*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 10/11D: Classes and Arrays](projects/1011d-classes-arrays.html)   |
| **T 16 Apr**  | Operating system I [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F4%5F16%5F%20OS%20I%20%28Sys%2C%20Array%2C%20String%2C%20Keyboard%2C%20Math%29%2D20240416%5F094513%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-04-16-OS-I.pdf)                                                            | Chapter 12                                                                                           |                                                                            |
| **Th 18 Apr** | Operating system II [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F4%5F18%5F%20OS%20II%20%28Screen%2C%20Output%2C%20Memory%29%2D20240418%5F094513%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](lectures/2024-04-18-OS-II.pdf)                                                                             |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 22 Apr*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 12A: Operating System I](projects/12-OS.html)                     |
| **T 23 Apr**  | Memory allocation and randomness [![stream](icons/stream.png)](https://hendrix.sharepoint.com/sites/Section_29479/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5F29479%2FShared%20Documents%2FGeneral%2FRecordings%2F4%5F23%5F%20OS%20II%2C%20randomness%2D20240423%5F094716%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview) [![pdf](icons/pdf.png)](2024-04-23-randomness.pdf)                                                                                           |                                                                                                      |                                                                            |
|               | Course evaluations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                      |                                                                            |
| **Th 25 Apr** | Project work day                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                      |                                                                            |
| *F 26 Apr*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 12B: Operating System II](projects/12-OS.html)                    |
-->

<!-- END CALENDAR -->

<hr />
# <a name="grading">Grading</a>

## Project credits

* Each project is assigned Level 1 or Level 2 completion when submitted.
  * A Level 2 submission is fully complete, passing **all** assigned tests.
  * A Level 1 project is sincerely attempted, passing at least **half** of the assigned tests.
  * Each submission earns from 1 to 3 project credits
    * One credit for each level achieved.
    * One additional credit for submitting on or before the deadline.
* A project receiving Level 1 credit may be revised and resubmitted **once** in order to
  be promoted to Level 2 credit.
* As there are 15 projects, when accounting for the on-time credits
  there are 45 total project credits available.

## Formative Assessments

* After completing groups of projects at Level 2, a student is expected to 
  undertake a **formative assessment** by visiting the instructor's office 
  hours for a demonstration of understanding.  
* A Level 1 assessment demonstrates some understanding of the topic but 
  with significant gaps.
* A Level 2 assessment demonstrates full expected understanding of the topic.
* Each assessment earns from 1 to 3 project credits
  * One credit for each level achieved.
  * One additional credit for assessing on or before the deadline.
* If a student receives a Level 1 assessment, they are welcome to schedule a second
  formative assessment to attempt to achieve Level 2 based on feedback from the
  assessment.
* There are six assessments, yielding a total of 18 available assessment credits.

| Assessment | Project Group         | Deadline       |
| ----------:|-----------------------|----------------|
| 1          | Projects 1, 2         | **F 6 Feb**    | 
| 2          | Projects 3, 4         | **F 13 Feb**   |
| 3          | Projects 5, 6         | **F 6 March**  |
| 4          | Projects 7, 8         | **W 1 April**  |
| 5          | Projects 9, 10/11 A-D | **F 24 April** |
| Final      | Projects 12A-B        | **F 8 May**    |

## Course Grade

To earn any grade of C or higher:
* Complete the [CSCI student information survey](https://forms.gle/VLRVHjUAisWP5R9J8).

Credit thresholds
* To earn an A in the course:
  * At least 42 Project Credits
    * All 15 projects Level 2
  * At least 17 Assessment Credits
* To earn a B in the course:
  * At least 33 Project Credits
    * At least 12 projects Level 2
  * At least 14 Assessment Credits
* To earn a C in the course:
  * At least 24 Project Credits
    * At least 9 projects Level 2
  * At least 11 Assessment Credits
* To earn a D in the course:
  * At least 15 Project Credits
  * At least 8 Assessment Credits
  
<hr>
# Coursework and policies

## <a name="projects">Projects</a>

Your work in this course will consist of a series of challenging
projects from our textbook.  Taken all together, they will result in a
complete, working (simulated) computer.

<!--Below you will find a list of all the projects in one place, as well
as suggested deadlines and subsets of projects depending on your
desired grade.-->

The average completion time shown for each project is based on
self-reported time spent by students in Spring 2022.  However, keep in
mind that actual reported times varied widely.  There was not enough
data to compute a meaningful average for project 12B, but it is
probably similar to 12A.

<div style="text-align: center">
<a class="btn btn-primary" href="{{ site.submission }}">
  Assignment submission form
</a>
</div>
<br/>

| #      | Topic                                                          | Avg time (hrs) | 
|:------:|----------------------------------------------------------------|:--------------:|
| 1      | [Boolean logic](projects/01-boolean-logic.html)                | 5              | 
| 2      | [Boolean arithmetic](projects/02-boolean-arithmetic.html)      | 5              | 
| 3      | [Memory](projects/03-memory.html)                              | 5              | 
| 4      | [Machine language](projects/04-machine-language.html)          | 6              | 
| 5      | [Computer archtecture](projects/05-computer-architecture.html) | 7              | 
| 6      | [Assembler](projects/06-assembler.html)                        | 8              | 
| 7      | [VM I: stack arithmetic](projects/07-stack-arithmetic.html)    | 8              | 
| 8      | [VM II: program control](projects/08-program-control.html)     | 8              | 
| 9      | [High-level programming](projects/09-high-level.html)          | 7              | 
| 10/11A | [Tokenizer](projects/10a-tokenizer.html)                       | 5              | 
| 10/11B | [Statements](projects/1011b-statements.html)                   | 7              | 
| 10/11C | [Conditionals and loops](projects/1011c-cond-loops.html)       | 8              | 
| 10/11D | [Classes and arrays](projects/1011d-classes-arrays.html)       | 8              | 
| 12A    | [Operating system I](projects/12-OS.html)                      | 6              | 
| 12B    | [Operating system II](projects/12-OS.html)                     | ?              | 

<!--
Keep in mind that the deadlines in the above table are only
suggestions!  You can and should customize to your heart's content.
For example:

- If you are aiming for a B or C, you are free to choose any subset of
  12 or 9 projects.  For example, if you are aiming for a C, perhaps
  the idea of an assembler is particularly interesting to you, so you
  would rather do Project 6 and leave out another project.
- By default, all deadlines are at 5pm, but you should pick a time
  that works well for you.  Do you like staying up late to work on
  projects?  Do you like getting things turned in by 2pm and then
  playing video games?  You decide.
- The suggested due dates just demonstrate one possible way of
  spreading work out over the whole semester.  You can and should
  customize these.  Maybe you will be doing a play or Model UN and
  want to make sure you have no deadlines during a certain period;
  maybe you want to get everything turned in by April 15th so you can
  spend the last few weeks of the semester focusing on your other
  classes; maybe you want every project due on a Tuesday; maybe you
  want to have the projects due all at once at 3:29am on Sunday,
  April 28th.  You decide!
- Keep in mind that the recommended schedule has each project due
  *after* the relevant material has been covered in class.  (However,
  your textbook has all the necessary information to complete the
  projects, so it is possible to complete projects earlier.)

## <a name="deadlines">Deadlines, extensions, and resubmissions</a>

- Every project is due at a specific date and time chosen by you in
  your grading contract.

- Assignments may be turned in any time up to your chosen deadline.  I
  will try my best to return graded assignments, with feedback, within
  *two weekdays* of being turned in.

- If you wish an **extension** on any deadline, simply send me an
  **email** (**not** a Teams message) prior to the deadline requesting
  a new deadline.  You must be specific about the date and time of the
  new deadline.  For example, you could say "I need a little extra
  time on project 5.  I will have it turned in by 8pm on Wednesday,"
  whereas it would not be acceptable to say "I need a couple extra
  days on project 5".  Such extension requests will be automatically
  granted.

- If you need a second extension, or if you miss a deadline, you
  **must meet with me** in order to discuss your situation and make a
  plan going forward.  You will not receive feedback or credit on any
  projects submitted late until you have met with me.

- If you do not get credit for a project, you may revise and resubmit
  the project (as many times as necessary to get credit).  The default
  deadline for resubmission is **one week after receiving feedback**
  (but you may ask for an extension as usual).

- The absolute latest any project may be turned in is **5pm on Wednesday,
  May 1.**
-->

### <a name="integrity">Academic integrity</a>

**Projects must be completed individually**.  Your experience of
learning how a computer works depends directly on your independent
completion of these projects.

* You **may** discuss the projects with other students at a high
  level.

* You **may** help each other debug your projects. However, be careful
  not to slide from "debugging help" into more substantive help.  "I
  don't know how to write this function" is very different than "I
  wrote this function but it doesn't work correctly".  In the former
  case you should come see me in office hours.

* You **may not**:

    - **Use generative AI coding tools** such as ChatGPT, Claude, or 
      GitHub copilot. Be sure to disable any such tools that may be 
      bundled with your IDE or editor.
    
    - **Read** any solution to any project, whether from another
      student, found online, or from any other source.

    - **Show** your solution to any other student.

Since completion of the projects is the fundamental learning
opportunity in this class, issues of academic integrity will be taken
very seriously.  Typically, plagiarism on a project will carry a
recommended sanction of failure in the course.

<hr />

# Expectations and accommodations

## <a name="expectations">Expectations</a>

Although you and I play different roles in the course, we both have
your learning as a common goal. There are things I expect from you as
a student in the course, but there are also things you can expect of
me as the course instructor and facilitator.

If I am not fulfilling my responsibilities outlined below, you are
welcome (and encouraged!) to call me out, perhaps via the [anonymous
feedback form](https://forms.gle/YhPgQTq1FHiH71B6A). I will also
initiate a conversation if you are not fulfilling yours. However, none
of us will meet all of the expectations perfectly---me included!---so
it's also important that we have grace and patience with one another.

<table class="table table-bordered mt-3">
  <thead>
    <tr>
      <th></th>
      <th>What I expect from you</th>
      <th>What you can expect from me</th>
    </tr>
  </thead>

  <tr>
    <th>Communication</th>
    <td>
      <ul>
        <li>Check your email and Teams for occasional course
          announcements.</li>
        <li>Let me know via email or Teams message if you will need to miss class
          for some reason.</li>
        <li>Let me know as soon as possible if you feel you are
          struggling, would like extra help, or have something
          going on that will affect your engagement in the
          course or your ability to fulfill your
          responsibilities.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Clearly communicate expectations, assignment
          details and dates, and grading standards.</li>
        <li>Return grades and feedback on submitted work within
          two weekdays of submission.</li>
        <li>Respond to emails within 24 hours.</li>
      </ul>
    </td>
  </tr>

  <tr>
    <th>Preparation</th>
    <td>
      <ul>
        <li>Come prepared to fully engage in class meetings, with
          distractions minimized, to the best of your ability.</li>
        <li>Spend time outside of class actively practicing
          unfamiliar or shaky concepts or skills (not just
          reading over notes).</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Have a concrete plan for how we will
          spend each class meeting, prepared to lead you through the
          plan.</li>
      </ul>
    </td>
  </tr>

  <tr>
    <th>Engagement</th>
    <td>
      <ul>
        <li>Actively engage in  lectures by taking notes and
          asking questions.</li>
        <li>Be proactive and intentional about spending time working
    on assignments.</li>
        <li>Abide by the
        College's <a href="https://www.hendrix.edu/Catalog/2021-2022/Academic_Policies_and_Regulations/Policies_and_Appeals/Academic_Integrity/">Academic
        Integrity Policy</a> and
        the <a href="http://ozark.hendrix.edu/~yorgey/ac-integrity-policy.html">Computer
            Science-specific Academic Integrity Policy</a>.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Make myself available to meet outside of class, and
          give you my full attention during a meeting.</li>
        <li>Be committed to your learning, open to feedback and
          willing to respond in substantive ways to your
          suggestions or concerns.</li>
      </ul>
    </td>
  </tr>
</table>

## <a name="attendance">Attendance</a>

Attendance in this class is not required as part of your grade.
However, I do expect you to attend and appreciate knowing in advance
if you will need to miss class.

## <a name="disabilities">Disabilities</a>

If you have a documented disability or some other reason that you
cannot meet the above expectations, and/or your learning would be best
served by a modification to the usual course policies, I would be
happy to work with you---please get in touch (via Teams or email)! The
course policies are just a means to an end; I don't care about the
policies per se but I do care about you and your learning.

*It is the policy of Hendrix College to accommodate students with
disabilities, pursuant to federal and state law. Students should
contact Julie Brown in the Office of Academic Success (505.2954;
brownj@hendrix.edu) to begin the accommodation process. Any student
seeking accommodation in relation to a recognized disability should
inform the instructor at the beginning of the course.*

## <a name="diversity">Diversity and Inclusion</a>

Hendrix College values a diverse learning environment as outlined in
the College's Statement on Diversity. All members of this community
are expected to contribute to a respectful, welcoming, and inclusive
environment for every other member of the community. If you believe
you have been the subject of discrimination please contact Dean Mike
Leblanc at [leblanc@hendrix.edu](mailto:leblanc@hendrix.edu) or
501-450-1222 or the Title IX Coordinator Jennifer Fulbright at
[titleix@hendrix.edu](mailto:titleix@hendrix.edu) or 501-505-2901. If
you have ideas for improving the inclusivity of the classroom
experience please feel free to [contact
me](https://forms.gle/YhPgQTq1FHiH71B6A).  For more information on
Hendrix non-discrimination policies, visit
[hendrix.edu/nondiscrimination](http://hendrix.edu/nondiscrimination).

## <a name="health">Mental and Physical Health</a>

Hendrix recognizes that many students face mental and/or physical
health challenges. If your health status will impact attendance or
assignments, please communicate with me as soon as possible.  If you
would like to implement academic accommodations, contact Julie Brown
in the office of Academic Success
([brownj@hendrix.edu](mailto:brownj@hendrix.edu)).  To maintain
optimal health, please make use of free campus resources like the
[Hendrix Medical Clinic](https://www.hendrix.edu/healthservices/) or
Counseling Services (501.450.1448).  Your health is important, and I
care more about your health and well-being than I do about this class!
