1. Normalization
	1. Partial Dependency
		1. (A,B) -> (C,D)
		2. B -> C
		3. (A,B) is primary key
		4. Then B -> C is <mark style="background: #FFFF00;">partial dependency</mark>
	2. Transitive Dependency
		1. X -> Y
		2. Y -> Z
		3. (X) is primary key
		4. X -> Z is <mark style="background: #FFFF00;">transitive dependency</mark>
#### Normal Forms
![[Pasted image 20250327113613.png]]
1. Conversion to First Normal Form (1NF)
	1. PROJ_NUM -> PROJ_NAME
	2. EMP_NUM -> EMP_NUM, JOB_CLASS, CHG_HOUR
	3. JOB_CLASS -> CHG_HOUR

	1NF (<u>PROJ_NUM</u>, <u>EMP_NUM</u>, PROJ_NAME, EMP_NAME, JOB_CLASS, CHG_HOURS, HOURS)
	**<mark style="background: #FFFF00;">PARTIAL DEPENDENCIES :</mark>**
		(PROJ_NUM -> PROJ_NAME)
		(EMP_NUM -> EMP_NAME, JOB_CLASS, HOURS)
	**<mark style="background: #FFFF00;">TRANSITIVE DEPENDENCIES :</mark>**
		(JOB_CLASS -> CHG_HOURS)
	they remove the repeating groups