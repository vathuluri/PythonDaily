import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result_overlap = [i for i in set(a) if i in b]
result = []
for element in result_overlap:
  if element not in result:
    result.appent(element)