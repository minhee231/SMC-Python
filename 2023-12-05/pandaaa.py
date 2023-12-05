import pandas as pd

df = pd.DataFrame({'col':[1,2,3,4]})

#print(df)

mylist = []

for i in range(100):
    mylist.append(i)


df = pd.DataFrame({"se":mylist})

print(df)

df.to_excel("test.xlsx")