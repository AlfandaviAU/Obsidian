Identity and Access Management, <mark style="background: #BBFABBA6;">Global Service</mark>
Root account already created by default, shouldn't be shared
Bisa create user, yang bisa di grouping

| Group: <mark style="background: #ADCCFFA6;">Developers</mark> | Group: <mark style="background: #FFB86CA6;">Operations</mark> | Group: <mark style="background: #BBFABBA6;">Audit Team</mark> |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| 1.  Alice                                                     | 1. David                                                      | 1. Charles                                                    |
| 2. Bob                                                        | 2. Edward                                                     | 2. David                                                      |
| 3. Charles                                                    |                                                               |                                                               |
<mark style="background: #FF5582A6;">Group only contain users, not other groups</mark>
 
User or Groups, bisa diatur pada JSON document bernama policies

![[Pasted image 20240616133401.png|300]]
Kita bisa define least privilege principle, jadi kalau gaperlu gausah dikasih -> Least Privillege Permissions

#### IAM Policies Inheritance

Jadi ketika kita punya 1 Group (Developer) yang berisi user Alice, Bob, Charles
Kita bisa apply policy ke group tersebut, dan membernya otomatis mendapatkan aksesnya

![[Pasted image 20240616152155.png|500]]
![[Pasted image 20240616152445.png|400]]

Contoh struktur IAM Policies:
1. Version
2. Id
3. Statement
	1. Sid : statement id
	2. Effect : Allow or Deny -> Whether statement allow or deny
	3. Principal : Account/user/role yang kena effect -> Which account will applied to
	4. Action: List aksi yang bisa dilakukan
	5. Resouce: Daftar resource yang terkena effect ini
	6. Condition: Kondisi untuk kapan policy in dijalankan

### IAM - Defense Mechanism
#### 1. IAM - Password Policy
1. Bisa setting minimum pass length, pola password, character khusus
2. Allow user untuk change password sendiri, dan bisa diatur expire date
3. Prevent previous password re-use

#### 2. IAM - MFA (Multi Factor Authentication)
Karena user punya access terhadap akun, kita harus menggunakan MFA device, karena resources itu bisa disalahgunakan

<mark style="background: #FFF3A3A6;">MFA</mark> = <mark style="background: #BBFABBA6;">password you know</mark> + <mark style="background: #FF5582A6;">security device you own</mark>

1. Virtual MFA Device (support multiple token on a single device)
	1. Google Authenticator
	2. Authy
2. U2F Security Key
	1. YubiKey -> 3rd party (Yubico)
3. Hardware Key Fob MFA Device
	1. Gemalto -> 3rd party
4. Hardware Key Fob for AWS GovCloud
	1. SurePassID -> 3rd party

Kalau Mac User -> Bisa pakai fingerprint untuk MFA -> iCloud Key Chain
Hacker meskipun bisa menebak password -> namun belum bisa dapet token dari MFA device

###### IAM - Credentials Report (account level)
Untuk list semua user pada akun tersebut dan statusnya
###### IAM - Access Advisor (user level)
Untuk list semua akses yang diberikan terhadap user dan kapan aja digunainnya -> bisa digunakan sebagai acuan revisi policies

#### IAM - Best Practices
1. Jangan gunakan AWS root account kecuali buat AWS setup aja
2. <mark style="background: #FF5582A6;">Satu orang satu akun AWS</mark>
3. Memasukkan orang ke grup, dan menambah permission ke grup tersebut
4. Membuat strong password policy
5. Menggunakan MFA
6. Membuat <mark style="background: #FF5582A6;">Role</mark> ketika memberikan akses service ke user
7. Gunakan <mark style="background: #FFF3A3A6;">Access Keys</mark> untuk CLI/SDK
8. Audit Permissions untuk akun menggunakan <mark style="background: #FFB86CA6;">IAM Credentials Report dan Access Advisor</mark>
9. Jangan pernah share IAM users dan Access Keys

#### Kewajiban Kita sebagai Pengguna IAM
1. Mengatur User, Grup, Role, Policies
2. Enable MFA untuk semua akun
3. Mengupayakan rotasi semua keys sesering mungkin
4. Menggunakan IAM tools untuk mengatur permissions
5. Analisa access patterns dan review permissions


[[AWS Access]]
