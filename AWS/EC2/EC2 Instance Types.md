[[EC2 (Elastic Compute Cloud)]] has many of instance types, refer to https://aws.amazon.com/id/ec2/instance-types/, it has naming convention

#### <mark style="background: #ADCCFFA6;">M</mark><mark style="background: #FFF3A3A6;">5</mark> . <mark style="background: #BBFABBA6;">2xLarge</mark>
<mark style="background: #ADCCFFA6;">m : instance class</mark>
<mark style="background: #FFF3A3A6;">5 : generation</mark>
<mark style="background: #BBFABBA6;">2xLarge : size within instance class</mark>

https://instances.vantage.sh/
#### Instance types:
1. **General Purpose**
	1. Balance betweed compute, memory, and networking
	2. ie: t2.micro, M6g, M5...

2. **Compute Optimized**
	1. Great for compute-intensive task -> high performance processors
		1. Batch processing workloads
		2. Media transcoding
		3. High performance web servers
		4. High performance computing
		5. Scientific modeling & ML
		6. Dedicated gaming server
	2. ie : C6g, C6gn, C5... (prefix C)
	
3. **Memory Optimized**
	1. Fast performance for workloads process large dataset in memory
		1. High performance, db
		2. Distributed web scale cache stores
		3. In-memory database for BI
		4. App performing realtime for big unstructured data
	2. ie : R6, R5, R5a ... (prefix R for RAM)
	
4. **Storage Optimized**
	1. Great for storage-intensize task, require high instensive read and write access to large dataset on loca storage ( <mark style="background: #BBFABBA6;">Fast I/O writes</mark> )
		1. High frequency online transaction processing (OLTP)
		2. Relational & NoSQL DB
		3. Cache for in-memory DB (Redis)
		4. Data warehousing app
		5. Distributed file systems
	2. ie : I3, I3en, D2... (prefix I and D)

###### When to use memory optimized vs storage optimized for DB?
Memory optimized for analytics which needs large dataset in memory, while storage optimized used for large i/o writes to db
Business Intelligence -> use memory optimized -> big data processing