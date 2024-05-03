Class yang menggunakan decorator <mark style="background: #FFF3A3A6;">@Controller</mark>
Memproses HTTP Request yang masuk dan mengembalikan HTTP Response
Perlu diregistrasikan terlebih dahulu pada module dan prefix pathnya, seperti <mark style="background: #BBFABBA6;">@Controller("/api/users")</mark>

Generatenya bisa menggunakan [[Commands]], contohnya
![[Pasted image 20240429130909.png|400]]
khusus controller, dia dibuatkan unit testnya sekalian menggunakan jest