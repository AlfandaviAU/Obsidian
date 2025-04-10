
Given these two relations:

**CUSTOMER (cust_id, cust_name, cust_address)**

**ORDER (order_id, order_date, cust_id)**

If a customer may have any number of orders and each order is placed by a single customer, define the following terms _based on the above relations_:
1. Relation
	1. Customer
	2. Order
	
2. Relationships
	1. one-to-many (single customer can have multiple order)
    
3. Attribute
	2. **CUSTOMER (cust_id, cust_name, cust_address)**
	3. ORDER (order_id, order_date, cust_id)**
    
4. Domain
	1. customer name just name, address is address like street code, and etc
	2. order is just date and cust id
    
5. Tuple
	1. tuple data maybe? no tuple -> cause of no data
     
6. Degree and cardinality of a relation
	1. 3rd degree on both
	2. cardinality is 1..N (one to many)
    
7. Primary key and foreign key
	1. Primary key is cust_id
	2. Primary key is order_id and FK is cust_id

![[Database ER diagram (crow's foot) - Page 3 (2).png]]


ORDER (order_id, order_date, cust_id)
- order_id PK
- cust_id FK-> if we got customer relation

**ORDERLINE (order_id, prod_no, ol_qtyordered, ol_lineprice)**
- order_ID PK FK
- prod_no PK FK

**PRODUCT (prod_no, prod_desc, prod_unitprice)**
- prod_no PK



**APPOINTMENT (dentist_id, dentist_name, patient_id, patient_name, appointment_datetime, surgery_roomno)**

- superkey
- (dentist_id, appointment_datetime),  
	  (dentist_id, appointment_datetime, patient_id),  
	  (dentist_id, appointment_datetime, patient_name),  
	  (dentist_id, appointment_datetime, surgery_roomno),  
	  (dentist_id, appointment_datetime, patient_id, surgery_roomno),  
	  (dentist_id, appointment_datetime, patient_id, patient_name),  
	  (dentist_id, appointment_datetime, patient_id, patient_name, surgery_roomno),  
	  (dentist_id, appointment_datetime, patient_id, patient_name, surgery_roomno, dentist_name),  
  - (surgery_roomno, appointment_datetime),  
	  (surgery_roomno, appointment_datetime, dentist_id),  
	  (surgery_roomno, appointment_datetime, patient_id),  
	  (surgery_roomno, appointment_datetime, patient_name),  
	  (surgery_roomno, appointment_datetime, dentist_id, patient_id),  
	  (surgery_roomno, appointment_datetime, dentist_id, patient_name),  
	  (surgery_roomno, appointment_datetime, dentist_id, patient_id, patient_name),  
	  (surgery_roomno, appointment_datetime, dentist_id, patient_id, patient_name, dentist_name)  

- candidate key
	- dentist_id, appointment_datetime
	- patient_id, appointment_datetime
	- surgery_roomno, appointment_datetime
- primary key
		- dentist_id, appointment_datetime


#### 4.2.1 Hotel Exercises
$$
project (𝝿), select (𝛔), join (⨝)
$$
![[Pasted image 20250324090315.png | 500]]

1. List the number and name for all hotels
$$
\pi_{\text{hotel\_no},{\text{hotel\_name}}}(\text{hotel})
$$
2. List all single rooms with a price below $50$
$$
	\sigma_{\text{room\_type = 'single'} \ \land \   \text{room\_price} < 50}(room)
$$
3. List the numbers and names of all hotels in Melbourne
$$
\pi_{\text{hotel\_no}, \text{hotel\_name}}(\sigma_{\text{hotel\_city = 
'melbourne'}}(hotel))
$$
4. List all numbers and names of hotels which have a presidential suite room
$$
(\pi_{hotel\_no}(\sigma_{room\_type = 'presidential\  suite'}(ROOM))) \bowtie (\pi_{hotel\_no, hotel\_name}(HOTEL))
 $$
##### <mark style="background: #FF5582A6;">TODO HERE </mark>

5. List the price and type of all rooms at the Grosvenor Hotel
$$
\pi_{\text{room\_price, room\_type}}((ROOM) \bowtie_{room\_hotel\_no=hotel\_no} (\sigma_{\text{hotel\_name = 'Grosvenor Hotel'}}(HOTEL)))
$$
6. List all numbers, names, and addresses of guests currently staying in deluxe room of any hotel (assume that if the guest has a tuple in the BOOKING relation, then they are currently staying in the hotel)
$$
R = \sigma_{room\_type = 'Deluxe'}(ROOM)
$$
$$
B = BOOKING \bowtie_{\ booking\_room\_no = room\_no \  \land \ booking\_hotel\_no = room\_no}(R)
$$
$$
G = GUEST \bowtie_{guest\_no = booking\_guest\_no}(B)
$$
$$
\pi_{guest\_no,\ guest\_name,\ guest\_address}(G)
$$


7. List all numbers, names, and addresses of guests currently staying at the Grosvenor Hotel (assume that if the guest has a tuple in the BOOKING relation, then they are currently staying in the hotel)

$$
H = \sigma_{hotel\_name = 'Grosvenor Hotel'} (HOTEL) 
$$
$$
B = BOOKING \bowtie_{}
$$


#### A4-2.2. Relational Algebra
![[Pasted image 20250324093704.png | 300]]
![[Pasted image 20250324093407.png|400]]
![[Pasted image 20250324093438.png]]
1. List ids, names of customers and descriptions of products bought by the customer. How many tuples will be returned by the relational algebra query that you have constructed as your answer? 
$$ 
number\ 1 \ goes \ here
$$
2. List all names which are shared by customers and staff 
$$
(\pi_{cust\_name} (CUSTOMER)) \bowtie_{customer\_name = staff\_name} (\pi_{staff\_name}(STAFF))
$$
$$
\pi_{cust\_name}(customer) \land \pi_{staff\_name}(staff)
$$
3. List ids and descriptions of products that haven’t been sold