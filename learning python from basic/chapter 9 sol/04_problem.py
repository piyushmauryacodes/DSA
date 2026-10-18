word="Donkey".lower()

with open("04_file.txt","r") as f:
    content=f.read().lower()
New_content=content.replace(word,"#####")

with open("04_file.txt","w") as f:
    f.write(New_content)