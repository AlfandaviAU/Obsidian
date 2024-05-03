Konsep yang sangat dasar di nest js, banyak class yang bisa dianggap sebagai provider, seperti Service, Repo, Factory, Helper, dll. Ide utama provider adalah agar object dari provider bisa diinject sebagai dependency ke object lainnya -> [[Dependency Injection]]


Provider bisa menggunakan class dengan decorator <mark style="background: #FFF3A3A6;">@Injectable</mark> dan bisa langsung saja command <mark style="background: #ADCCFFA6;">nest generate provider nama_path</mark> kalau service langsung nest generate service
