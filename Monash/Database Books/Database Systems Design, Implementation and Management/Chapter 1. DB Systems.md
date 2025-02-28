##### General Concepts
1. Why need db?
	1. Data is ubiquitous (any form) and pervasive (persistent)
	2. Generate and consume data from birth to dead
	3. Essential for org to survive -> know their customer, product, money etc

2. Database -> <mark style="background: #FFFF00;">specialized</mark> structured that allow computer-based system to store, manage and retrieve data very quickly
3. Data -> Raw Facts <mark style="background: #FF5582A6;">(not processed to reveal its meaning)</mark>
4. Information -> Result of processing data to <mark style="background: #BBFABBA6;">reveal its meaning</mark> -> requires context
5. Data management -> study of proper generation, storage and retrieval of data
##### Database
1. Computer structure that store end user data, and its <mark style="background: #BBFABBA6;">metadata</mark> -> data about data
	1. metadata : type of values, table constraints, etc
2. DBMS -> program that <mark style="background: #ABF7F7A6;">manages DB structure</mark> and <mark style="background: #ABF7F7A6;">control access</mark> to data stored in DB
3. Advantages of DBMS :
	1. Improved data sharing
	2. Improved data security -> handle policies
	3. Better data integration
	4. Minimize data inconsistency
	5. Improved data access
	6. Improved decision making
	7. Increased end user productivity

##### Type of DB
1. Based of user
	1. single-user DB -> only support 1, cant multiple at same time
	2. multi-user DB -> small amount of user
		1. workgroup DB -> specific department
		2. enterprise DB -> support many department
2. Location
	1. centralized DB -> single location
	2. distributed DB -> multi different location
3. Purpose
	1. General purpose DB
	2. Discipline-specific DB
4. How they used and time sensitivity
	1. Operational DB -> day to day ops
		1. OLTP DB
		2. Transactional DB
		3. Prod DB
	2. Analytical DB -> Storing historical data -> for business decision making
		1. Data warehouse -> store data in format 
		2. OLAP (Online analytical processing) -> tools that work together to provide advanced data analysis
	3. Degree which data is structured
		1. Unstructured -> 0% 
		2. Structured -> 100%
		3. Semistructured -> 0% < n < 100% processed


