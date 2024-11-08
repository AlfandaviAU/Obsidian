[[S3 (Simple Storage Service)]] storage classes
1. Standard - General Purpose
2. Standard - Infrequent Access (IA)
3. One Zone - Infrequent Access
4. Glacier Instant Retrieval
5. Glacier Flexible Retrieval
6. Glacier Deep Archive
7. Intelligent Tiering

Can move between classes manual / S3 Lifecycle config

#### S3 Durability and Availability
1. Durability
	1. High durability ( 99.999 %) accross multi AZ
	2. Same for all storage classes
2. Availability
	1. Depends storage class
	2. Example : S3 has 99.99%
	
![[Pasted image 20241027114237.png]]
##### 1. S3 Standard - General Purpose
1. 99.99 % Availability
2. Used for frequently accessed data
3. Low latency and high throughput
4. Sustain 2 concurrent facility failures
5. Use cases
	1. Big Data analytics
	2. mobile and gaming applications
	3. CDN

##### 2. S3 Infrequent Access
1. Less frequently accessed data, but <mark style="background: #BBFABBA6;">required rapid access when needed</mark>
2. Lower cost than S3 standard
###### 2.1 Standard - Infrequent Access
1. 99.9 % Availability
2. Use cases :
	1. Disaster Recovery, Backups
###### 2.2 One Zone - Infrequent Access
1. High durability in single AZ
2. Data lost when AZ destroyed
3. 99.5 % Availability
4. Use cases : 
	1. Secondary backup copies of data

##### 3. S3 Glacier
1. Low-cost object storage -> archiving and backup
2. Pricing : price for storage + obj retrieval cost

###### 3.1 Glacier Instant Retrieval
1. <1 s (ms) retrieval, great for data accessed once / quarter
2. Minimum storage duration 90 days

###### 3.2 Glacier Flexible Retrieval
1. 3 Flexibility Duration
	1. Expedited ( 1 - 5 minutes )
	2. Standard ( 3 - 5 hours )
	3. Bulk ( 5 - 12 hours ) - free
2. Minimum storage duration 90 days

###### 3.3 Glacier Deep Archive - long term storage
1. Standard (12 hours), Bulk (48 hours)
2. Lowest cost
3. Minimum storage duration 180 days

##### 4. S3 Intelligent - Tiering
1. Small monthly monitoring and auto-tiering fee
2. Move object across tiers based on usage
3. No retrieval chargees
4. Auto tiering : 
	1. Frequent Access Tier : default
	2. Infrequent Access Tier : > 30 days
	3. Archive Instant Access Tier : > 90 days
	4. Archive Access Tier (optional) : 90 - 700+ days
	5. Deep Archive Access Tier (optional) : 180 - 700+ days

We can create S3 Bucket Lifecycle Configuration for moving objects around storage classes