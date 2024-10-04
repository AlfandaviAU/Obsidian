Cara mengakses AWS ada 3 options:
1. AWS Management Console (protect by password and MFA)
2. AWS CLI (protect by access keys)
3. AWS SDK (protect by access keys)

Access Keys generated dari AWS Console, 1 user 1 access keys
<mark style="background: #FF5582A6;">Tidak disarankan untuk root user access keys</mark>

IAM Roles for Services -> Bisa diatur untuk mengakses services tertentu
EC2 Instance Roles, Lambda Roles, etc