# # Using pickle module we can Store any object or any data (in there original type ) in a file  .

# # To store in a file , we require to open a file in binary mode for any opertion


import pickle


l = {'name': 'John', 'age': 30, 'city': 'New York','exp': '3 years'}
print(l)
op2 = open("t1.txt", "wb")
pickle.dump(l, op2)
op2.close()

op = open("t1.txt", "rb")
rd = pickle.load(op)
print(dict(rd))
op.close()




# Data to be pickled
# data = {'name': 'John', 'age': 30, 'city': 'New York'}

# # Pickling the data and writing it to a file
# with open('data.pkl', 'wb') as file:
#     pickle.dump(data, file)

# # Unpickling the data from the file
# with open('data.pkl', 'rb') as file:
#     loaded_data = pickle.load(file)

# print(loaded_data)


