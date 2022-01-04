---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: course-single
---

# <a name="description">Overview</a>

{{ site.description }}

## <a name="goals">Learning Goals</a>

Upon completing this course, you will be able to:

* Describe the hierarchy of abstractions that define a modern computer:
    - Logic gates
    - CPU
    - Machine language
    - Assembly language and assemblers
    - Virtual machines
    - High-level languages and compilers
    - The operating system
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

XXX assignment submission form

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
| *F 11 Mar*     |                                            |                                   |           | Project 9: Concept                                  |
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
|                |                                            |                                   |           |                                                     |
|                |                                            |                                   |           |                                                     |
| T 3 May        | Final project presentations                |                                   |           |                                                     |
| (8:30-11:30)   |                                            |                                   |           |                                                     |

<hr>
# Coursework and policies

## <a name="deadlines">Due dates policy</a>

Every project has a specific date and time (usually 5pm) at which it
is due.

- Projects **will not be accepted** after the deadline.
- However, I will automatically grant extensions to anyone who asks.
  Simply send me an email prior to the deadline, asking for an
  extension on a particular project, and informing me what your new
  deadline will be.  The new deadline should be a specific day and
  time ("11pm this Saturday, March 5", not "in a couple days").  I
  will hold you to the new deadline.
- The latest any project may be turned in is XXX.

## <a name="projects">Projects</a>

Your work in this course will consist of a series of projects.

| #      | Name                                                           | Due      |
|:------:|----------------------------------------------------------------|:--------:|
| 1      | [Boolean logic](projects/01-boolean-logic.html)                | F 21 Jan |
| 2      | [Boolean arithmetic](projects/02-boolean-arithmetic.html)      | W 26 Jan |
| 3      | [Memory](projects/03-memory.html)                              | M 31 Jan |
| 4      | [Machine language](projects/04-machine-language.html)          | M 7 Feb  |
| 5      | [Computer archtecture](projects/05-computer-architecture.html) | M 14 Feb |
| 6      | [Assembler](projects/06-assembler.html)                        | M 21 Feb |
| 7      | [VM I: stack arithmetic](projects/07-stack-arithmetic.html)    | M 28 Feb |
| 8      | [VM II: program control]((projects/08-program-control.html))   | M 7 Mar  |
| 9      | High-level programming                                         |          |
|        | Concept                                                        | F 11 Mar |
|        | Demo                                                           | T 15 Mar |
|        | Final version                                                  | W 16 Mar |
| 10/11A | Tokenizer                                                      | F 1 Apr  |
| 10/11B | Statements                                                     | W 6 Apr  |
| 10/11C | Conditionals and loops                                         | M 11 Apr |
| 10/11D | Classes and arrays                                             | M 18 Apr |
| 12A    | Operating system I                                             | M 25 Apr |
| 12B    | Operating system II                                            | F 29 Apr |
| S      | System abstraction analysis                                    | T 3 May  |

## <a name="grading">Grading</a>

This course uses **specifications grading**. Your final grade in the
course is based on the number of projects successfully completed.
There will be 16 projects available to complete throughout the
semester.

| Grade | Projects required | Other requirements                                     |
|:-----:|:-----------------:|--------------------------------------------------------|
| A     | 15                | Must complete the system abstraction analysis project. |
| B     | 13                |                                                        |
| C     | 11                |                                                        |
| D     | 9                 |                                                        |

