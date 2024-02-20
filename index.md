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

<div style="text-align: center">
<a class="btn btn-primary" href="{{ site.submission }}">
  Assignment submission form
</a>
</div>
<br/>

<!-- BEGIN CALENDAR -->

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
| **Th 22 Feb** | VM stack arithmetic & branch instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Chapter 8                                                                                            | Grading contract evaluation I due                                          |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 26 Feb*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 7: VM I: Stack Arithmetic](projects/07-stack-arithmetic.html)     |
| **T 27 Feb**  | VM function instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Chapter 8                                                                                            |                                                                            |
| **Th 29 Feb** | TBD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 4 Mar*     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 8: VM II: Program control](projects/08-program-control.html)      |
| **T 5 Mar**   | Introduction to Jack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Chapter 9                                                                                            |                                                                            |
| **Th 7 Mar**  | Jack example: jumping Jack                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 11 Mar*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 9: High-level programming](projects/09-high-level.html)           |
| **T 12 Mar**  | TBD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                      |                                                                            |
| **Th 14 Mar** | TBD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| **T 19 Mar**  | *No class (spring break)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                      |                                                                            |
| **Th 21 Mar** | *No class (spring break)*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| **T 26 Mar**  | Tokenizing input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Chapter 10                                                                                           |                                                                            |
| **Th 28 Mar** | A simple LISP compiler                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                      |                                                                            |
| *F 29 Mar*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 10/11A: Tokenizer](projects/10a-tokenizer.html)                   |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| **T 2 Apr**   | Compiling Jack to VM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                      |                                                                            |
| *W 3 Apr*     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 10/11B: Statements](projects/1011b-statements.html)               |
| **Th 4 Apr**  | Compiling conditionals and loops                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Chapter 11                                                                                           | Grading contract evaluation II due                                         |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [GO TO statement considered harmful](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf) |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 8 Apr*     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 10/11C: Conditionals and Loops](projects/1011c-cond-loops.html)   |
| **T 9 Apr**   | Compiling arrays                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                      |                                                                            |
| **Th 11 Apr** | Compiling classes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 15 Apr*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 10/11D: Classes and Arrays](projects/1011d-classes-arrays.html)   |
| **T 16 Apr**  | Operating system I                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Chapter 12                                                                                           |                                                                            |
| **Th 18 Apr** | Operating system II                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                      |                                                                            |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      |                                                                            |
| *M 22 Apr*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 12A: Operating System I](projects/12-OS.html)                     |
| **T 23 Apr**  | Memory allocation and randomness                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                      |                                                                            |
|               | Course evaluations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                      |                                                                            |
| **Th 25 Apr** | Project work day                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                      |                                                                            |
| *F 26 Apr*    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                      | [Project 12B: Operating System II](projects/12-OS.html)                    |

<!-- END CALENDAR -->

<hr />
# <a name="grading">Grading</a>

## <a name="contracts">Grading contracts</a>

You will prepare and submit for my approval a *grading contract and
work plan* explaining your chosen final grade and what you will do to
achieve it.  You will then earn your chosen final grade by fulfilling
the agreed-upon contract.

