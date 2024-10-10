- Usually goes hand in hand with horizontal scaling
- Running app in at least 2 AZ, reduce effect of error
- Goal -> Minimize data loss

1. <mark style="background: #FFB86CA6;">Vertical Scaling</mark> Increase instance size
	1. From t2.nano to t2.large
2. <mark style="background: #FFF3A3A6;">Horizontal Scaling</mark> Increase number of instances
	1. Auto Scaling Group
	2. Load Balancer
3. <mark style="background: #BBFABBA6;">High Availability</mark> Run instances for the same app across multiple Availability Zone
	1. Auto Scaling Group multi AZ
	2. Load Balancer multi AZ
##### Scalability vs Elasticity vs Agility
Scalability: Ability to accommodate a larger load by make hardware stronger or adding nodes (scale up and scale out)

Elasticity: once system is scalable, some "auto-scaling" based on the load

Agility: How much time to make some resources available for developers from weeks to just minutes