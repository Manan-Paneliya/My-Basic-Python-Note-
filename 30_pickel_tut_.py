import pickle

inp = input("E")
inp2 = input("E")
l = [[inp, inp2], ]
op = open("t1.txt", "rb")
op2 = open("t1.txt", "wb")
wt = pickle.dump(l, op2)
rd = pickle.load(op)
op.close()
op2.close()
