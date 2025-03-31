##### Data Modeling
1. process of creating specific data model -> for determined problem
2. data model -> relatively simple representation of real-world data structures
3. <mark style="background: #BBFABBA6;">database model</mark> -> implementation of data model in specific DB system

##### Entity
1. something which data will be collected and stored (object), distinguishable -> unique and distinct
2. <mark style="background: #FFFF00;">Attribute</mark> -> characteristic of entity
3. <mark style="background: #FFFF00;">Relationship</mark> -> association among entities

##### Relationship
1. One-to-many (1:M or 1..) relationship
	1. Painter create many paintings, but each is painted by 1 painter
2. Many-to-many (M:N ) relationship
	2. Employee learn many job skills, and each job skill may be learned by many employees
3. One-to-one (1:1 or 1..1) relationship

##### Data Models
1. <mark style="background: #FFFF00;">Hierarchical and Network model</mark>
	1. Hierarchical model
		1. level or segments, higher the parent, lower is the child
	2. Network model
		1. first introduced 1 to many relationship, more than 1 parent
2. <mark style="background: #FFFF00;">Relational model</mark>
	1. RDBMS -> hide complexities of relational model from user
	2. Table related to each other using <mark style="background: #FFFF00;">common attribute</mark>
	3. Have relational diagram -> show connection between tables
3. <mark style="background: #FFFF00;">Entity Relationship model</mark>
	1. Peter Chen 1976
	2. Have ERD -> graphical rep of DB components
	3. Entity 
		1. Each row -> Entity Instance / Entity occurrence
		2. Collection of entity -> entity set
		3. 3 AGENT -> entity set
		4. Have attributes
		5. Have relationships -> connectivity to other entities
	4. Model Notations ![[Pasted image 20250226142026.png]]
4. <mark style="background: #FFFF00;">Object-Oriented Model</mark>
	1. OODM, OODBMS
	2. ![[Pasted image 20250226142331.png|500]]
	3. It has its own methods
		1. real world actions such finding, changing, printing
	4. Inheritance
	5. Using UML class diagrams
5. <mark style="background: #FFFF00;">Object/Relational XML</mark>
	1. Extended relational data model (ERDM)
	2. O/R DBMS
	3. using XML
6. <mark style="background: #FFFF00;">Big Data and NoSQL</mark>
	1. Big data -> new way to handle large amount of data
		1. Volume -> amount of data stored
		2. Velocity -> Speed of data processed to get info and insight
		3. Variety -> Different data format


##### Last Read Page 85