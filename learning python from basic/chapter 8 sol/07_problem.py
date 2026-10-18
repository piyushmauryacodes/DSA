def remove(l,word):
    n=[]
    for item in l:
        if item!=word:
            n.append(item.strip(word))
    return n


l=["Harry", "Rohan","Subham","an"]
print(remove(l,"an"))