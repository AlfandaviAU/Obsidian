Service on [[AWS (Amazon Web Services)]] to provide relational databases (like excel spreadsheets with links between them)
- AWS offers use ot manage different DB
- Benefits : 
	1. Quick Provisioning, High Availability, Scaling
	2. Automated Backup & Restore, Ops, Upgrades
	3. OS Patching
	4. Monitoring, alerting
- EC2 may run db, but we need to handle many things behind -> not efficient

##### Advantage Using RDS vs deploying DB on EC2
- RDS is managed service
	- Auto provisioning, OS patch
	- Cont backups, restore to timestamp
	- Monitoring Dashboards
	- Multi AZ for Disaster Recovery
	- Maintenance windows for upgrades
	- Scaling capability
	- Storage backed by EBS
<mark style="background: #FF5582A6;">- Cant SSH to our instances</mark>
![[Amazon RDS|500]]

##### Amazon Aurora
- Proprietary Tech from AWS
- PostgreSQL and MySQL supported
- Cloud optimized, 5x performance improvement on MySQL and 3x performance improvement on Postgres
- Storage automatically grows in increment of 10GB until 128TB
- Cost more than RDS (20%) - more efficient
- Not in free tier