This may be different than what you are used to.  Professor [Cathy
Davidson](https://www.gc.cuny.edu/people/cathy-n-davidson) of CUNY
perfectly sums up the reasons for doing things this way:

> The advantage of contract grading is that you, the student, decide
> how much work you wish to do this semester; if you complete that
> work on time and satisfactorily, you will receive the grade for
> which you contracted. This means planning ahead, thinking about all
> of your obligations and responsibilities this semester and also
> determining what grade you want or need in this course. The
> advantage of contract grading to the professor is no whining, no
> special pleading, on the student's part. If you complete the work you
> contracted for, you get the grade. Done. I respect the student who
> only needs a C, who has other obligations that preclude doing all of
> the requirements to earn an A in the course, and who contracts for
> the C and carries out the contract perfectly.

### Required components of a grading contract

There is no specific format required for a grading contract, but it
must have the following components:

- **Your desired course grade.**  You may choose to contract for an A,
  B, or C (if you're wondering about D's and F's, [see
  below](#evaluation)).  Note that your grading contract *should not*
  explain the *reasons* for your choice.  I will not judge you because
  of your choice, and you do not need to justify it: there are as many
  different valid reasons for choosing to work toward a particular
  final grade as there are students.  If you do wish to explain to me the
  reasons for your choice---which you are in no way required to
  do---you may do so in an email, a personal conversation, *etc.*, but
  it should not go in your contract.

- **A description of the work and requirements you will complete, in
  checklist format.**  It doesn't have to be super detailed, but you
  do have to explicitly include everything.  For example, you can't
  just say "I will complete all the assignments listed in the
  syllabus"; you must actually list them.  This is so that you and I
  both know that you are explicitly aware of the requirements, and to
  help you keep track of what you have completed and what you have yet
  to complete.  You also have some choice in terms of which
  assignments you complete, so you must record your choice in the
  contract.

  **Note** that at the beginning of the semester you may not have a
  very good idea about this.  For example, if you need to complete
  9 projects, it's not reasonable to insist that you know which
  specific projects you plan to complete.  However, you can refine your
  contract over the course of the semester.  You just have to put
  **something** to start; for example, a reasonable default would be
  to plan to complete the first nine projects assigned.  I have also
  provided some sample selections of projects and due dates below.

- **The specific due date and time for each project you will
  complete**.  You must commit to specific due dates at the beginning
  of the semester.  You may choose to simply use one of my suggested
  schedules of deadlines, but I encourage you to think carefully about
  any commitments you have (plays, travel for sports, exams in other
  classes) and how you might wish to adjust your due dates as a
  result.

- **A work plan**.  Success in this class requires consistent,
  sustained effort; for an A, you should expect to spend about 7 hours
  a week outside of class working on projects. Along with your grade
  contract, you must turn in a *work plan*, a one-to-two paragraph
  plan for how you will make time to work on the course projects. Be
  as specific as possible, and be creative in coming up with very
  specific ways to help yourself succeed. Some examples:

    -   Horrible: "I will work on CSO projects  7 hours per week."

    -   Bad: "I will work on CSO projects from 2-4pm every Tuesday and
        from 9-noon every Sunday."

    -   Good: "Every Tuesday from 2-5pm, I will go to the library
        which is a good distraction-free place for me to work.  I will
        turn off my phone and put Teams in "Do Not Disturb" mode. I
        will spend the first 15 minutes reviewing material from class
        and the textbook.  The rest of the time will be devoted to
        working on the latest project, referring back to the textbook
        and in-class materials as necessary.  I will work in 25-minute
        chunks with 5-minute breaks.  Depending on how the session
        goes, I will write down a list of questions and schedule
        office hours for later in the week.  On Thursdays and
        Saturdays, ..." etc.

  To receive credit, a work plan must be at the level of detail of
  the "Good" example or higher.

  Note that the work plan is not part of the "contract" per se, that
  is, your grade is not based on how well you stick to your work plan.
  Instead, it is intended as a helpful tool for your own planning and
  a useful jumping-off point for discussion if you get behind.

### Example grading contract

For example, a grading contract might look like this:

*My desired course grade in CSO is a C.  To achieve this grade, I will
complete the following:*

- [X] *CSCI student info survey*
- [ ] *Grading contract*
  - [X] *Submit grading contract*
  - [ ] *Grading contract evaluation 1*
  - [ ] *Grading contract evaluation 2*
- [ ] *Projects (9)*
  - [ ] *Project 1*
  - [ ] *Project 2*
  - [ ] *Project 3*
  - [ ] *Project 4*
  - [ ] *Project 5*
  - [ ] *Project 9*
  - [ ] *Project 10/11A*
  - [ ] *Project 10/11B*
  - [ ] *Project 12A*

*I will use the recommended deadline schedule for 9 projects, except
that my deadlines will be at 10pm instead of 5pm, and I will turn in
Project 5 by 2/24 instead of 2/26. [Your schedule of deadlines will
hopefully be more detailed/customized than this.]*

*My work plan is as follows: [your detailed work plan here]*

### Grading contract submission

You must turn in an initial proposed grading contract by the **start
of class on Thursday, January 18th**.  After the initial submission, I
may require some revisions before I approve your contract.

### <a name="evaluation">Contract evaluation and adjustment</a>

Two times during the semester (Thursday, February 22 and Thursday,
April 4) you are required to reflect on your progress in the course
and complete an evaluation of your work, comparing it against what you
agreed to in your grading contract.  Your evaluation should:

1. Contain a copy of your original grading contract, with items you
   have completed checked off.

2. Revise your grading contract with more specific details as
   appropriate, for example, regarding which projects you intend to
   complete.

3. Include a 1-2 paragraph reflection, which answers questions such as the
   following:

    * What have you done well?
    * What have you learned?
    * What could you do to improve your learning?
    * What could I (the instructor) do to improve your learning?
    * Are there ways in which you have not lived up to the requirements of
      your contract, and if so, what steps are you taking, or will you
      take, to rectify that?

Your evaluation is also an opportunity to request an adjustment to
your contract in either direction. If you find that you will be unable
to meet the obligations of your contract, you may request to move to a
lower grade and its requirements. Contrariwise, if you find that
you’ve been performing above the obligations of your contract, you may
request to fulfill the requirements for a higher grade.

**Note**, however, that you don't have to wait for an evaluation to
adjust your contract.  If your life has really gone off the rails (or
if, say, you are finding the class easier and more enjoyable than you
thought!) just come and talk to me about adjusting your contract.

### <a name="requirements">A, B, and C grades</a>

* To earn an A in the course, you must complete all the requirements
  for a C, and complete all 15 [projects](#projects)---that is,
  build a complete, working computer.

* To earn a B in the course, you must complete all the requirements
  for a C and complete a minimum of 12 [projects](#projects).

* To earn a C in the course, you must:
    * Complete the [CSCI student information survey](https://forms.gle/VLRVHjUAisWP5R9J8).
    * Submit and agree on a [grading contract](#grading) with the instructor.
    * Complete two [grading contract evaluations](#evaluation).
	* Complete a minimum of nine [projects](#projects).

### D and F grades

[*Adapted from Cathy Davidson.*] You cannot intentionally contract for
a grade of D (and certainly not for an F).  However, I reserve the
right to award a grade of D or F to anyone who fails to meet their
contractual obligations in a systematic way. A "D" grade denotes some
minimal fulfilling of the contract (typically, I would want to see at
least 5 projects complete). An "F" denotes absence of enough
satisfactory work, as contracted, to warrant passing of the
course. Both a "D" and "F" denote a breakdown of the contractual
relationship.

<hr>
# Coursework and policies

## <a name="projects">Projects</a>

Your work in this course will consist of a series of challenging
projects from our textbook.  Taken all together, they will result in a
complete, working (simulated) computer.

Below you will find a list of all the projects in one place, as well
as suggested deadlines and subsets of projects depending on your
desired grade.

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

| #      | Topic                                                          | Avg time (hrs) | A        | B        | C        |
|:------:|----------------------------------------------------------------|:--------------:|:--------:|:--------:|:--------:|
| 1      | [Boolean logic](projects/01-boolean-logic.html)                | 5              | F 19 Jan | F 19 Jan | M 22 Jan |
| 2      | [Boolean arithmetic](projects/02-boolean-arithmetic.html)      | 5              | W 24 Jan | W 24 Jan | M 29 Jan |
| 3      | [Memory](projects/03-memory.html)                              | 5              | M 29 Jan | M 29 Jan | W 7 Feb  |
| 4      | [Machine language](projects/04-machine-language.html)          | 6              | M 5 Feb  | M 5 Feb  | F 16 Feb |
| 5      | [Computer archtecture](projects/05-computer-architecture.html) | 7              | M 12 Feb | W 14 Feb | M 26 Feb |
| 6      | [Assembler](projects/06-assembler.html)                        | 8              | M 19 Feb | M 26 Feb |          |
| 7      | [VM I: stack arithmetic](projects/07-stack-arithmetic.html)    | 8              | M 26 Feb | M 4 Mar  |          |
| 8      | [VM II: program control](projects/08-program-control.html)     | 8              | M 4 Mar  |          |          |
| 9      | [High-level programming](projects/09-high-level.html)          | 7              | M 11 Mar | M 11 Mar | M 11 Mar |
| 10/11A | [Tokenizer](projects/10a-tokenizer.html)                       | 5              | F 29 Mar | M 1 Apr  | F 5 Apr  |
| 10/11B | [Statements](projects/1011b-statements.html)                   | 7              | W 3 Apr  | W 10 Apr | M 15 Apr |
| 10/11C | [Conditionals and loops](projects/1011c-cond-loops.html)       | 8              | M 8 Apr  | W 17 Apr |          |
| 10/11D | [Classes and arrays](projects/1011d-classes-arrays.html)       | 8              | M 15 Apr |          |          |
| 12A    | [Operating system I](projects/12-OS.html)                      | 6              | M 22 Apr | F 26 Apr | F 26 Apr |
| 12B    | [Operating system II](projects/12-OS.html)                     | ?              | F 26 Apr |          |          |

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

* You **may** use generative AI tools such as ChatGPT or GitHub
  Copilot.

    - The projects in this class are sufficiently high-level that
      generative AI is not going to be able to do them for you.  It
      could be an interesting learning experience to figure out ways
      to use these tools effectively.

    - If you do use generative AI tools, you **must cite their use**
      (*e.g.* in a comment explaining how you used them).

* You **may not**:

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
