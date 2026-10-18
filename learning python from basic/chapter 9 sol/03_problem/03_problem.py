
for n in range(2,21):
    with open(f"Table{n}.txt","w") as table:
        for i in range(1,11):
            table.write(f"{n} X {i}= {i*n}\n")