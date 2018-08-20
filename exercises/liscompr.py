even = [i for i in range(10) if i % 2 == 0]
print(even)

numbers = range(10)

size = len(numbers)

evens = []

i = 0
while i < size:
    if i % 2 == 0:
        evens.append(i)
    i += 1

print(evens)

odd = [i for i in range(100) if i % 3 == 0]
print(odd)


i = 0
seq = ["one", "two", "three"]
for i, element in enumerate(seq):
    seq[i] = '%d: %s' % (i, seq[i])

print(seq)


def _treatment(pos, element):
    return '%d: %s' % (pos, element)

seq = ["one", "two", "three"]

seq2 = [_treatment(i, el) for i, el in enumerate(seq)]

print(seq2)
