#### COPY
```python
from copy import copy


arr = [[1,2,3],[4,5,6]]
arr2 = copy(arr)

arr2[0][0] = 99

# maka, arr dan arr2 masi sama karena dia ga sampe dalem
# arr = [[99,2,3],[4,5,6]] = arr2
```

#### DEEPCOPY
```python
# bisa copy by value sampe dalem misalnya 
from copy import deepcopy

arr = [[1,2,3,4,5],[2,3,4,5,6]]
arr2 = deepcopy(arr)

arr2[0][0] = 99

# maka, arr dan arr2 itu uda beda jadi ga kena
# arr = [[1,2,3,4,5],[2,3,4,5,6]]
# arr2 = [[99,2,3,4,5],[2,3,4,5,6]]
```
