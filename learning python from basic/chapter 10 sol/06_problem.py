class change:
    


    def __init__(harry,name,age,language):
        print(harry,type(harry))
        harry.name=name 
        harry.age=age
        harry.language=language
        print(f"The name is {harry.name} age - {harry.age} and learning {harry.language}")

    def trying_harry_with_self(harry,name,title):
        print(f"{name} {title} is a very good coder.")


Harry=change("Piyush",24,"Python")
Harry.trying_harry_with_self("Rahul","Kumar")

                    #OR

change.trying_harry_with_self(Harry, "Rahul","Kumar")