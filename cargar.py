import pandas as pd
import csv
myData = [["celular", "mensaje", "link"],
         
          ['54 9 3585 08-0817','Hola !!!','https://flask-appbuilder.readthedocs.io/en/latest/rest_api.html'], 
          
          ]        

myFile = open('datos.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
   
print("Writing complete")