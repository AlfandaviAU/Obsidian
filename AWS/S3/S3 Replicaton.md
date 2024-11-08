[[S3 (Simple Storage Service)]] Replication Cross Region Replication (CRR) & Same Region Replication (SRR)
1. Can setup async replication within/cross region bucket
2. Buckets can be in different AWS accounts
3. Need proper IAM permissions to S3
4. Use cases :
	1. CRR - compliance, lower latency access, replicaton accross accounts
	2. SRR - log aggregation, live replication between production and test accounts (have its own test env)
	
Replication rules from source bucket -> directed to destination bucket