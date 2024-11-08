Multiple architectural choices
1. Read Replicas
	1. Some copies of RDS allow our app to read from this replica
	2. Can create up to 15 Read Replicas
	3. Writing data to main DB
2. Multi-AZ
	1. Failover in case of AZ outage
	2. Use failover DB to backup in case Main DB error
	3. Data is only read/written to main DB
	4. Can only have 1 other AZ as failover
3. Multi-Region
	1. Read replica but on another region
	2. Local performance for global reads
	3. Replication cost

![[Excalidraw/RDS Deployments|1000]]
