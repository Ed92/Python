num = 26
name = 'Erik'

print('My number is {one} and my name is {two}'.format(one=num, two=name))

print(name[2])


my_list = ['a', 'b', 'c']

my_list.append('d')

print(my_list)
print(my_list[0:3])


my_list[1] = 'cool'

print(my_list)

nest = [1,2,[3,4]]

print(nest)

print(nest[2])

print(nest[2][1])

nest = [1,2,3,[4,5,['target']]]

print(nest[3][2][0])


i = 1

while i < 5:
    print('i is: {}'.format(i))
    i += 1


x = [1,2,3,4]

out = [num**2 for num in x]

print(out)

def times2(var):return var*2

print(times2(5))

seq = [1,2,3,4,5]

print(list(map(times2, seq)))

print(list(filter(lambda num: num%2 == 0,seq)))


