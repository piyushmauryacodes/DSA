word="python"

with open("06_file.txt","r") as f:
    content=f.read()
if(word in content):
    print("Yes python is present.")
else:
    print("Python is not present.")