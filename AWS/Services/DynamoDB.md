[[AWS (Amazon Web Services)]] service for No-SQL DB
1. Fully managed, high available, replication across 3 AZ
2. NoSQL DB - not relation DB
3. Flagship product AWS
4. Scales to massive workloads, distributed "serverless" db
5. Millions of req / seconds, T of rows, high storage
6. Fast and consistent
7. Single-digits ms latency - low latency retrieval
8. Integrated with IAM
9. Low cost, auto scaling capabilities
10. Standard & Infrequent Access Table Class
11. Very flexible for columns, <mark style="background: #FF5582A6;">cant join to another table</mark> 


##### Type of Data
1. Primary Key
	1. Partition Key
	2. Sort Key
2. Products
	1. Attributes

![[Pasted image 20241029192014.png | 400]]

#### DynamoDB Accelerator - DAX
1. Fully Managed in-memory cache for DynamoDB
2. Cache frequently read object
<mark style="background: #FF5582A6;">3. Specifically for DynamoDB</mark>
4. 10x performance improvement
