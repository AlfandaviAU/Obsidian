Default return value yang diberikan di controller, akan jadi response body untuk HTTP response, namun kita bisa menggunakan express.Response atau <mark style="background: #FFF3A3A6;">@Res()</mark>, contohnya
![[Pasted image 20240429135203.png|400]]
![[Pasted image 20240429135642.png|350]]
![[Pasted image 20240429135834.png|350]]
##### Response Decorator
| Decorator                 | Utility                            |
| ------------------------- | ---------------------------------- |
| @HttpCode(code)           | Mengubah response status code      |
| @Header(key, value)       | Mengubah response header           |
| @Redirect(location, code) | Redirect ke lokasi yang diinginkan |
| @Next()                   | Untuk express.NestFunction         |
untuk redirect, kita bisa memanggilnya seperti ini
![[Pasted image 20240429140153.png|300]]
