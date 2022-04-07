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
* Understand and apply the basic boolean logical operators.
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

<hr>

# <a name="calendar">Calendar</a>

<div style="text-align: center">
<a class="btn btn-primary" href="{{ site.submission }}">
  Assignment submission form
</a>
</div>
<br/>

| Date           | Topic                                                                                                                                                                         | Reading                           | Assignments due                                                          |
|:--------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|--------------------------------------------------------------------------|
| T 18 Jan       | [Introduction<br/>Boolean logic <img src="assets/images/yt.png" width="24px" />][18-Jan-video]                                                                                |                                   |                                                                          |
| Th 20 Jan      | [Boolean arithmetic <img src="assets/images/yt.png" width="24px" />][20-Jan-video] [<img src="assets/images/PDF2.png" width="24px" />][20-Jan-lec]                            | Chapters 1 and 2<br /> Appendix A |                                                                          |
| *F 21 Jan*     |                                                                                                                                                                               |                                   | [Project 1](projects/01-boolean-logic.html)                              |
|                |                                                                                                                                                                               |                                   |                                                                          |
| T 25 Jan       | [Boolean arithmetic; sequential logic <img src="assets/images/yt.png" width="24px" />][ALU-mem-video] [<img src="assets/images/PDF2.png" width="24px" />][ALU-mem-lec]        | Chapter 3                         |                                                                          |
| *W 26 Jan*     |                                                                                                                                                                               |                                   | [Project 2](projects/02-boolean-arithmetic.html)                         |
| Th 27 Jan      | [Sequential logic (memory) <img src="assets/images/yt.png" width="24px" />][mem-video] [<img src="assets/images/PDF2.png" width="24px" />][mem-lec]                           | Chapter 3                         |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *M 31 Jan*     |                                                                                                                                                                               |                                   | [Project 3](projects/03-memory.html)                                     |
| T 1 Feb        | [Machine & assembly language <img src="assets/images/yt.png" width="24px" />][asm-video] [<img src="assets/images/PDF2.png" width="24px" />][asm-lec]                         | Chapter 4                         |                                                                          |
|                | [example.asm](lectures/example.asm), [example2.asm](lectures/example2.asm)                                                                                                    |                                   |                                                                          |
| Th 3 Feb       | [Hack assembly examples <img src="assets/images/yt.png" width="24px" />][gabe-asm-video]                                                                                      |                                   |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *M 7 Feb*      |                                                                                                                                                                               |                                   | [Project 4](projects/04-machine-language.html)                           |
| T 8 Feb        | [Turing machine CPU <img src="assets/images/yt.png" width="24px" />][tm-cpu-video] [<img src="assets/images/PDF2.png" width="24px" />][tm-cpu-lec]                            | Chapter 5                         |                                                                          |
| Th 10 Feb      | [More Turing machine CPU; CPU history <img src="assets/images/yt.png" width="24px" />][cpu-hist-video] [<img src="assets/images/PDF2.png" width="24px" />][cpu-hist-lec]      |                                   |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *M 14 Feb*     |                                                                                                                                                                               |                                   | [Project 5](projects/05-computer-architecture.html)                      |
| T 15 Feb       | [Assembler <img src="assets/images/yt.png" width="24px" />][assembler-video] [<img src="assets/images/PDF2.png" width="24px" />][assembler-lec]                               | Chapter 6                         |                                                                          |
|                | [Assembler.py](lectures/assembler/Assembler.py), [example.tm](lectures/assembler/example.tm)                                                                                  |                                   |                                                                          |
| Th 17 Feb      | [6502 chip <img src="assets/images/yt.png" width="24px" />][6502-video] [<img src="assets/images/PDF2.png" width="24px" />][6502-lec]                                         |                                   |                                                                          |
|                | [6502 layout](https://davidmjc.github.io/6502/), [SMB source code](https://gist.github.com/1wErt3r/4048722)                                                                   |                                   |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *M 21 Feb*     |                                                                                                                                                                               |                                   | [Project 6](projects/06-assembler.html)                                  |
| T 22 Feb       | [VM memory layout & access <img src="assets/images/yt.png" width="24px" />][VM-video] [<img src="assets/images/PDF2.png" width="24px" />][VM-lec]                             | Chapter 7                         |                                                                          |
| Th 24 Feb      | *No class (ice)*                                                                                                                                                              |                                   |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *M 28 Feb*     |                                                                                                                                                                               |                                   | [Project 7](projects/07-stack-arithmetic.html)                           |
| T 1 Mar        | [VM stack arithmetic & branch instructions <img src="assets/images/yt.png" width="24px" />][VM-arith-video] [<img src="assets/images/PDF2.png" width="24px" />][VM-arith-lec] | Chapter 8                         |                                                                          |
| Th 3 Mar       | [VM function instructions <img src="assets/images/yt.png" width="24px" />][VM-fun-video] [<img src="assets/images/PDF2.png" width="24px" />][VM-fun-lec]                      |                                   |                                                                          |
|                | [VMfiles.py](lectures/VMFiles.py)                                                                                                                                             |                                   |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *M 7 Mar*      |                                                                                                                                                                               |                                   | [Project 8](projects/08-program-control.html)                            |
| T 8 Mar        | [Introduction to Jack <img src="assets/images/yt.png" width="24px" />][Jack-video] [<img src="assets/images/PDF2.png" width="24px" />][Jack-lec]                              | Chapter 9                         |                                                                          |
| Th 10 Mar      | [Jack example: jumping Jack <img src="assets/images/yt.png" width="24px" />][jump-video]                                                                                      |                                   |                                                                          |
| *F 11 Mar*     |                                                                                                                                                                               |                                   | [Project 9: Proposal](projects/09-high-level.html)                       |
|                |                                                                                                                                                                               |                                   |                                                                          |
| T 15 Mar       | Project 9 demos                                                                                                                                                               |                                   | [Project 9: Demo](projects/09-high-level.html)                           |
| Th 17 Mar      | *No class*                                                                                                                                                                    |                                   |                                                                          |
| *F 18 Mar*     |                                                                                                                                                                               |                                   | [Project 9](projects/09-high-level.html)                                 |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *Spring break* |                                                                                                                                                                               |                                   |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| T 29 Mar       | [Tokenizing input <img src="assets/images/yt.png" width="24px" />][tok-video] [<img src="assets/images/PDF2.png" width="24px" />][tok-lec]                                    | Chapter 10                        |                                                                          |
|                | [Tokenizer.py](lectures/tokenizer/Tokenizer.py)                                                                                                                               |                                   |                                                                          |
| Th 31 Mar      | A simple LISP compiler [<img src="assets/images/PDF2.png" width="24px" />][compiler-lec]                                                                                      |                                   |                                                                          |
|                | [Compiler.py](lectures/compiler/Compiler.py)                                                                                                                                  |                                   |                                                                          |
|                | *Unfortunately, Dr. Yorgey pushed the wrong button so there is no recording for the 3/31 class*                                                                               |                                   |                                                                          |
| *F 1 Apr*      |                                                                                                                                                                               |                                   | [Project 10/11A: Tokenizer](projects/10a-tokenizer.html)                 |
|                |                                                                                                                                                                               |                                   |                                                                          |
| T 5 Apr        | [Compiling Jack to VM <img src="assets/images/yt.png" width="24px" />][compile-jack-video]                                                                                    |                                   |                                                                          |
|                | [AlphaWhere/Main.jack](lectures/AlphaWhere/Main.jack) /  [compiler.txt](lectures/compiler.txt)                                                                                |                                   |                                                                          |
| *W 6 Apr*      |                                                                                                                                                                               |                                   | [Project 10/11B: Statements](projects/1011b-statements.html)             |
| Th 7 Apr       | [Compiling conditionals and loops <img src="assets/images/yt.png" width="24px" />][compile-cond-video]                                                                        | Chapter 11                        |                                                                          |
|                | [AlphaShow/Main.jack](lectures/AlphaShow/Main.jack) / [compiler.txt](lectures/compiler.txt)                                                                                   |                                   |                                                                          |
|                | [GO TO statement considered harmful](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf)                                                                          |                                   |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *M 11 Apr*     |                                                                                                                                                                               |                                   | [Project 10/11C: Conditionals and Loops](projects/1011c-cond-loops.html) |
| T 12 Apr       | Classes and arrays                                                                                                                                                            |                                   |                                                                          |
| Th 14 Apr      | Classes and arrays                                                                                                                                                            |                                   |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *M 18 Apr*     |                                                                                                                                                                               |                                   | [Project 10/11D: Classes and Arrays](projects/1011d-classes-arrays.html) |
| T 19 Apr       | Operating system                                                                                                                                                              | Chapter 12                        |                                                                          |
| Th 21 Apr      | Operating system                                                                                                                                                              |                                   |                                                                          |
|                |                                                                                                                                                                               |                                   |                                                                          |
| *M 25 Apr*     |                                                                                                                                                                               |                                   | Project 12A                                                              |
| T 26 Apr       | *Buffer*                                                                                                                                                                      |                                   |                                                                          |
| Th 28 Apr      | *Buffer*                                                                                                                                                                      |                                   |                                                                          |
| *F 29 Apr*     |                                                                                                                                                                               |                                   | Project 12B                                                              |

[18-Jan-video]: https://hendrix.sharepoint.com/sites/Section_26974/Shared%20Documents/General/Recordings/Computing%20Systems%20Organization-20220118_094748-Meeting%20Recording.mp4?web=1
[20-Jan-video]: https://hendrix.sharepoint.com/sites/Section_26974/Shared%20Documents/General/Recordings/Computing%20Systems%20Organization-20220120_094924-Meeting%20Recording.mp4?web=1
[20-Jan-lec]: lectures/2022-01-20-boolean-arithmetic.pdf
[ALU-mem-video]: https://youtu.be/tSLpUCtt8ms
[ALU-mem-lec]: lectures/2022-01-25-ALU-and-memory.pdf
[mem-video]: https://youtu.be/7rhQDgkFt4U
[mem-lec]: lectures/2022-01-27-memory.pdf
[asm-video]: https://hendrix.sharepoint.com/sites/Section_26974/Shared%20Documents/General/Recordings/Tues%202_1_%20machine%20+%20assembly%20language-20220201_094748-Meeting%20Recording.mp4?web=1
[asm-lec]: lectures/2022-02-01-machine-and-assembly-language.pdf
[gabe-asm-video]: https://www.youtube.com/watch?v=K8LwpzgoCcY&t=6s
[tm-cpu-video]: https://hendrix.sharepoint.com/sites/Section_26974/Shared%20Documents/General/Recordings/2_8_%20Turing%20Machine%20CPU-20220208_095750-Meeting%20Recording.mp4?web=1
[tm-cpu-lec]: lectures/2022-02-08-Turing-machine-CPU.pdf
[cpu-hist-video]: https://hendrix.sharepoint.com/sites/Section_26974/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FSection%5F26974%2FShared%20Documents%2FGeneral%2FRecordings%2F2%5F10%5F%20more%20CPUs%2D20220210%5F094530%2DMeeting%20Recording%2Emp4&parent=%2Fsites%2FSection%5F26974%2FShared%20Documents%2FGeneral%2FRecordings
[cpu-hist-lec]: lectures/2022-02-10-more-CPU.pdf
[assembler-video]: https://youtu.be/EWu6-J1TUz0
[assembler-lec]: lectures/2022-02-15-assembler.pdf
[6502-video]: https://youtu.be/aeG6s-ds0ok
[6502-lec]: lectures/2022-02-17-MOS6502.pdf
[VM-video]: https://youtu.be/83C8hPXw9zk
[VM-lec]: lectures/2022-02-22-VM.pdf
[VM-arith-video]: https://youtu.be/K90HEWq7y0A
[VM-arith-lec]: lectures/2022-03-01-VM-arithmetic.pdf
[VM-fun-video]: https://youtu.be/658lz1jnkE8
[VM-fun-lec]: lectures/2022-03-03-VM-functions.pdf
[Jack-video]: https://youtu.be/Bfz9ELaE1S4
[Jack-lec]: lectures/2022-03-08-Jack.pdf
[jump-video]: https://youtu.be/20kEyyvjhhI
[tok-video]: https://youtu.be/41YU_pQ-pTo
[tok-lec]: lectures/2022-03-29-tokenization.pdf
[compiler-lec]: lectures/2022-03-31-lisp.pdf
[compile-jack-video]: https://youtu.be/YpBH3pS7F_I
[compile-cond-video]: https://youtu.be/KSnDzbnHHsQ

<hr>
# Coursework and policies

## <a name="grading">Specifications grading</a>

This course uses *specifications grading*.  Briefly, this means that
grading of individual projects is on a credit/no-credit basis, with a
*specification* that tells you what you must do in order to get
credit. Your final letter grade in the course, in turn, is based
simply on the number of projects successfully completed.  There will
be 15 projects available to complete throughout the semester.

| Grade | Projects required |
|:-----:|:-----------------:|
| A     | 14                |
| B     | 12                |
| C     | 10                |
| D     | 8                 |

## <a name="deadlines">Due dates policy</a>

- Every project has a specific date and time (usually 5pm) at which it
  is due.

- Assignments may be turned in any time up to the deadline.  I will
  try my best to return graded assignments, with feedback, within *two
  weekdays* of being turned in.

- Projects **will not be accepted** after the deadline.

- However, I will automatically grant **extensions** to anyone who
  asks.  Simply send me an email prior to the deadline, asking for an
  extension on a particular project, and informing me what your new
  deadline will be.  The new deadline should be a specific day and
  time ("11pm this Saturday, March 5", not "in a couple days").  I
  will hold you to the new deadline.

    - Yes, this process may be chained: you may ask for another extension prior
      to your chosen deadline, and so on.  The key is communication.

- If you do not get credit for a project, you may revise and
  resubmit the project until you do.  There is no deadline for
  resubmissions.

- However, the above only applies if you made a reasonable attempt at
  the project the first time.  You cannot turn in a half-finished
  project before the deadline and then "revise" it by completing the
  rest.  If your project is only half-finished, you must request an
  extension.

- The absolute latest any project may be turned in is 5pm on Tuesday,
  May 3.

- As always, exceptions to this policy can be made in cases of
  emergency, mental health issues, *etc.* Please come talk to me!

## <a name="projects">Projects</a>

<div style="text-align: center">
<a class="btn btn-primary" href="{{ site.submission }}">
  Assignment submission form
</a>
</div>
<br/>

Your work in this course will consist of a series of challenging
projects from our textbook.  Taken all together, they will result in a
complete working (simulated) computer.  See the links below for the
details and specification for each project.

**Projects must be completed individually**.  Your experience of
learning how a computer works depends directly on your independent
completion of these projects.

* You **may** discuss the projects with other students.

* You **may not**:

    - **Read** any solution to any project, whether from another
      student, found online, or from any other source.

    - **Show** your solution to any other student.

    - **Give or receive help** in debugging a project solution. Requests
      for debugging help must be directed to the professor.

Any violations of this policy will be referred to the Committee on
Academic Integrity as a major violation, with a recommended sanction
of failure in the course.

| #      | Name                                                           | Due      |
|:------:|----------------------------------------------------------------|:--------:|
| 1      | [Boolean logic](projects/01-boolean-logic.html)                | F 21 Jan |
| 2      | [Boolean arithmetic](projects/02-boolean-arithmetic.html)      | W 26 Jan |
| 3      | [Memory](projects/03-memory.html)                              | M 31 Jan |
| 4      | [Machine language](projects/04-machine-language.html)          | M 7 Feb  |
| 5      | [Computer archtecture](projects/05-computer-architecture.html) | M 14 Feb |
| 6      | [Assembler](projects/06-assembler.html)                        | M 21 Feb |
| 7      | [VM I: stack arithmetic](projects/07-stack-arithmetic.html)    | M 28 Feb |
| 8      | [VM II: program control](projects/08-program-control.html)     | M 7 Mar  |
| 9      | [High-level programming](projects/09-high-level.html)          |          |
|        | Proposal                                                       | F 11 Mar |
|        | Demo                                                           | T 15 Mar |
|        | Final version                                                  | F 18 Mar |
| 10/11A | [Tokenizer](projects/10a-tokenizer.html)                       | F 1 Apr  |
| 10/11B | [Statements](projects/1011b-statements.html)                   | W 6 Apr  |
| 10/11C | [Conditionals and loops](projects/1011c-cond-loops.html)       | M 11 Apr |
| 10/11D | [Classes and arrays](projects/1011d-classes-arrays.html)       | M 18 Apr |
| 12A    | Operating system I                                             | M 25 Apr |
| 12B    | Operating system II                                            | F 29 Apr |

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

<!--
If you have chosen to attend class in person, you are expected to do
so consistently; you may not decide to attend remotely some days just
because you feel like it.  However, there are legitimate reasons
for attending remotely, such as feeling ill or travelling unavoidably.
-->

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
501-450-1222 or the Title IX Coordinator Allison Vetter at
[titleix@hendrix.edu](mailto:titleix@hendrix.edu)or 501-505-2901. If
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
