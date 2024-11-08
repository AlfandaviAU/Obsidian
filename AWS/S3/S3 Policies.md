[[AWS/S3/S3 Buckets|S3 Buckets]] policies
![[Pasted image 20241026144002.png]]
1. JSON based policies 
	1. Resources : buckets and objects
	2. Effect : Allow / Deny
	3. Actions : Set of API to Allow or Deny
	4. Principal : Which account will rules applied to
2. Use S3 bucket policy to : 
	1. Grant public access to the bucket
	2. Force objects to be encrypted at upload
	3. Grant access to another account
	
![[Bucket Policy s3 public access]]

1. S3 can host static website and have them accessible on the internet
2. URL will depends on region