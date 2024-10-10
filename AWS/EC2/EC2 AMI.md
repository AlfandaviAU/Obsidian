[[EC2 (Elastic Compute Cloud)]] instance customization -> software, config, os, monitoring
Benefit faster boot and config time, built for specific region and can be copied across region
We can launch EC2 from:
1. Public AMI :  From AWS
2. Our own AMI : From us
3. Marketplace AMI : third party / buy from others

##### Process
1. Start EC2 instance and customize it
2. Stop the instance
3. Build AMI -> create EBS snapshots
4. Launch instances from other AMI

AMI as templating from EC2, so we can just create from AMI, and do some functionality over it
we can like extend67