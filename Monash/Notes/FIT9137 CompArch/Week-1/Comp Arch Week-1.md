 ### 1. Number Systems
#### 1.1 What is a Computer?
1. Computer -> was people doing calculations
2. Digital computer
	1. CSIRAC -> Australia first computer (1949)
3. Computer Generations
	1. 1st gen: vacuum tubes
	2. 2nd gen: transistors
		1. small version and more reliable vacuum tubes
	3. 3rd gen: integrated circuits
	4. 4th gen: VLSI
		1. more compact -> can pack many transistors
		2. computationally performance
	5. 5th gen: quantum computers?
4. Computer
	1. anything that can does computational function
5. Modern Computer
	1. digital (work with 0s and 1s)
	2. use electronic circuits
	3. controlled by programs
	4. most have
		1. cpu
		2. ram
		3. i/o devices
	5. may connected to network

##### Why 0 and 1?
1. How can we represent information with 0/1 value?
	1. Bits, bytes, number systems and encodings
2. How can we calculate using 0/1 values?
	1. Boolean logic, algebra and circuits

##### Data
1. smallest unit -> <mark style="background: #FFFF00;">bit (0 or 1)</mark> -> on/off state
2. <mark style="background: #FFFF00;">8 bits -> 1 Byte</mark> -> smallest individual unit on computer
3. word -> chunk of bits (32 or 64 bit)
	1. 32 or lesser bits for simpler/smaller computer arch

#### 1.2 Number Systems
1. to represent numbers in digits
2. usually use decimal system
	1. 2396  = 2 x 10^3 + 3 x 10^2 + 9 x 10^1 + 6 x 10^0 
3. computer use <mark style="background: #FFFF00;">binary numbers</mark> (base2)
	1. 2396 -> need to divide into power of 2
		1. 1 x 2^11 = 2048
		2. 0 x 2^10 = 0
		3. 0 x 2^9 = 0
		4. 1 x 2^8 = 256
		5. 0 x 2^7 = 0
		6. 1 x 2^6 = 64
		7. 0 x 2^5 = 0
		8. 1 x 2^4 = 16
		9. 1 x 2^3 = 8
		10. 1 x 2^2 = 4
		11. 0 x 2^1 = 0
		12. 0 x 2^0 = 0
	2. total will be 2048 + 256 + 64 + 16 + 8 + 4 = 2396
	3. bin representation  will be 100101011100 base2

##### 1.2.1 Base16

| Decimal | Binary | Hex |
| ------- | ------ | --- |
| 0       | 0000   | 0   |
| 1       | 0001   | 1   |
| 2       | 0010   | 2   |
| 3       | 0011   | 3   |
| 4       | 0100   | 4   |
| 5       | 0101   | 5   |
| 6       | 0110   | 6   |
| 7       | 0111   | 7   |
| 8       | 1000   | 8   |
| 9       | 1001   | 9   |
| 10      | 1010   | A   |
| 11      | 1011   | B   |
| 12      | 1100   | C   |
| 13      | 1101   | D   |
| 14      | 1110   | E   |
| 15      | 1111   | F   |
1. Example
	1. 100101011100 base 2 -> 95C base16

#### 1.3 Signed Integer
1. to represent negative number, example -256 until 255 for 8bit/1Byte
2. "0" is the sign bit
3. drawbacks
	1. difficult to implement
	2. how addition work
	3. how to detect result is (+) or (-) or overflow
4. <mark style="background: #FFFF00;">Computer often use 2's complement</mark>
	1. math can be done easily
	2. overflow can be detected
	3. no duplication 0

##### 1.3. 2's Complement
![[Comp Arch Week-1 Drawings#^group=PJrRNq9u]]
1. Leftmost still indicates the sign
2. Negative 1 always 111111...
	1. Because leftmost is like -32 + 16 + 8 + 4 + 2 + 1 = -1
3. Largest positive number -> 011111...
4. Only have 1 zero  rep
5. can ignore carry bit

![[Comp Arch Week-1 Drawings#^group=W6jBoruh|800]]

#### 1.4 Representing Text
1. Using [ASCII](https://www.ascii-code.com/) and Unicode formats
	1. American Standard Code for Information Interchange (1967)
	2. Map all characters, numbers, and symbols into 7bit code
	3. 7bit not enough for international character sets
2. [Unicode](https://home.unicode.org/) standard
	1. between 0 and 10FFFF base16
	2. can represent any chars, emojis, etc.
3. [UTF-8](https://en.wikipedia.org/wiki/UTF-8) Unicode Transfer Formats
	1. Use block of 8 bits to represent each character
	2. h on hello -> 01101000 -> 104 - 96 = 8 (h is 8th character) 
	3. extremely widely used on internet
4.  [UTF-16](https://en.wikipedia.org/wiki/UTF-16)  (depreciated)
	1. each character mapped to exactly 2 Bytes (16 bits)
	2. only limited to the first 2^16 codepoints
5.  [UTF-32](https://en.wikipedia.org/wiki/UTF-32) (for fast memory access)
	1. mapped exactly 4 Bytes (32 bits)


### 2. Boolean Logic
![[Pasted image 20250305114623.png|500]]
![[Pasted image 20250305114634.png|500]]
![[Pasted image 20250305114644.png|500]]
![[Comp Arch Week-1 Supplementary Reading#^group=H9bd7cXJ| 700]]
