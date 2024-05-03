Memerluka config file yang dinamic, kita bisa menggunakan .env -> bisa dibaca secara otomatis tanpa perlu setting2

<mark style="background: #BBFABBA6;">npm install @nestjs/config</mark>

Kemudian diimport di app.module sebagai ConfigModule
![[Pasted image 20240503105257.png|300]]

Contoh pemanggilan .env variables
![[Pasted image 20240503105750.png|500]]
