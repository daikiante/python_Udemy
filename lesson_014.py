# for

some_list = [1,2,3,4,5]

'''
whileで書いた場合

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

'''

# forで書いた場合

for i in some_list:
    print(i)





# for else

for fruits in ['apple','banana','orange']:
    # if fruits == 'banana':
        # print('stop eating')
        # break
    print(fruits)
else:
    print('I eat all!!')




# range()

'''
リストを作ってforループを処理する場合

num_list = [0,1,2,3,4,5,6,7,8,9]
for i in num_list:
    print(i)

'''

for i in range(2,10,3):
    print(i)



# enumerate()

for i,fruit in enumerate(['apple','banana','orange']):
    print(i,fruit)



# zip()

days = ['mon','Tue','Wed']
fruits = ['apple','banana','orange']
drinks = ['coffe','tea','beer']

for day,fruit,drink in zip(days,fruits,drinks):
    print(day,fruit,drink)




# items() dictをforループで回す
d = {'x':100,'y':200}

print(d.items())

for k , v in d.items():
    print(k ,':',v)