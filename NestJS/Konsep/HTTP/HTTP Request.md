- Saat membuat routing, kita ingin mendapatkan informasi yang dikirim oleh pengguna, seperti Query Param, Headers, Request Body, and etc
- Karena NestJS adalah Express, maka bisa menggunakan dekorator <mark style="background: #FFF3A3A6;">@Req()</mark>
- Langsung saja mengambil dekorator yang dibutuhkan

Meskipun bisa seperti begini,
![[Pasted image 20240429132626.png|300]]
namun lebih baik menggunakan dekorator berikut ini,

| **Decorator** | **Utility**      |
| ------------- | ---------------- |
| @Req()        | express.Request  |
| @Param(key?)  | req.params.key?  |
| @Body(key?)   | req.body.key?    |
| @Query(key?)  | req.query.key?   |
| @Header(key?) | req.headers.key? |
| @Ip           | req.ip           |
| @HostParam()  | req.hosts        |
![[Pasted image 20240429133439.png|400]]
![[Pasted image 20240429133915.png|400]]
Kita bisa ambil query paramsnya langsung tanpa bongkar bongkar request