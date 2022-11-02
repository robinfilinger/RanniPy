import pyodbc 

conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=DESKTOP-SQR7QOT\SQLEXPRESS;"
                        "Database=Cooking;"
                        "Trusted_Connection=yes")

def addRecipe(RecipeName, cooking, status):
    print("add recipe")
    print(RecipeName)
    cursor = conn.cursor()
    cursor.execute('insert into Recipes(RecipeName,Cook,Status) values(?,?,?);', (RecipeName,cooking,status))

def addIngredient():
    print("add ingredient")




def read():
    hello = ""
    print("read")
    cursor = conn.cursor()
    cursor.execute('select * from Recipes')
    for row in cursor:
        print (f'row = {row}')
        print (row[1])
        hello = hello + row[1]
    print(hello)
    return hello

conn.close()