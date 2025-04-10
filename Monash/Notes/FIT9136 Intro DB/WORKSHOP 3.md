$$
\pi_{project\_manager}\ PRDETAIL
$$
$$
\sigma_{project\_code = 25-5A}\ PRDETAIL
$$
$$
\pi_{project\_manager}(\sigma_{project\_code = 25-5A} \ PRDETAIL)
$$
###### Show the name and dob of all black belt members
$$
\pi_{member\_name,\ member\_dob}(\sigma_{member\_belt = 'black'}\ MEMBER)
$$
###### Show the name, belt color and attendance dates of the member with an id of 12345
1. Inefficient Way
$$
\pi_{member\_name,\ member\_belt,\ attendance\_date}(\sigma_{member\_id=12345}\ MEMBER \bowtie ATTENDANCE)
$$
2. Efficient Way
$$
A2a = \pi_{member\_id, attendance\_date}(\sigma_{member\_id=12345}\ ATTENDANCE)
$$
$$
A2b = \pi_{member\_id, member\_name, member\_belt}(\sigma_{member\_id=12345}\ MEMBER)
$$
$$
R2  = \pi_{member\_name, member\_belt, attendance\_date}(A2a \bowtie A2b)
$$

###### Show the id, name and age level group name of members who were absent (did not attend any training) between 01-03-2021 and 31-03-2021 (inclusive).
$$
A3a = \pi_{member\_id, member\_name, group\_id}\ (MEMBER)
$$
$$
A3b1 = \pi_{member\_id, attendace\_date}\ (ATTENDANCE)
$$
$$
A3b = \pi_{member\_id}(\sigma_{attendance\_date >= 01-03-2021 and attendance\_date <= 31-03-2021} (A3b1))
$$
$$
A3c = A3a \bowtie A3b
$$
$$
A3d = A3a - A3c
$$
$$
R = \pi_{member\_id, member\_name, group\_name}\ (A3d \bowtie (\pi_{group\_id, group\_name}\ (GROUP)))
$$
