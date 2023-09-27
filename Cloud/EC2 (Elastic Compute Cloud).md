[[AWS (Amazon Web Services)]]
- Menyediakan layanan computation sesuai kebutuhan bisnis
- Bisa berubah  ukurannya di cloud, sehingga dinamis
- Kalau sudah selesai, instance bisa diakhiri
- Berbagi instance dengan instance lainnya
- Scaling, milih OS dengan mudah

#### Instance Family
1. General purpose : umum, buat server web atau repo
2. Compute optimized : komputasi berat, untuk game, modeling
3. Memory optimized : memproses data besar -> db
4. Accelerated computing : Machine learning -> akselerasi
5. Storage optimized : read dan write yang tinggi, like sister

#### Harga EC2
1. On Demand : Selama instance berjalan
2. Saving Plans : Jangka waktu yang lama
3. Reserved Instances 
	1. Standard 
	2. Convertible
	3. Scheduled

##### EC2 Auto Scaling
Otomatis menyesuaikan kebutuhan akan komputasi
1. Dynamic scaling -> Respon terhadap permintaan
2. Predictive scaling -> Dijadwalkan EC2 yg dibutuhkan

Tipe scaling : 
1. Scaling up -> memperbesar instances (1 to 10)
2. Scaling down -> mengecilkan instances (10 to 1)
3. Scaling out -> memperbanyak instances (1 to 1,1,1)    
4. Scaling in -> mengurangi instances (1,1,1 to 1)

Decouple system : Dipisahkan sistemnya antar proses sehingga scaling bisa dimudahkan 
