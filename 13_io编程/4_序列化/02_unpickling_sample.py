import pickle

with open("dump.txt",'rb')as file:
    print(pickle.load(file))