Attack Network Drive to [[EC2 (Elastic Compute Cloud)]],  [[EBS (Elastic Block Store)]] are network drives with good but <mark style="background: #FF5582A6;">limited</mark> performances. To solve this, if we need <mark style="background: #BBFABBA6;">high-performance hardware disk</mark>, we use EC2 Instance Store
1. Better I/O performance (Very High IOPS up to 1.4 - 3.3million IOPS)
2. Lose storage if stopped
3. Good for buffer / cache / temporary content
4. Risk of data loss if hardware fails
Make sure to backup data to anticipate fails

