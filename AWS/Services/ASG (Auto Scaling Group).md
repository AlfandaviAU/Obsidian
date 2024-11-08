[[AWS (Amazon Web Services)]] service, grouped with [[ELB (Elastic Load Balancer)]] 
	- Load of our website can change overtime, small load during day, more load at night
- Goal ASG :
	- Scale out -> Add EC2 instances
	- Scale in -> Remove EC2 instances
	- Ensure we have min & max number of machines
	- Auto register instances to load balancer
	- Replace unhealthy instances
- Benefit on Cost Savings: only run at optimal capacity

##### ASG AWS
1. Minimum size
2. Actual Size / Desired Capacity
3. Maximum size
Scale out as needed

Web traffic come to Load Balancer -> Auto assigned to EC2 instances, until max number of instances

![[Auto Scaling Groups|600]]

##### ASG - Scaling Strategies
1. Manual Scaling : Update size of ASG manually
2. Dynamic Scaling : Respond to changing demand
	1. Simple / Step Scaling
		1. When CloudWatch alarm triggered (if CPU > 70%), then add n-units
		2. When CloudWatch alarm triggered (if CPU < 30), then remove n-units
	2. Target Tracking Scaling
		1. Set Average ASG CPU to stay ~40%
	3. Scheduled Scaling
		1. Anticipate based on usage patterns
		2. Example: increase min capacity at friday evening to 10
3. Predictive Scaling : Use ML to predict future traffic (forecasting)
	1. Auto provision right number of EC2 in advances
	2. Useful when load has predictable patterns