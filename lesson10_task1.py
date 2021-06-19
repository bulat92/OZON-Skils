import copy

animals = ['питон', 'питон', 'кит', 'собака', 'питон', 'кит', 'кошка', 'горилла', 'кит', 'кошка', 'жираф', 'леопард', 'жираф', 'жираф', 'кошка',
           'горилла', 'жираф', 'жираф', 'кошка', 'жираф', 'кошка', 'кошка', 'собака', 'кит','жираф', 'леопард', 'жираф', 'собака', 'кит', 'кит',
           'кит', 'жираф', 'собака', 'собака', 'кит', 'питон', 'леопард', 'кошка', 'жираф', 'собака', 'кошка', 'жираф', 'кошка', 'собака', 'кит',
           'леопард', 'леопард', 'горилла', 'горилла', 'кит']

p = lambda x: print(x)
animals2 = copy.copy(animals)

animals = [len(x) for x in animals] #comprehension

for i in animals:
    p(i)

p('animals2')

animals2 = map(lambda x: len(x), animals2) #map

for i in animals2:
    p(i)



