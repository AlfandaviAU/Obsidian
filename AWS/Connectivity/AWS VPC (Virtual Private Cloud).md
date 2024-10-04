[[AWS (Amazon Web Services)]]
![[Pasted image 20230928130020.png|500]]
VPC untuk memisahkan antara instances yang privat dengan konten publik yang bisa dilihat orang lain. Gateway disediakan untuk mengakses instances tersebut

###### Virtual Private Gateway
![[Pasted image 20230928130328.png|500]]
Jadi hanya jaringan yang diizinkan saja yang bisa mengakses, dibuat dengan VPN agar tidak sembarangan orang bisa masuk

[[AWS VPC (Virtual Private Cloud)]]
[[AWS Direct Connect]]

##### Subnet
![[Pasted image 20230928130948.png|300]]
Pengelopokkan resources berdasarkan keamanan ataupun kebutuhan operasional, bisa dipisahkan visibilitasnya. Dan bisa diatur untuk saling berkomunikasi didalam VPC yang sama.

##### Network Access Control List
![[Pasted image 20230928132430.png]]
Firewall yang mengatur siapa saja yang boleh masuk dan mengakses resources pada VPC

##### Security Group
![[Pasted image 20230928132935.png|500]]
Pada satu subnet memiliki beberapa security group, nah di security group ini melindungin instances yang dimiliki didalamnya -> lebih ke firewall untuk mengontrol traffic EC2 instances -> otomatis dilindungi ketika launch

By Default menolak semua traffic masuk, namun allow semua traffic keluar. Semua port dan IP address yg mau masuk akan diblokir, sehingga bisa diconfig buat siapa aja yang boleh masuk

Security group ngecek siapa yang masuk, namun kalau siapa yang keluar maka dibiarkan -> mirip satpam maupun bioskop

| Network ACL | Security Group                                |
| ----------- | --------------------------------------------- |
| Stateless   | Stateful, mengingat siapa yg masuk dan keluar |

##### Journey Paket antar Subnet pada VPC
![[Pasted image 20230928133911.png|500]]
![[Pasted image 20230928133918.png|500]]
![[Pasted image 20230928133921.png|500]]
![[Pasted image 20230928133924.png|500]]
![[Pasted image 20230928133927.png|500]]