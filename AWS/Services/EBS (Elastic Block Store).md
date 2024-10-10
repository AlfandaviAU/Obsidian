[[AWS (Amazon Web Services)]] EC2 Storage Options

![[ebs2.drawio.png|400]]
1. Network drive that we can attach to our instances while running
2. Allow instances to persist data, even after termination
3. Only can be mounted at 1 instance at 1 time, but 1 instance can have more than 1 EBS -> EBS Female cant have more than 1 EC2
4. Bound to specific availability zone -> cant share across AZ
5. Network drive, use network to communicate the instance, can attached very quickly
6. To move volume across, we can snapshot it [[EBS Snapshot]]
7. Have provisioned capacity (size in GBs and IOPS), can increased later
8. Delete on termination ( root -> true, any other -> false)
