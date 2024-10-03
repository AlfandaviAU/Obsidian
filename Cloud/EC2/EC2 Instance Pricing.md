[[EC2 (Elastic Compute Cloud)]]
1. **On-Demand Instances** : short workload, predictable pricing, pay by second
	1. Pay for what you use
	2. Highest cost but no upfront payment
	3. No long-term commitment
	4. Recommended for <mark style="background: #BBFABBA6;">short-term</mark> and <mark style="background: #BBFABBA6;">un-interrupted workloads</mark>
	
2. **Reserved** ( 1 & 3 Years ) : long workloads, can be convertible
	1. Up to <mark style="background: #BBFABBA6;">72% discount</mark> compared to On-demand
	2. Reserve specific instance attributes ( Instance Type, Region, Tenancy, OS )
	3. Reservation Period
		1. 1 Year ( + discount )
		2. 3 Years ( +++ discount )
	4. Payment Options
		1. No Upfront ( + )
		2. Patrial Upfront ( ++ )
		3. All Upfront ( +++ )
	5. Reserved Instance's Scope
		1. Regional
		2. Zonal
	6. Recommended for DB
	7. Can buy and sell in <mark style="background: #FFB86CA6;">Reserved Instance Marketplace</mark>
	8. Convertible Reserved Instance
		1. Allows change EC2 instance type, family, OS, scope, and tenancy
		2. Up to <mark style="background: #BBFABBA6;">66% discount</mark>

3. **Saving Plans** ( 1 & 3 Years ) : commitment to an amount of usage, long workload
	1. Discount based on long-term usage, same like Reserved Instances
	2. Commit to certain type of usage ( $10/h for 1 or 3 years )
	3. Usage beyond EC2 Saving Plans will billed at <mark style="background: #FF5582A6;">On-Demand price</mark>
	4. Locked to specific instance family & region ( M5 in us-east-1)
	5. Flexible across:
		1. Instance Size ( M5.xlarge and M5.2xlarge)
		2. OS
		3. Tenancy

4. **Spot Instances** : short workload, cheap, can lose instances
	1. Discount up to 90% compared to on-demand
	2. Bidding max price we willing to pay
	3. Can lose instance if our max price < current spot price
	4. <mark style="background: #BBFABBA6;">Most cost-efficient instance iN AWS</mark>
	5. Useful use cases : 
		1. Batch jobs
		2. Data analysis
		3. Image processing
		4. Any distributed workloads
		5. Workloads with flexible start and end time
	6. <mark style="background: #FF5582A6;">Not suitable for critical jobs or DB</mark>
	
5. **Dedicated Host** -> Book entire physical server
	1. Physical server with EC2 instance capacity fully dedicated for us
	2. Allow us to address compliance requirements, using our server-bound software licences
	3. Purchasing Options:
		1. On-demand
		2. Reserved
	4. Most expensive options -> cause of renting 1 whole physical server
	5. Useful for software that have complicated licensing model ( bring your own license ) or some companies that have strong regulatory and compliance
	
6. **Dedicated Instances** -> Book entire hardware, not sharing with others
	1. Instance run on hardware that dedicated to us
	2. Share hardware with other instances
	3. No control over instance placement

7. **Capacity Reservations** -> Reserve capacity in specific for any duration
	1. Reserve on-demand instances capacity for any duration
	2. Always have access to EC2 capacity when we need it
	3. <mark style="background: #FF5582A6;">No time commmitment, no billing discounts</mark>
	4. To get billing discounts -> combine with regional reserved instances and saving plans
	5. Charged at On-Demand rate even we not using it
	6. Suitable for short-term, <mark style="background: #BBFABBA6;">uninterrupted</mark> workloads, that need to be done



##### When to use Reserved Instances vs Saving Plans?
1. Reserved instances locked at same Region and Instance family
2. RI is commitment to use an instance  at particular price for specific period
	1. it means that we want to use machine a, for 10 bucks, for 1 year, whether i use it or not
3. Saving Plans is commitment to spend particular dollar amount per hour for specific period
	1. it means that we want to spend 10bucks for any machine, for 1 year

##### Dedicated Instances vs Dedicated Host
![[Pasted image 20240904090452.png|300]]
Key notes : dedicated host -> we buy the whole racks, and dedicated instances -> we buy the instances i.e. 1 hardware and if we stop using it, we may use another hardware, but private use