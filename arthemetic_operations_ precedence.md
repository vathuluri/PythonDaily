||Operator|Description|
|----|----|----|
|lowest precedence|or	|Boolean OR|
||and	|Boolean AND|
||not	|Boolean NOT|
||==, |!=, <, <=, >, >=, is, is not	comparisons, identity|
|||	|bitwise OR|
||^	|bitwise XOR|
||&	|bitwise AND|
||<<, >>	|bit shifts|
||+, -	|addition, subtraction|
||*, /, //, %	|multiplication, division, floor division, modulo|
||+x, -x, ~x	|unary positive, unary negation, bitwise negation|
|highest precedence|**	|exponentiation|


#   Example 1

```
>>> 20 + 4 * 10
60
>>> (20 + 4) * 10
240

>>> 2 * 3 ** 4 * 5
810
>>> 2 * 3 ** (4 * 5)
6973568802
```