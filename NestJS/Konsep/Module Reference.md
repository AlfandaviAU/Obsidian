Untuk mengambil data provider yang ada di aplikasi Nest -> tidak mau melakukan [[Dependency Injection]] secara otomatis -> secara <mark style="background: #FF5582A6;">manual</mark> 

<mark style="background: #FF5582A6;">Warning</mark> : Semua akan berjalan normal, sampai ada suatu error baru ketahuan

![[Pasted image 20240503104410.png|400]]

Jadi dia memanggil modul dia -> user module untuk diambil referensi, seperti Connection, MailService dll kemudian <mark style="background: #FF5582A6;">perlu dicek apakah ada atau tidaknya dulu</mark>, nanti malah error

![[Pasted image 20240503104616.png | 400]]
