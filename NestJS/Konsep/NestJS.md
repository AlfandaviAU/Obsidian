### Core concept ![[nest.svg|20]]

- Framework untuk membuat aplikasi berbasis server dengan menggunakan NodeJS, bisa pakai TS(utamanya) dan tetep bisa pakai js biasa
- Framework yang cukup populer dikalangan programmer typescript
- https://nestjs.com/
- Kita butuh framework untuk menyamakan alur pekerjaan dan pengembangan aplikasi, biar ketika ada orang keluar masuk bisa dengan mudah menyesuaikan flownya
- Keuntungannya dengan menggunakan cara yang sama, no doubt lagi cara kerjanya dan adaptability dijamin
- Menggunakan [[Decorator]] sebagai penambah metadata
- Mempunyai [[Struktur Folder]]
- Memiliki [[Module]] yang mengandung beberapa [[Controller]] dan bisa [[Shared Module]]
- Controller untuk [[HTTP Request]] bisa memiliki beberapa [[HTTP Method]] yang terkait dan menghasilkan [[HTTP Response]] baik yang sync maupun [[Asynchronous]]
- Library seperti cookie parser bisa digunakan untuk mengaplikasikan [[Cookie]]
- Template engine seperti [[View]] diintegrasikan dengan ExpressJS seperti mustache
- Testing untuk [[Unit Test]] dan [[Integration Test]] menggunakan Jest
- Konsep seperti [[Provider]] tersedia pada NestJS, [[Dependency Injection]] beserta [[Optional Dependency]]
- [[Module Reference]] untuk refer ke Module lain
- Memiliki [[Configuration]] tersendiri
- [[Database]] di nest tidak mendukung ORM bawaan, namun bisa diintegrasikan dengan banyak ORM yang populer
### NestJS Internal
- NestJS sebenarnya pakai library yang disediakan di NodeJS
- Menggunakan ExpressJS sebagai HTTP Handlernya
- Menggunakan Jest sebagai unit testnya
- Bisa diintegrasikan dengan Prisma untuk DB nya
- Bisa diintegrasikan dengan Winston untuk loggingnya

