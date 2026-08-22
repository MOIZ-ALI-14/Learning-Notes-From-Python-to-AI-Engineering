def tables(n):
    with open(f"chapter 09/Tables/Table_{n}.txt", "w") as f:
        for i in range(1, 11):
            table = f"{n}X{i}={n*i}\n"
            f.write(table)


for i in range(2, 21):
    tables(i)
