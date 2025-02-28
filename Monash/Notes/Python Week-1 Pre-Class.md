##### TypeOf
1. list
2. str
3. int
4. float

##### Type Conversion
1. Integer rounding is always close to 0, i.e. 3.9999 -> 3 and -3.99999 -> -3
2. String parsing to integer int(string_here) -> can be used also for calc
3. Float parsing -> float(string_here) and type is float afterwards

##### Interpreter
`square(x + sub(square(y), 2 * x))`.

1. lookup square func
2. lookup x
3. lookup sub func
4. lookup square func again
5. lookup y
6. run square func on y
7. lookup x again
8. run 2 . x
9. run sub 
10. x + sub result
11. run square function

##### Order of Function
<mark style="background: #FF5582A6;">** Function -> RIGHTMOST FIRST TO BE DONE</mark>

is_digit() -> check if float or integer
![[Pasted image 20250225151718.png]]
