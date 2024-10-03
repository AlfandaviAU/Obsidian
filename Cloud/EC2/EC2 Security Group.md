
Security group control how traffic is allowid into or out of our [[EC2 (Elastic Compute Cloud)]] in [[AWS (Amazon Web Services)]] instances, only contain <mark style="background: #BBFABBA6;">allow</mark> rules, can reference by IP or security group. Control inbound, outbound traffic from EC2 -> act as firewall, regulates : 
1. Access to ports
2. Authorized IP ranges - IPv4 and IPv6
3. Control inbound network ( from others to instance )
4. Control outbound network ( from instance to others )

##### Security Group Tips
1. SG can be attached to multiple instances, and 1 instance can have multiple security groups
2. Locked down to a region / VPC combination ( move region -> make another security group)
3. Live <mark style="background: #BBFABBA6;">outside</mark> EC2, just a firewall, ec2 doesnt know it
4. 1 separate security group for ssh access
5. if <mark style="background: #FFB8EBA6;">not accessible ( timeout )</mark>, then it's a <mark style="background: #FFB8EBA6;">security group issue</mark>
6. if <mark style="background: #D2B3FFA6;">connection refused</mark>, then <mark style="background: #D2B3FFA6;">app error</mark> not security group
7. By default, all <mark style="background: #FF5582A6;">inbound</mark> traffic -> <mark style="background: #FF5582A6;">blocked</mark>
8. By default, all <mark style="background: #BBFABBA6;">outbound</mark> traffic -> <mark style="background: #BBFABBA6;">authorized</mark>

##### Classic Ports to know
1. 22 = SSH - log into a Linux instance
2. 21 = FTP - upload files into a file share
3. 22 = SFTP - upload files using SSH
4. 80 = HTTP - access unsecured websites
5. 443 = HTTPS - access secured websites
6. 3389 = RDP (Remote Desktop Protocol) - log into a windows instance

