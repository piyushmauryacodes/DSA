count=1
with open("06_file.txt","r") as f:
    content=f.readlines()

for line in content:
    if("python" in line):
        print(f"python is on line number: {count}")
    count+=1

if(count==1):
    print("we don't find any word like python")
 