1. How much <mark style="background: #FF5582A6;">time</mark> does algorithm need to finish?
2. How much <mark style="background: #FF5582A6;">space</mark> does algorithm need for its computation?

##### BigO Notation
1. Upper bound of complexity -> worst case, quantify performance

| Notation     | Description       |
| ------------ | ----------------- |
| O(1)         | Constant Time     |
| O(log(n))    | Logarithmic Time  |
| O(n)         | Linear Time       |
| O(n log (n)) | Linearithmic time |
| O(n^2)       | Quadric Time      |
| O(n^3)       | Cubic Time        |
| O(b^n)       | Exponential Time  |
| O(n!)        | Factorial Time    |
$$
\begin{matrix}
O(n + c) = O(n) \\
O(cn) = O(n),c > 0 \\ \\
f(n) = 7 log(n)^3 +15n^2+2n^3+8\\
O(f(n)) = O(n^3)
\end{matrix}
$$
###### Examples
1. O(1) Constant Time
```c
i := 0
while i < 11 Do
	i = i + 1
```
2. O(n) Linear Time
```c
i := 0
while i < n Do
	i = i + 1

i := 0
while i < n Do
	i = i + 3
```
3. O(n^2) Quadric Time
```c
For (i := 0; i < n; i = i + 1)
	For (j := 0; j < n; j = j + 1)

For (i := 0; i < n; i = i + 1)
	For (j := i; j < n; j = j + 1)
```
$$
\begin{matrix}
On\ second\ loop\\
(n) + (n-1) + (n-2)+ (n-3)+...+3+2+1\\
\\ Result\ will\ be,\ n(n+1)/2\\
O(n(n+1)/2) = O(n^2+n/2) = O(n^2)
\end{matrix}
$$
