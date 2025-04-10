![[Pasted image 20250410100420.png]]
1. Protocol vs Protocol Layering
	1. protocol -> Set of rules for communication (rules of exchanging information) so both end can understand each other and interpret data correctly
		1. HTTP
		2. TCP
		3. IP
	2. protocol layering -> organizing complex protocol into few simpler layers
		1. OSI Model
		2. TCP/IP Model
2. Benefit (OUTWEIGHT THE DRAWBACKS)
		1. Division of task -> make its easy to understand
		2. We can swap without affecting the others
			1. Least affected on other layers
		3. Hides complexity
			1. Don't have to worry how data across the network
3. Disadvantages
		1. Overhead
			1. Extra information on Headers and Trailers
		2. Redundancy
			1. Error detection may repeat across layers (inefficiency)
				1. Performance
				2. Usage of Resources
4. Logical Connection
	1. Basically way we think
	2. Layer 3 -> Layer 3
	3. Layer 2 -> Layer 2
	4. Layer 1 -> Layer 1
	5. each corresponding layer, follows the same protocol (protocol consistency)
5. Addressing
	1. App layer -> App Name
	2. Transport Layer -> Port 0 until 65,535 (locally unique)
	3. Network Layer -> IP Address (globally unique logical address)
	4. Data-link Layer -> MAC Address (globally unique NIC address)

6. 