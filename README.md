# Custom-8-bit-CPU-Architecture

This project was created for CPTR 380 instructed by Dr. Larray Aamodt. It is the design of a Custom 8-bit CPU with a histogram routine in mind

## Overview

For this project, [Ethan Stong], [Christian Williams], and I were tasked with developing a CPU architecture that would run a specific routine. The routine that we decided to base our architecture off of was a Histogram equalization routine of a simple greyscale image. With that in mind we decided to use 8-bit architecture due to its simplicity. Adding more bits would allow us to "use more pixels in our histogram routine", but for the time frame given we could demonstrate this project with 8 bits which allowed for up to 256 shades.

For this project, [Ethan Stong](), [Christian Williams](), and I were tasked with developing a custom CPU (Central Processing Unit) architecture that would run a specific routine. Our architecture aimed for a simple 16X16 greyscale image with up to 256 shades. The architecture has 16 8-bit registers and is a store/load instruction set (no Move instruction). There are 16 instructions that run on single cycle design (no pipeline). As the architecture is simple, we are assuming that the programmer made no errors so there is no error detection or exceptions. Max Program Size is 256 instructions.

## Theory

This was a 5 step project with an emphasis on creating a Custom Instruction Set, CPU Architecture, and an Assembler. We then implimented this in hardware using C++ language code.

insert 5 step photo here

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

picture

### Instruction Library

picture

## Assembler

I designed the assembler using Python due to its user friendly token features. I would type out a series of our assembly instructions into a txt file shown below. The assembler would then look through all the instructions, determine what they were and what registers were being used, and output the instruction lines as binary code. The code for the assembler can be viewed [here]().

2 pictures

### Part I.

The code displayed below allows access to the assembler input text file. It then processes the file and separates all the instructions into tokens. In this code, a token is anything separated by whitespace.

file = "assemblerInput.txt"
filehandle = open("assemblerInput.txt","r")
with filehandle:
    for line in filehandle:
        tokenized_line = line.split()
        
### Part II.

The second part of the assembler, represented by the code below, is in charge of deciding what OPCODE leads each line. Once it reads the first token of each line, it uses and if-else statement to determine what to do based on what instruction it is. The general idea of what happens in each if-statement is: the register tokens, address tokens, and immediate tokens are all read and added into an array as decimal values. These values are then all converted into binary.

if tokenized_line[0].upper() =="LM":
            r=int(tokenized_line[1][1])
            hex = tokenized_line[2]
            hex_list = hex.split("x")
            v=int(hex_list[(1)])                            
            b=[2,r,v>>4,v&0xF]                            
            i=bin(b[0])
            j=bin(b[1])
            k=bin(b[2])
            l=bin(b[3])
            m=[i,j,k,l,]
            
### Part III.

The final part of the assembler is sending these lines of binary into the output text file. This is displayed in the code below.

lines = m
            with open('assemblerOutput.txt', 'a') as f:
                for line in lines:
                    f.write(line)
                    f.write(' ')


                f.write('\n')

[Full Code]().

## Hardware

The hardware design was discussed as a group, and Ethan drew out the basic architecture needed to implement our routine. Snippets of the architecture are shown below.

![image](https://user-images.githubusercontent.com/103919092/177879477-3c5770e1-4f99-4d63-a4b3-b097bcd87400.png)

![image](https://user-images.githubusercontent.com/103919092/177879560-7a524697-0a8d-4a78-8518-8b58a3798ba8.png)

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

Other blocks created were program memory, main memory, control unit, program counter, and registers. The code for this can be viewed [here](). More indebth information for the software implementation can be read in our [report]().
