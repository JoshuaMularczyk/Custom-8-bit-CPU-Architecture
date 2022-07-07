# Custom-8-bit-CPU-Architecture

This project was created for CPTR 380 instructed by Dr. Larray Aamodt. It is the design of a Custom 8-bit CPU with a histogram routine in mind

## Overview

For this project, Ethan Stong, [Christian Williams](https://github.com/cwill713), and I were tasked with developing a custom CPU (Central Processing Unit) architecture that would run a specific routine. Our architecture aimed for a simple histogram 16X16 greyscale image with up to 256 shades. The architecture has 16 8-bit registers and is a store/load instruction set (no Move instruction). There are 16 instructions that run on single cycle design (no pipeline). As the architecture is simple, we are assuming that the programmer made no errors so there is no error detection or exceptions. Max Program Size is 256 instructions.

## Theory

This was a 5 step project with an emphasis on creating a Custom Instruction Set, CPU Architecture, and an Assembler. We then implimented this in hardware using C++ language code.

<img width="269" alt="method" src="https://user-images.githubusercontent.com/103919092/177882280-98607888-c47d-4be6-b16a-c575cbc16c44.PNG">


## Custom Instruction Set

We realized that with only an 8-bit architecture, we would be limited to how many instructions we could create so this forced us to use only what was needed.

### Details:

- Instructions are 16 bits wide
- Uses 16 OP codes (4 bits each)
- Uses 16 8-bit registers
- Has 256 bytes of memory
- There are no direct operations on memory (Operations that would normally combine LW and ADD such as a MOV (move) will be seperate steps)
- We will only load from memory (LM, we use an ADD for registers and immediates)

### Instruction Format

-	First byte is opcode (first 4 bits)
-	Second byte is register (second 4 bits)
-	Third and fourth byte are the data or address (8bits)

<img width="527" alt="instforma" src="https://user-images.githubusercontent.com/103919092/177882299-ea938a1b-1b69-43c8-8a76-c8ab27b68d3c.PNG">

### Instruction Library

<img width="358" alt="lib1" src="https://user-images.githubusercontent.com/103919092/177882318-556a6f3a-49f4-460d-9694-de12c39f86ad.PNG">
<img width="358" alt="lib2" src="https://user-images.githubusercontent.com/103919092/177882319-aa0a20a1-fe54-4c83-a9c0-a5d1205ca6be.PNG">
<img width="358" alt="lib3" src="https://user-images.githubusercontent.com/103919092/177882322-2c30abfa-236f-4bc3-9f89-ee529b2a4996.PNG">

## Assembler

I designed the assembler using Python due to its user friendly token features. I would type out a series of our assembly instructions into a txt file shown below. The assembler would then look through all the instructions, determine what they were and what registers were being used, and output the instruction lines as binary code. The code for the assembler can be viewed [here](https://github.com/JoshuaMularczyk/Custom-8-bit-CPU-Architecture/blob/main/Program%20Files/Python%20Assember%20Code.txt).

Text file with the assembler input:
<img width="88" alt="assemin" src="https://user-images.githubusercontent.com/103919092/177890393-252ea3cd-22f0-4989-964c-627cee9000d3.PNG">

Text file with the assembler output:
<img width="138" alt="assemout" src="https://user-images.githubusercontent.com/103919092/177890395-3cc106a4-7470-41b5-b6bc-055ed85cb441.PNG">

### Part I.

The code displayed below allows access to the assembler input text file. It then processes the file and separates all the instructions into tokens. In this code, a token is anything separated by whitespace.

<img width="417" alt="code1" src="https://user-images.githubusercontent.com/103919092/177882380-418a1cc6-36ba-4475-83df-3812e50cfb51.PNG">
 
### Part II.

The second part of the assembler, represented by the code below, is in charge of deciding what OPCODE leads each line. Once it reads the first token of each line, it uses and if-else statement to determine what to do based on what instruction it is. The general idea of what happens in each if-statement is: the register tokens, address tokens, and immediate tokens are all read and added into an array as decimal values. These values are then all converted into binary.

<img width="262" alt="code2" src="https://user-images.githubusercontent.com/103919092/177882401-b6bb342a-f9e9-4e36-9b51-e41e3fc54ecb.PNG">
        
### Part III.

The final part of the assembler is sending these lines of binary into the output text file. This is displayed in the code below.

<img width="416" alt="code3" src="https://user-images.githubusercontent.com/103919092/177882426-1dd9f9d6-6b5b-46ae-ab89-b7347b9c2a41.PNG">

[Full Code](https://github.com/JoshuaMularczyk/Custom-8-bit-CPU-Architecture/blob/main/Program%20Files/Python%20Assember%20Code.txt).

## Hardware

The hardware design was discussed as a group, and Ethan drew out the basic architecture needed to implement our routine. Snippets of the architecture are shown below.

<img width="416" alt="code3" src="https://user-images.githubusercontent.com/103919092/177879477-3c5770e1-4f99-4d63-a4b3-b097bcd87400.png">

<img width="416" alt="code3" src="https://user-images.githubusercontent.com/103919092/177879560-7a524697-0a8d-4a78-8518-8b58a3798ba8.png">

## Software Simulation

The architecture was designed by Ethan and Christian in software using C++ where a block in the diagram (generally) correlates with a function in C++. The code is running a single cycle at a time with no concurrent tasks for more accurate simulation. The ALU has 7 operations that are controlled by a bus coming from the control unit. The control unit translates the opcode into different control lines for multilple components.

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

Other blocks created were program memory, main memory, control unit, program counter, and registers. The code for this can be viewed [here](). More indebth information for the software implementation can be read in our [report](https://github.com/JoshuaMularczyk/Custom-8-bit-CPU-Architecture/blob/main/Documentation/Custom%20CPU%20Report.docx).
