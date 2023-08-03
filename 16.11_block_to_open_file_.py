# it works a read but dont required to close
with open("16.10_text_5_.txt") as f:
    a = f.readlines()
    print(a)

f2 = open("16.10_text_5_.txt","rt")
r = f2.readlines()
print(r)

f2.close()