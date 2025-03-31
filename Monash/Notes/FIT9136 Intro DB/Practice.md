1. Find the names of all red parts. $$
\pi_{pName}(\sigma_{colour = 'red'}(Parts))
$$
2. Find all prices for parts that are red or green. (A part may have different prices from different manufacturers.)$$
	\pi_{price}((\sigma_{color = 'red' \ V \ color='green'}\ Parts) \bowtie Catalog)
	$$
3. Find the sIDs of all suppliers who supply a part that is red or green.
$$
\pi_{sID}\ ((\sigma_{color='red' \ V \ color='green}\ Parts ) \bowtie Catalog)
$$
4. Find the names of all suppliers who supply a part that is red or green.
$$
\pi_{sName}\ (\pi_{sID}\ ((\sigma_{color='red' \ V \ color='green}\ Parts ) \bowtie Catalog) \bowtie Suppliers)
$$

![[Pasted image 20250330142410.png|300]]
1. Find the names and salaries of all bosses who have an employee earning more than 100. Hint: Below each subexpression, write the names of the attributes in the resulting relation.
$$
\pi_{name, salary}(\sigma_{boss = number} \ ((\pi_{boss} (\sigma_{number = employee} \ (\pi_{number}(\sigma_{salary > 100} \ Employee) \bowtie Supervises))) \bowtie Employee ))
$$
