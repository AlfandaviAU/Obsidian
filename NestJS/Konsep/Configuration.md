Memerluka config file yang dinamic, kita bisa menggunakan .env -> bisa dibaca secara otomatis tanpa perlu setting2

<mark style="background: #FF5582A6;">ENV DILUAR SRC!!!!</mark>

<mark style="background: #BBFABBA6;">npm install @nestjs/config</mark>

Kemudian diimport di app.module sebagai ConfigModule
![[Pasted image 20240503105257.png|300]]

Contoh pemanggilan .env variables
![[Pasted image 20240503105750.png|500]]
dan nanti tinggal diubah saja yang di user module
![[Pasted image 20240503110033.png|200]]

Untuk ganti port dan main.ts setting, bisa pakai ini
![[Pasted image 20240503110613.png|500]]
