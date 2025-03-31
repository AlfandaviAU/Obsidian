 #### 1. Computer Architecture
1. CPU
2. Von Neumann
3. MARIE
##### 1.1. Computer Architecture
1. How to design and construct a computer
2. Von Neumann Architecture
	 ![[Pasted image 20250312093632.png|400]]
	1. CPU, Memory, I/O
		1. ALU
			1. Arithmetic
			2. Int addition, subtraction, multiplication
		2. Logic
			1. Boolean Operations
	2. Memory
		1. Store data and program code
		2. Connected to CPU visa <mark style="background: #FFFF00;">BUS</mark>
		3. CPU can read and write words from/to memory
	3. Registers
		1. Very <mark style="background: #FFFF00;">fast memory</mark> inside cpu
		2. Store temporary results
		3. Help move data around (from/to memory and I/O)
	4. Control Unit
		1. Responsible for executing program
		2. Control all components
		3. <mark style="background: #FFFF00;">Switches components on/off</mark> according to instructions
	5. I/O 
		1. Anything connected to computer
3. MARIE
	1. Machine Architecture that is Really Intuitive and Easy
	2. Very simple machine simulator
	3. Simulates : CPU, memory, and I/O
	4. All data stores in 16 bit words
4. Architecture ![[Monash/Notes/FIT9137 CompArch/Week-2/Comp Arch Week-2 Drawings.md#^group=o3bxVvcQLL3p9u90XAI8e|600]]
##### 1.2. Programs
1. Program tell computer what to do
2. CPU cant execute program directly
3. Need to be compiled/interpreted first
4. CPU can only execute machine code

##### 1.2.1 Machine Code
1. Very simple computer language
	1. Sequence of instructions
	2. Stored in memory
	3. Each instructions encoded in one or more words
2. ISA (Instruction Set Architecture)
	1. Do some math
	2. Move data between memory, registers, and i/o
	3. Execute conditionals and loops
3. Registers
	1. Small number of very fast memory cells inside CPU
	2. Each can hold 1 word of data
	3. General purpose
	4. Special purpose

##### 1.3. MARIE Programming
![[Monash/Notes/FIT9137 CompArch/Week-2/Comp Arch Week-2 Drawings.md#^group=bnHHRp3f]]
```MARIE
	Load 4 	/ Load contents of X into AC
	Add 5 	/ Add contents of Y to AC
	Store 4 	/ Store contents of AC into location X
	Halt
	DEC 42
	DEC 1
```

##### 1.3.1 Definitions
1. **AC (Accumulator)**
	1. The main register used for arithmetic and logic operations

2. **IR (Instruction Register)**
	2. Holds the instruction that is currently being executed

3. **MAR (Memory Address Register)**
	2. Holds the address of the memory location to be accessed

4. **MBR (Memory Buffer Register)**
	2. Temporarily holds data being transferred to/from memory

5. **PC (Program Counter)**
	2. Stores the address of the next instruction to be executed

6. **IN**
7. **OUT**

##### 1.3.2 Explanations
This looks like a simple assembly-like program using a basic instruction set, possibly for a hypothetical or educational computer. Let's break it down step by step.

### Instructions:

1. **LOAD 4** – Load the value stored at memory address 4 into the accumulator (ACC).
2. **ADD 5** – Add the value stored at memory address 5 to the accumulator.
3. **STORE 4** – Store the result from the accumulator back into memory address 4.
4. **HALT** – Stop execution.

### Memory Declarations:

- **DEC 42** at address 4 – This means memory address 4 starts with the value 42.
- **DEC 1** at address 5 – This means memory address 5 contains the value 1.

### Step-by-step execution:

| Step | Instruction | ACC (Accumulator) | Memory[4] | Memory[5] |
| ---- | ----------- | ----------------- | --------- | --------- |
| 1    | LOAD 4      | 42                | 42        | 1         |
| 2    | ADD 5       | 42 + 1 = 43       | 42        | 1         |
| 3    | STORE 4     | 43                | 43        | 1         |
| 4    | HALT        | (Stops execution) | 43        | 1         |

### Final State:

- Memory[4] = **43**
- Memory[5] = **1**
- The program successfully increments the value stored at memory address 4 by 1.

This is a simple program that increments the value in memory address 4 by the value stored in memory address 5 (which is 1). It’s a basic demonstration of load, add, store, and halt operations in an assembly-like language.
