konsep dimana suatu object membutuhkan object lain, tinggal ditamhakan provider yang dibutuhkan pada constructor, contohnya

![[Pasted image 20240503092023.png|500]]
Dia memanggil constructor, init service dari UserService, dan nanti servicenya dipanggil pada controller yang diinginkan
![[Pasted image 20240503092452.png|400]]
Dan jangan lupa menambahkan providers dari service yang digunakan pada unit testing, agar referensinya tidak bingung

![[Optional Dependency]]
