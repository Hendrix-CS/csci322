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

<hr>

# <a name="calendar">Calendar</a>

<div style="text-align: center">
<a class="btn btn-primary" href="{{ site.submission }}">
  Assignment submission form
</a>
</div>
<br/>

| Date           | Topic                                      | Reading                           | Resources | Assignments due                                     |
|:--------------:|--------------------------------------------|-----------------------------------|-----------|-----------------------------------------------------|
| T 18 Jan       | Introduction<br/>Boolean logic             |                                   |           |                                                     |
| Th 20 Jan      | Boolean arithmetic                         | Chapters 1 and 2<br /> Appendix A |           |                                                     |
| *F 21 Jan*     |                                            |                                   |           | [Project 1](projects/01-boolean-logic.html)         |
|                |                                            |                                   |           |                                                     |
| T 25 Jan       | Boolean arithmetic<br/>Sequential logic    | Chapter 3                         |           |                                                     |
| *W 26 Jan*     |                                            |                                   |           | [Project 2](projects/02-boolean-arithmetic.html)    |
| Th 27 Jan      | Sequential logic                           | Chapter 3                         |           |                                                     |
|                |                                            |                                   |           |                                                     |
| *M 31 Jan*     |                                            |                                   |           | [Project 3](projects/03-memory.html)                |
| T 1 Feb        | Machine language                           | Chapter 4                         |           |                                                     |
| Th 3 Feb       | Hack assembly examples                     |                                   |           |                                                     |
|                |                                            |                                   |           |                                                     |
| *M 7 Feb*      |                                            |                                   |           | [Project 4](projects/04-machine-language.html)      |
| T 8 Feb        | Computer architecture                      | Chapter 5                         |           |                                                     |
| Th 10 Feb      | Computer architecture                      |                                   |           |                                                     |
|                |                                            |                                   |           |                                                     |
| *M 14 Feb*     |                                            |                                   |           | [Project 5](projects/05-computer-architecture.html) |
| T 15 Feb       | Assembler                                  | Chapter 6                         |           |                                                     |
| Th 17 Feb      | Assembler                                  |                                   |           |                                                     |
|                |                                            |                                   |           |                                                     |
| *M 21 Feb*     |                                            |                                   |           | [Project 6](projects/06-assembler.html)             |
| T 22 Feb       | VM I: Stack arithmetic                     | Chapter 7                         |           |                                                     |
| Th 24 Feb      | Stack arithmetic practice</b>Memory layout |                                   |           |                                                     |
|                |                                            |                                   |           |                                                     |
| *M 28 Feb*     |                                            |                                   |           | [Project 7](projects/07-stack-arithmetic.html)      |
| T 1 Mar        | VM II: Program control                     | Chapter 8                         |           |                                                     |
| Th 3 Mar       | VM II: Program control                     |                                   |           |                                                     |
|                |                                            |                                   |           | [Project 8](projects/08-program-control.html)       |
| *M 7 Mar*      |                                            |                                   |           |                                                     |
| T 8 Mar        | High-level language (Jack)                 | Chapter 9                         |           |                                                     |
| Th 10 Mar      | High-level language                        |                                   |           |                                                     |
| *F 11 Mar*     |                                            |                                   |           | Project 9: Proposal                                 |
|                |                                            |                                   |           |                                                     |
| T 15 Mar       | Project 9 demos                            |                                   |           | Project 9: Demo                                     |
| *W 16 Mar*     |                                            |                                   |           | Project 9                                           |
| Th 17 Mar      | *Buffer*                                   |                                   |           |                                                     |
|                |                                            |                                   |           |                                                     |
| *Spring break* |                                            |                                   |           |                                                     |
|                |                                            |                                   |           |                                                     |
| T 29 Mar       | Tokenizing input                           | Chapter 10                        |           |                                                     |
| Th 31 Mar      | A simple compiler<br/>Jack to VM           |                                   |           |                                                     |
| *F 1 Apr*      |                                            |                                   |           | Project 10/11A                                      |
|                |                                            |                                   |           |                                                     |
| T 5 Apr        | Jack to VM                                 |                                   |           |                                                     |
| *W 6 Apr*      |                                            |                                   |           | Project 10/11B                                      |
| Th 7 Apr       | Conditionals and loops                     | Chapter 11                        |           |                                                     |
|                |                                            |                                   |           |                                                     |
| *M 11 Apr*     |                                            |                                   |           | Project 10/11C                                      |
| T 12 Apr       | Classes and arrays                         |                                   |           |                                                     |
| Th 14 Apr      | Classes and arrays                         |                                   |           |                                                     |
|                |                                            |                                   |           |                                                     |
| *M 18 Apr*     |                                            |                                   |           | Project 10/11D                                      |
| T 19 Apr       | Operating system                           | Chapter 12                        |           |                                                     |
| Th 21 Apr      | Operating system                           |                                   |           |                                                     |
|                |                                            |                                   |           |                                                     |
| *M 25 Apr*     |                                            |                                   |           | Project 12A                                         |
| T 26 Apr       | *Buffer*                                   |                                   |           |                                                     |
| Th 28 Apr      | *Buffer*                                   |                                   |           |                                                     |
| *F 29 Apr*     |                                            |                                   |           | Project 12B                                         |

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
|        | Final version                                                  | W 16 Mar |
| 10/11A | Tokenizer                                                      | F 1 Apr  |
| 10/11B | Statements                                                     | W 6 Apr  |
| 10/11C | Conditionals and loops                                         | M 11 Apr |
| 10/11D | Classes and arrays                                             | M 18 Apr |
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
