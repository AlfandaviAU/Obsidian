Cookie tidak didukung langsung oleh express, sehingga kita perlu library tambahan seperti cookie-parser, dan nanti ditambahin ke main.ts

![[Pasted image 20240429141554.png|400]]

nanti dimasukkan ke main.ts, dan app use cookie parser
![[Pasted image 20240429141727.png|400]]

Karena cookie ini bawaan express, maka mau tidak mau harus ambil response punya express, kita bisa set and get seperti berikut
![[Pasted image 20240429142107.png|500]]
