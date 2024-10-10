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

![[Pasted image 20241010173621.png|400]]