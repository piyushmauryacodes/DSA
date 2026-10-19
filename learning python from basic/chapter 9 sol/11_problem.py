with open("11_python.txt","r") as f:
    content=f.read()

with open("11_renamed_by_python.txt","w") as f:
    f.write(content)