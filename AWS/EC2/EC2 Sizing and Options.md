[[EC2 (Elastic Compute Cloud)]]
1. Operating system : Linux / MacOS / Windows
2. CPU
3. RAM
4. Storage
	1. Network-attached : EBS & EFS
	2. Hardware : EC2 Instance Store
5. Network : Speed and public IP
6. Firewall rules : security group
7. Bootstrap script : EC2 user data -> run at first launch

<mark style="background: #BBFABBA6;">Boostrapping</mark> -> script launch when machine starts (once) :
1. Install updates
2. Install software
3. Downloading common files
4. Anything script


###### EC2 User data -> Launch on first instance called

```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
```

```
#!/bin/bash 
apt update -y 
apt install -y apache2 
systemctl start apache2 
systemctl enable apache2 
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
```
