import pickle

with open('/tmp/data', 'wb') as f1:
    shopping_list = ['egg', 'apple', 'banana']
    pickle.dump(shopping_list, f1)

with open('/tmp/data', 'rb') as f2:
    mylist = pickle.load(f2)

print(mylist)

