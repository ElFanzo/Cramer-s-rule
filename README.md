# Cramer-s-rule
Find the solution of a system of linear algebraic equations using Cramer's rule.

## Example
<b>SLAE</b>:<br>
| 2a + 5b + 4c = 30,<br>
| a + 3b + 2c = 150,<br>
| 2a + 10b + 9c = 110.
```python
from cramers_rule import solve

array_a = [
  [2, 5, 4],
  [1, 3, 2],
  [2, 10, 9],
]
array_b = [30, 150, 110]

print(solve(array_a, array_b))
# (-152, 270, -254)
```
a = -152, b = 270, c = -254.
