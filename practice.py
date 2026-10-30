import numpy as np 
import pandas as pd 
a = np.array([10,20,30,40])
print(a)
data = pd.DataFrame({
    "Name":["A","B","C"],
    "Marks":[80,90,85]
    })
print(data)
print("Average Marks:",data["Marks"].mean())
   
