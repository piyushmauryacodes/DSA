with open("08_this.txt") as f:
    content1=f.read()

with open("08_this_copy.txt") as f:
    content2=f.read()

if(content1==content2):
    print("Yest these files are identical")
else:
    print("No these file are not identical")