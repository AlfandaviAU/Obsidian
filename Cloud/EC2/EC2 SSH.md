[[EC2 (Elastic Compute Cloud)]] using mac, allow us to control remote machine using command line, using ssh port 22, make sure (.pem) file already on the directory

```
chmod 0400 EC2.pem
ssh -i EC2.pem ec2-user@18.136.201.164
```

![[Pasted image 20240904075927.png|400]]

We can use aws instance connect -> no need of uploading ssh keys.
If we using aws instance connect, dont ever store aws configure data inside, other user can access our credentials and using it.
So if we want our instance to get list users, just <mark style="background: #BBFABBA6;">attach IAM roles</mark> for it, like IAM list users

![[Pasted image 20240904083115.png|400]]
