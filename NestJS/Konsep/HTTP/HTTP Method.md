Membuat routing di nest, kita tinggal menambahkan decorator HTTP method yang ingin digunakan, tinggal dibuat methodnya saja

@Get(path)
@Post(path)
@Put(path)
@Delete(path)
@Patch(path)
@Head(path)
@Options(path)
@All(path) -> menerima semua HTTP method

![[Pasted image 20240429131642.png|500]]

<mark style="background: #FFF3A3A6;">post()</mark> akan dipanggil ketika post api ke /api/users dipanggil 
<mark style="background: #BBFABBA6;">get()</mark> akan dipanggil ketika get api ke /api/users/sample dipanggil