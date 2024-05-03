Saat membuat provider, ada case dimana provider yang mau dibuat agak sedikit kompleks, sehingga tidak bisa hanya nyebutin nama classnya saja, atau bahkan tidak bisa hanya ditambahkan decorator <mark style="background: #FFF3A3A6;">@Injectable()</mark> 

#### 1. Standard Provider
![[Pasted image 20240503093141.png|200]]
#### 2. Class Provider
Membuat provider dengan menentukan class yang ingin digunakan, misalkan punya interface <mark style="background: #FFB8EBA6;">Connection</mark> dan class implementasi <mark style="background: #FF5582A6;">MySQLConnection</mark> dan <mark style="background: #FFB86CA6;">MongoDBConnection</mark>, kita bisa menentukan mau pakai yang mana

Langkah-langkahnya:
1. <mark style="background: #BBFABBA6;">nest generate provider connection user</mark>
2. set base dan 2 atau lebih injectable
![[Pasted image 20240503094112.png|300]]
3. tinggal panggil useClass untuk object connection yang telah dibuat sesuai kondisi yang diinginkan
![[Pasted image 20240503094208.png|400]]

Nanti di controller yang memanggil, tinggal dimasukkan dan dipanggil saja
![[Pasted image 20240503094413.png|250]]


#### 3. Value Provider
Membuat dependency dari value (object) yang usdah ada -> dijadikan dependency provider

Langkah-langkahnya:
1. <mark style="background: #BBFABBA6;">nest generate service mail user</mark>
2. Update mailservice
![[Pasted image 20240503095059.png|400]]
3. Update user module 
![[Pasted image 20240503095205.png|200]]
4. Dipanggil pada user controller untuk digunakan
![[Pasted image 20240503095401.png|300]]

#### 4. Factory Provider
Mekanisme pembuatan dependency, dengan menyediakan function ang bisa dipanggil untuk membuat object dependencynya -> generator

Langkah-langkahnya:
1. <mark style="background: #BBFABBA6;">nest generate provider user-repository user</mark>
2. Membuat factory pada provider yang diinginkan ![[Pasted image 20240503100844.png|500]]
3. Panggil useFactory dan jangan lupa inject dependency-nya ![[Pasted image 20240503101035.png|500]]


#### 5. Alias Provider
Membuat dependency dengan nama yang berbeda untuk object provider yang sama
<mark style="background: #FF5582A6;">Hanya beda nama saja</mark> 
![[Pasted image 20240503101932.png|200]]
![[Pasted image 20240503102118.png|400]]
