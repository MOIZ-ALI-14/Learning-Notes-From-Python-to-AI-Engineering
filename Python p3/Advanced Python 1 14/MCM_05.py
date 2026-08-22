#Multiple context manager
with open("Advanced Python 1 14/MCM1_05.txt", "r") as f1, open(
    "Advanced Python 1 14/MCM2_05.txt",
    "r",
) as f2:
    data1 = f1.read()
    data2 = f2.read()
    print(data1)
    print(data2)
