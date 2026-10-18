# f=open("poem.txt","r")
# T=f.readlines()
# count=0
# for i in range(len(T)):
#     if("Twinkle".lower in T[i].lower()):
#         print(T[i])
#         count+=1
#         print(f"Index: {i} Count: {count}")

# print(f"\n Total count: {count}")
# f.close()

with open("poem.txt") as f:
    T= f.readlines()
    count=0
    for i in range(len(T)):
        if("twinkle" in T[i].lower()):
            print("\n")
            t=T[i].split(" ")
            for j in range(len(t)):
                if("twinkle"==t[j].lower().replace(",", "").replace(".", "").replace("!", "")):
                    print(t[j].replace(",", "").replace(".", "").replace("!", ""))
                    count+=1
    print(count)
            