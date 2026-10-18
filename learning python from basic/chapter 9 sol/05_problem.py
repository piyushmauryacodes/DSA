words=["bad","ganda","Donkey"]

with open("04_file.txt","r") as f:
     content=f.read().lower()

for word in words:
        word=word.lower()
        content=content.replace(word,"#"*len(word))

with open("04_file.txt","w") as f:
    f.write(content)