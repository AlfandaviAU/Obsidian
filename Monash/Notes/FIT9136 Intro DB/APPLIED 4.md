![[Pasted image 20250409124542.png|500]]
1. List the number and name for all hotels
$$
\pi_{hotel\_no, hotel\_name}\ (HOTEL)    
$$
2. List all single rooms with a price below $50
$$
\sigma_{room\_type='single' \  \land \  room\_price < 50}(ROOM)    
$$
3. List the numbers and names of all hotels in Melbourne$$
    \pi_{hotel\_no, hotel\_name}(\sigma_{hotel\_city='melbourne'}\ (HOTEL))
    $$
4. List all numbers and names of hotels which have a presidential suite room
$$
PSUITE\_NO =  \pi_{hotel\_no}(\sigma_{room\_type = 'presidential\ suite'}(ROOM))
$$
$$
R = PSUITE\_NO \bowtie (\pi_{hotel\_no, hotel\_name}(HOTEL))
$$
5. List the price and type of all rooms at the Grosvenor Hotel
$$
A = \pi_{hotel\_no}(\sigma_{hotel\_name='Grosvenor\ Hotel'}(HOTEL)

$$
$$
B = \pi_{hotel\_no, room\_price, room\_type}(ROOM)
$$
$$
R = \pi_{room\_price, room\_type}(A\bowtie B)
$$
6. List all numbers, names, and addresses of guests currently staying in deluxe room of any hotel (assume that if the guest has a tuple in the BOOKING relation, then they are currently staying in the hotel)
$$
A = \pi_{room\_no}(\sigma_{room\_type='deluxe\ room'}(ROOM))
$$
$$
B = \pi_{guest\_no, room\_no}(BOOKING)
$$
$$
C = \pi_{guest\_no, guest\_name, guest\_address}(GUEST)
$$
$$
R = \pi_{guest\_no, guest\_name, guest\_address}((A\bowtie B) \bowtie C)
$$
	    
7. List all numbers, names, and addresses of guests currently staying at the Grosvenor Hotel (assume that if the guest has a tuple in the BOOKING relation, then they are currently staying in the hotel)
$$
A = \pi_{hotel\_no}(\sigma_{hotel\_name='Grosvenor\ Hotel'}(HOTEL))
$$
$$
B = \pi_{hotel\_no, guest\_no}(BOOKING)
$$
$$
C = \pi_{guest\_no, guest\_name, guest\_address}(GUEST)
$$
$$
R = \pi_{guest\_no, guest\_name, guest\_address}((A\bowtie B)\bowtie C)
$$

##### ADDITIONAL EXERCISE
![[Pasted image 20250409144049.png|600]]
1. List ids, names of customers and descriptions of products bought by the customer. How many tuples will be returned by the relational algebra query that you have constructed as your answer?
$$
R1 = \pi_{cust\_id, cust\_name}(CUSTOMER)
$$
$$
R2 = \pi_{cust\_id,prod\_id}(SALE)
$$
$$
R3 = \pi_{prod\_id, prod\_desc}(PRODUCT)
$$
$$
R = \pi_{cust\_id, cust\_name, prod\_desc}((R1 \bowtie R2) \bowtie R3)
$$
2. List all names which are shared by customers and staff
	$$
	R1 = \pi_{cust\_name}(CUSTOMER)
	$$
	$$
	R2 = \pi_{staff\_name}(STAFF)
	$$$$
	R = R1 \cap R2
	$$
3. List ids and descriptions of products that haven’t been sold
	$$
	R1 = \pi_{prod\_id, prod\_desc}(PRODUCT)
	$$
	$$
	R2 = \pi_{prod\_id}(SALE)
	$$
	$$
	R3 = \pi_{prod\_id, prod\_desc}(R1 \bowtie R2)
	$$
	$$
	R = R1-R3$$
4. List names of clerks who don’t have any sales yet
$$
\pi_{staff\_name}(\sigma_{staff\_position='clerk}(STAFF)) - \pi_{sold\_by}(SALE)
$$
5. List categories (positions) of staff who have made sales
$$
\pi_{staff\_position}(\sigma_{staff\_name=sold\_by}\   (STAFF \bowtie SALE))
$$
