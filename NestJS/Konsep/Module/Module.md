Konsep modular untuk membagi beberapa module, 1 module utama melakukan import beberapa modul dibawahnya, saat dibuat pertama kali, hanya ada 1 default module (App)
<div style="width: 800px;"> <!-- Adjust the width as needed --> <div class="mermaid"> <!-- Mermaid diagram code goes here --> </div> </div>
  

```mermaid

flowchart TD

style Application_ fill:#f9d5e5,color:#333,stroke:#b56576,stroke-width:2px

style Users_ fill:#f4acea,color:#333,stroke:#b56576,stroke-width:2px

style Orders_ fill:#f4acea,color:#333,stroke:#b56576,stroke-width:2px

style Products_ fill:#f4acea,color:#333,stroke:#b56576,stroke-width:2px

style Order_Details_ fill:#e0bbe4,color:#333,stroke:#957dad,stroke-width:2px

style Order_History_ fill:#e0bbe4,color:#333,stroke:#957dad,stroke-width:2px

style Product_Search_ fill:#e0bbe4,color:#333,stroke:#957dad,stroke-width:2px

  

Application_[Application ] --> Users_[Users ]

Application_ --> Orders_[Orders ]

Application_ --> Products_[Products ]

Orders_ --> Order_Details_[Order Details ]

Orders_ --> Order_History_[Order History ]

Products_ --> Product_Search_[Product Search ]

  

```
Disini kita bisa memiliki <mark style="background: #FFF3A3A6;">1 root module (App) dan tinggal import beberapa modul dibawahnya</mark> saja, yang mana membuat manajemen filenya lebih enak dilihat, jadi tidak pakai layering

![[Pasted image 20240429115516.png|500]]
Disini kita bisa menentukan mau import modul apa saja, cara generate modul user bisa dilihat pada [[Commands]]