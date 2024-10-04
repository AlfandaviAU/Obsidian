[[EC2 (Elastic Compute Cloud)]] Elastic File System
1. Managed NFS ( Network File System), can be mounted on 100s EC2 <mark style="background: #FFF3A3A6;">( comparison EBS only 1 instances at 1 time )</mark>
2. Works only with EC2 Linux instances in Multiple Availability Zone
3. Highly available, scalable, expensive (3x EBS), pay per use, no capacity planning

##### EBS vs EFS
1. [[EBS (Elastic Block Store)]] volume can only have 1 instance, and 1 specific AZ. If we want to move to another AZ, we need to create [[EBS Snapshot]] and restore it on another AZ
2. [[EC2 EFS]] shared file with a lot of instances in all availability zone, can mount same EFS Mount Target, <mark style="background: #BBFABBA6;">"shared file system"</mark>
3.  