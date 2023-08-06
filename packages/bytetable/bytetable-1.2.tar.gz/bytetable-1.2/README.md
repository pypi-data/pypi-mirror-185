[GitHub](https://github.com/Santuchin/bytetable)

Bytetable is a simple data table manager, create a table file defining their columns, and modify it

```
import bytetable as bt

tb = bt.table('./table.tb', id=None, name=str, age=None)

tb.add(id=0, name='test name', age=21)

for row in tb:
    print(row)

tb.save()
```

It also has a smaller data file for an object

```
import bytetable as bt

val = bt.value('./value.val', str) # the default codec is None, which stands for raw codec

val.obj = 'testing strings'

print(val.obj)

val.save()
```

You can combine it like this
```
import bytetable as bt

tb = bt.table('./table.tb', id=None, name=str, age=int)
val = bt.value('./value.val')

name = input('input your name: ')

age = ''

while not age.isdigit():
    age = input('input your age: ')

tb.add(id=val.obj, name=name, age=int(age))
val.obj += 1

print('after')

for row in tb:
    print(row)


tb.save()
val.save()
```