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

| Date          | Topic                                     | Reading & Links                                                                                      | Projects (recommended A schedule)                                          |
|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **T 16 Jan**  | Introduction, Boolean logic               |                                                                                                      |                                                                            |
| **Th 18 Jan** | Boolean arithmetic                        | Chapters 1 and 2                                                                                     |                                                                            |
|               |                                           | Appendix A                                                                                           |                                                                            |
| *F 19 Jan*    |                                           |                                                                                                      | [Project 1: Boolean logic](projects/01-boolean-logic.html)                 |
|               |                                           |                                                                                                      |                                                                            |
| **T 23 Jan**  | Boolean arithmetic & sequential logic     | Chapter 3                                                                                            |                                                                            |
| *W 24 Jan*    |                                           |                                                                                                      | [Project 2: Boolean arithmetic](projects/02-boolean-arithmetic.html)       |
| **Th 25 Jan** | Sequential logic (memory)                 | Chapter 3                                                                                            |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| *M 29 Jan*    |                                           |                                                                                                      | [Project 3: Memory](projects/03-memory.html)                               |
| **T 30 Jan**  | Machine & assembly language               | Chapter 4                                                                                            |                                                                            |
| **Th 1 Feb**  | Hack assembly examples                    |                                                                                                      |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| *M 5 Feb*     |                                           |                                                                                                      | [Project 4: Machine language](projects/04-machine-language.html)           |
| **T 6 Feb**   | Turing machine CPU                        | Chapter 5                                                                                            |                                                                            |
| **Th 8 Feb**  | More Turing machine CPU; CPU history      |                                                                                                      |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| *M 12 Feb*    |                                           |                                                                                                      | [Project 5: Computer architecture](projects/05-computer-architecture.html) |
| **T 13 Feb**  | Assembler                                 | Chapter 6                                                                                            |                                                                            |
| **Th 15 Feb** | 6502 chip                                 |                                                                                                      |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| *M 19 Feb*    |                                           |                                                                                                      | [Project 6: Assembler](projects/06-assembler.html)                         |
| **T 20 Feb**  | VM memory layout & access                 | Chapter 7                                                                                            |                                                                            |
| **Th 22 Feb** | TBD                                       |                                                                                                      |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| *M 26 Feb*    |                                           |                                                                                                      | [Project 7: VM I: Stack Arithmetic](projects/07-stack-arithmetic.html)     |
| **T 27 Feb**  | VM stack arithmetic & branch instructions | Chapter 8                                                                                            |                                                                            |
| **Th 29 Feb** | VM function instructions                  |                                                                                                      |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| *M 4 Mar*     |                                           |                                                                                                      | [Project 8: VM II: Program control](projects/08-program-control.html)      |
| **T 5 Mar**   | Introduction to Jack                      | Chapter 9                                                                                            |                                                                            |
| **Th 7 Mar**  | Jack example: jumping Jack                |                                                                                                      |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| **T 12 Mar**  | TBD                                       |                                                                                                      |                                                                            |
| **Th 14 Mar** | TBD                                       |                                                                                                      |                                                                            |
| *F 15 Mar*    |                                           |                                                                                                      | [Project 9: High-level programming](projects/09-high-level.html)           |
|               |                                           |                                                                                                      |                                                                            |
| **T 19 Mar**  | No class (spring break)                   |                                                                                                      |                                                                            |
| **Th 21 Mar** | No class (spring break)                   |                                                                                                      |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| **T 26 Mar**  | Tokenizing input                          | Chapter 10                                                                                           |                                                                            |
| **Th 28 Mar** | A simple LISP compiler                    |                                                                                                      |                                                                            |
| *F 29 Mar*    |                                           |                                                                                                      | [Project 10/11A: Tokenizer](projects/10a-tokenizer.html)                   |
|               |                                           |                                                                                                      |                                                                            |
| **T 2 Apr**   | Compiling Jack to VM                      |                                                                                                      |                                                                            |
| *W 3 Apr*     |                                           |                                                                                                      | [Project 10/11B: Statements](projects/1011b-statements.html)               |
| **Th 4 Apr**  | Compiling conditionals and loops          | Chapter 11                                                                                           |                                                                            |
|               |                                           | [GO TO statement considered harmful](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf) |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| *M 8 Apr*     |                                           |                                                                                                      | [Project 10/11C: Conditionals and Loops](projects/1011c-cond-loops.html)   |
| **T 9 Apr**   | Compiling arrays                          |                                                                                                      |                                                                            |
| **Th 11 Apr** | Compiling classes                         |                                                                                                      |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| *M 15 Apr*    |                                           |                                                                                                      | [Project 10/11D: Classes and Arrays](projects/1011d-classes-arrays.html)   |
| **T 16 Apr**  | Operating system I                        | Chapter 12                                                                                           |                                                                            |
| **Th 18 Apr** | Operating system II                       |                                                                                                      |                                                                            |
|               |                                           |                                                                                                      |                                                                            |
| *M 22 Apr*    |                                           |                                                                                                      | [Project 12A: Operating System I](projects/12-OS.html)                     |
| **T 23 Apr**  | Memory allocation and randomness          |                                                                                                      |                                                                            |
| **Th 25 Apr** | Project work day                          |                                                                                                      |                                                                            |
| *F 26 Apr*    |                                           |                                                                                                      | [Project 12B: Operating System II](projects/12-OS.html)                    |

