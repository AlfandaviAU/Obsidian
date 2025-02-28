---
Book: "[[Database Systems Design, Implementation, and Management (Carlos Coronel Steven Morris) (2019).pdf]]"
---
1. Creating Data Everyday -> On Any Activities, Data -> Ubiquitous and Pervasive
##### <mark style="background: yellow;">Data vs Information</mark>
1. <mark style="background: #FF5582A6;">Data</mark> -> Raw Facts and have no useful meaning before processed
2. <mark style="background: #FF5582A6;">Information</mark> -> Result of processing raw data to reveal its meaning
3. Information requires Context for reveal its meaning
	1. 105° -> in Fahrenheit or Kelvin or Any Temp Scale? For what machine temp? body temp?

2. Data Management -> Proper generation, storage and retrieval of data
3. <mark style="background: #FF5582A6;">Metadata</mark> -> data about data

##### DBMS (Database Management System)
1. Collection of programs
2. Manage DB Structure
3. Control access to data stored in DB

4. <mark style="background: #FF5582A6;">Query</mark> -> Specific request to DBMS for data manipulation -> send back query result set

##### Type of DB
1. By user ? 
	1. single-user DB -> can only serve 1 user at 1 time
	2. multiuser DB -> support multiple user
		1. specific department -> Workgroup DB
		2. entire org and many users -> ERP DB
2. By location ?
	1. Single site location -> Centralized DB
	2. Several different sites -> Distributed DB
3. By data stored ?
	1. General Purpose DB -> Wide variety of data
	2. Discipline-specific DB -> Specific Subject

<mark style="background: #FFB86CA6;">Production DB</mark> -> Company's day-to-day operations

#### Analytical DB
1. Data Warehouse
	1. Special DB to store data, formatting
2. OLAP (Online Analytical Processing)
	1. Tools for data analysis from Data Warehouse
	2. Business Intelligence purpose

**Business Intelligence** -> Capture and process business data to generate information to support business decision making

#### Unstructured vs Structured Data
1. Unstructured -> original (raw) state
2. Structured -> Result of processing unstructured data
3. Semi-structured data -> Already processed to some extent