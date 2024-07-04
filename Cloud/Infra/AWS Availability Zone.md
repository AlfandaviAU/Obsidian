![[Pasted image 20230928050149.png|300]]

- Gabungan dari beberapa data center yang terpisahkan dengan daya, jaringan atau koneksinya
- Mencegah hilangnya koneksi apabila ada bencana alam
- Best practice bikin 2 availability zone di 1 region

Contohnya AWS Region Sydney: ap-southeast-2
{<mark style="background: #FF5582A6;">ap-southeast-2a</mark>, <mark style="background: #FFB86CA6;">ap-southeast-2b</mark>, <mark style="background: #FFF3A3A6;">ap-southeast-2c</mark>}

Availability zone saling terpisah satu sama lain, sehinga ketika ada bencana, maka tidak merusak AZ yang lainnya, namun saling terkoneksi satu sama lain

