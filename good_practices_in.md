#   One Statement of Code per Line

##  Bad practice

```
print 'foo'; print 'bar'

if x == 1: print 'foo'

if <complex comparison> and <other complex comparison>:
    # do something
```

## Good Practice

```
print 'foo'
print 'bar'

if x == 1:
    print 'foo'

cond1 = <complex comparison>
cond2 = <other complex comparison>
if cond1 and cond2:
    # do something
```