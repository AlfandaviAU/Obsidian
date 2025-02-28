#### 1. Static Array
- Fixed length container containing n elements indexable from range [0,n-1]
- Indexable -> Each index in the array can be referenced with number
![[Pasted image 20250120184439.png|300]]
#### 2. Dynamic Array
- Array that can grow and shrink in size
- How to implement :
	1. Create static array with initial capacity
	2. Add elements to array
	3. If max size -> create new array with 2x size, then copy original elements