<!-- END CALENDAR -->

<hr />
# <a name="grading">Grading</a>

## Grading contracts

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

- **The due date for each project you will complete**.  These can also
  be adjusted (see below), but you must commit to specific due dates
  at the beginning of the semester.  You may choose to simply use one
  of my suggested schedules of due dates, but I encourage you to think
  carefully about any commitments you have (plays, travel for sports,
  exams in other classes) and how you might wish to adjust your due
  dates as a result.

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

### Example grading contract

For example, a grading contract might look like this:

*My desired course grade in CSO is a C.  To
achieve this grade, I will complete the following:*

- [X] *CSCI student info survey*
- [ ] *Grading contract*
  - [X] *Submit grading contract*
  - [ ] *Grading contract evaluation 1*
  - [ ] *Grading contract evaluation 2*
- [ ] Projects (9)
  - [ ] Project 1
  - [ ] Project 2
  - [ ] Project 3
  - [ ] Project 4
  - [ ] Project 5
  - [ ] Project 9
  - [ ] Project 10/11A
  - [ ] Project 10/11B
  - [ ] Project 12A

*I will use the recommended deadline schedule for 9 projects, except
that I will turn in Project 5 by XXX.*

*My work plan is as follows: ...*

### Grading contract submission

You must turn in an initial proposed grading contract by the **start
of class on Thursday, January 18th**.  After the initial submission, I
may require some revisions before I approve your contract.

### <a name="evaluation">Contract evaluation and adjustment</a>

Two times during the semester (Monday, September 25 and Monday,
October 30) you are required to reflect on your progress in the course
and complete an evaluation of your work, comparing it against what you
agreed to in your grading contract.  Your evaluation should:

1. Contain a copy of your original grading contract, with items you
   have completed checked off.

2. Revise your grading contract with more specific details as
   appropriate, for example, regarding which modules you intend to
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

To "complete" an assignment means to complete it at or above the
required criteria for receiving credit.  For example, "complete a
midterm exam" means not just taking the exam, but scoring sufficiently
high on the problems so as to receive credit (possibly after retaking
it).

### A, B, and C grades

* To earn an A in the course, you must complete all the requirements
  for a B, plus:
    * Complete the final exam and both midterm [exams](#exams).
	* Complete a minimum of eight [problem sets](#problemsets).
	* Have at most one unexcused [absence](#attendance).

* To earn a B in the course, you must complete all the requirements
  for a C, plus:
    * Complete both midterm [exams](#exams).
	* Complete a minimum of seven [problem sets](#problemsets).
	* Have at most two unexcused [absences](#attendance).

* To earn a C in the course, you must:
    * Complete the [CSCI student information survey][survey].
    * Submit and agree on a [grading contract](#grading) with the instructor.
    * Complete two [grading contract evaluations](#evaluation).
    * Complete at least one midterm [exam](#exams).
	* Complete a minimum of five [problem sets](#problemsets).
	* Have at most three unexcused [absences](#attendance).

### D and F grades

[*Adapted from Cathy Davidson.*] You cannot intentionally contract for
a grade of D (and certainly not for an F).  However, I reserve the
right to award a grade of D or F to anyone who fails to meet their
contractual obligations in a systematic way. A "D" grade denotes some
minimal fulfilling of the contract; an "F" denotes absence of enough
satisfactory work, as contracted, to warrant passing of the
course. Both a "D" and "F" denote a breakdown of the contractual
relationship.


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
| A     | 15                |
| B     | 12                |
| C     | 9                 |
| D     | 6                 |

## <a name="contract">Grading contract</a>



## <a name="deadlines">Submissions, deadlines, and resubmission</a>

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
| 12A    | [Operating system I](projects/12-OS.html)                      | M 25 Apr |
| 12B    | [Operating system II](projects/12-OS.html)                     | F 29 Apr |

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
