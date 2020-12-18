import pickle
friends = {'dan': [20, 'London', 223432], 'Maria': [25, 'Madrid', 423789]}
with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)
with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)
