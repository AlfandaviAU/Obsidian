[[EC2 (Elastic Compute Cloud)]]
Pemerataan traffic untuk instances biar tidak numpuk di 1 instances saja, agar tidak menganggur

Regional Construct : tingkat region -> highly available

![[Pasted image 20230927232152.png|500]]
Memudahkan untuk load balancing

#### Queuing
Menyediakan buffer untuk antrean -> queue, kalau sudah maka di pop sampai queue berakhir
[[Monolitik vs Microservices]]

#### Amazon SQS (Simple Queue Service)
Mengirim pesan antar komponen dengan payload dan dilindungi hingga terkirim, aplikasi A naruh ke queue, aplikasi B menyelesaikan queue

#### Amazon SNS (Simple Notification Service)
Sama seperti SQS namun bisa mengirimkan pesan notif ke pelanggan, dengan model *pub/sub*. Jadi ketika punya pesan bisa dipilih siapa saja yang bisa menerima pesan (endpoints)