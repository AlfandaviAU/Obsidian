- Allow customers to store object (files) in "buckets"(directories)
- Bucket name must <mark style="background: #BBFABBA6;">globally unique name (accross all regions all accounts)</mark>
- Buckets are defined at region level
- Naming convention
	- No uppercase, no underscore
	- 3-63 characters long
	- Not an IP
	- Must start with lowercase letter and etc...
	
![[Excalidraw/S3 Buckets|S3 Buckets|300]]

Object have key, key -> full path (s3://my-bucket/my_file.txt)
##### Key : <mark style="background: #FFB86CA6;">prefix</mark> + <mark style="background: #BBFABBA6;">object name</mark>
##### s3://my-bucket/<mark style="background: #FFB86CA6;">folder1/folder2/</mark><mark style="background: #BBFABBA6;">file.txt</mark>

- Max object size 5TB
	- More than 5GB -> multt-part upload
- Metadata (list of text key / value pair for system info)
- Tags (Unicode key / value pair (up to 10)) for security / lifecycle
- Version ID (if using versioning)

##### S3 Presigned URL
URL contain signature that authorize who's using it with credentials encoded

##### S3 Security
1. User Based
	1. IAM Policies -> Which api calls that allowed
2. Resource Based
	1. Bucket Policies -> Which bucket allows
		1. Most Commonly Used
	2. Object Access Control List (ACL)
	3. Bucket Access Control List (ACL)
3. Encryption : encrypt object using keys
