1. Entity -> object of interest
2. Attributes -> Characteristics of Entities
	1. Required -> Must have value / cannot be empty
	2. Optional -> Does not require value / can be empty
3. Domain -> set of possible values for attribute
4. Composite primary key
	1. Backup of primary key if deleted![[Pasted image 20250313112846.png]]
5. Composite and Simple attributes
	1. composite attribute
		1. attribute that can subdivided into other attributes (address, phone number)
	2. simple attribute
		1. cannot be subdivided
6. Single Valued Attribute
	1. can only have single value like social security number
7. Multi Valued Attribute
	1. can have many values
	2. e.g. College degrees, different phone number

![[Pasted image 20250313125917.png]]
	Because there's no foreign key prof_id on class -> non identifying, so 1 to zero or many
8. Relationship
	1. a customer may generate many invoices
	2. each invoice is generated by one customer
		1. (relationship is one to many 1:M)
		2. should ask question if we only know 1 direction
9. 