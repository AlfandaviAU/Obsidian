1. Highly-secure, portable devices to collect and process data at the edge, and migrate data into and out of AWS
	1. Snowcone
		1. 2 CPU, 4GB of memory
		2. 8 TB of storage (HDD)
		3. 14 TB of storage (SSD)
	2. Snowball Edge
		1. Can be compute optimized or storage optimized
			1. Storage optimized : 80 TB
			2. Compute Optimized : 39.5 TB
		2. Run EC2 instances or Lambda functions at the edge
	3. Snowmobile
		1. 100 PB of storage
Use cases edge computing :
1. preprocess data
2. machine learning
3. transcoding media
 ![[Pasted image 20241027115352.png]]

##### Data Migrations with AWS Snow Family
![[Pasted image 20241027115432.png]]

AWS Snow Family : offline devices to perform data migrations
If it takes > 1 week to transfer over network, use snowball devices

![[Snow Family]]

Before : over the network upload files
After : Upload to snowball devices, then ship the devices to Amazon then Amazon team will upload the files to their network and desired bucket

##### Usage Process
1. Request Snowball devices for delivery
2. IInstall snowball client / AWS OpsHub on our servers
3. Connect snowball to our servers and copy files using client
4. Ship back the device -> AWS facility
5. Data will be loaded into S3 bucket
6. Snowball is completely wiped

#### Pricing
1. Pay for device usage and data transfer out of AWS
2. Data transfer IN to Amazon S3 -> Free
3. On-Demand
	1. Includes 1 time service fee per job
		1. 10 days usage for Snowball Edge Storage Optimized 80TB
		2. 15 days usage for Snowball Edge Storage Optimized 210TB
	2. Shipping days are NOT counted towards these durations (excluded)
	3. Pay per day for any additional days
4. Committed Upfront
	1. Pay in advance for monthly, 1 - year, and 3 - years of usage
	2. Up to 62% discounted pricing
