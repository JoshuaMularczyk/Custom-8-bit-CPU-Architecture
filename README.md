# Custom-8-bit-CPU-Architecture
Design of a 8-bit CPU Architecture with a histogram routine in mind
cptr 380 hardware design custom cpu with 8-bit architecture 

## Overview

For this project, [Ethan Stong], [Christian Williams], and I were tasked with developing a CPU architecture that would run a specific routine. The routine that we decided to base our architecture off of was a Histogram equalization routine of a simple greyscale image. With that in mind we decided to use 8-bit architecture due to its simplicity. Adding more bits would allow us to "use more pixels in our histogram routine", but for the time frame given we could demonstrate this project with 8 bits which allowed for up to 256 shades.

## Theory

This was a 5 step project with an emphasis on creating a Custom Instruction Set, CPU Architecture, and an Assembler. We then implimented this in hardware using C language code.

insert 5 step photo here

## Custom Instruction Set

We realized that with only an 8-bit architecture, we would be limited to how many instructions we could create so this forced us to use only what was needed.

### Details:

- Instructions are 16 bits wide
- Uses 16 OP codes (4 bits each)
- Uses 16 8-bit registers
- Has 256 bytes of memory
- There are no direct operations on memory (Operations that would normally combine LW and ADD. These would be seperate steps)
- We will only load from memory (LM, we use an ADD for registers and immediates)

### Instruction Format

picture

### Instruction Library

picture

## Assembler

I designed the assembler using Python due to its user friendly token features. I would type out a series of our assembly instructions into a txt file shown below. The assembler would then look through all the instructions, determine what they were and what registers were being used, and output the instruction lines as binary code. The code for the assembler can be viewed [here]().

2 pictures

## Hardware

The hardware design was discussed as a group, and Ethan drew out the basic architecture needed to implement our routine. Snippets of the architecture are shown below.

2 pics

## Software Simulation

The architecture was designed in software using C++. Here Ethan and Christian developed a program to create each main block of our architecture design.

The process for accumulating program memory was to:
- Read assember output (fstream)
- Copy into a temp array (sstream)
- Convert to ulong
- Read into program memory

Overview of ALU:
- 4 different options for arithmetic
- Has compare functionality
- Control Line Selection bus
- Triggers branch flag for beq, blt, and bgt instructions

Other blocks created were program memory, main memory, control unit, program counter, and registers. The code for this can be viewed [here]().
