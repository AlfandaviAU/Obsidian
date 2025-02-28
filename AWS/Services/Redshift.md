1. [[AWS (Amazon Web Services)]] services based on PostgreSQL but <mark style="background: #FF5582A6;">not used for OLTP</mark> (Online Transaction Processing)
2. <mark style="background: #BBFABBA6;">OLAP</mark> (Online analytical processing) -> analytics and data warehousing
3. Load data once / hour, 10x better performance
4. <mark style="background: #FFB86CA6;">Columnar</mark> storage of data, not row based
5. Massively Parallel Query Execution (MPP), highly available
6. Has SQL interface for performance queries
7. BI tools integration (AWS Quick sight or Tableau)

#### Redshift Serverless
1. Automatically provisions and scales data warehouse underlying capacity
2. Run analytics workloads without managing data warehouse infra
3. Pay for what we use
4. Use case : 
	1. Reporting
	2. Dashboard app
	3. Realtime analytics