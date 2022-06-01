# Import the xlrd module
from src.dbconnector import *
from src.sample import searchfn
import xlrd

# Open the Workbook
workbook = xlrd.open_workbook("Book1.xlsx")

# Open the worksheet
worksheet = workbook.sheet_by_index(0)

# Iterate the rows and columns
for i in range(986, 989):
    print(worksheet.cell_value(i,1))
    key=searchfn(worksheet.cell_value(i,1))


    try:
        qry="INSERT INTO `information` VALUES(NULL,%s,%s,%s,%s,%s,'',1,'approved')"
        val=(worksheet.cell_value(i,0),worksheet.cell_value(i,1),worksheet.cell_value(i,2),key[1],key[0])
        iud(qry,val)
    except:
        print("error===============")
    # for j in range(0, 3):
    #     # Print the cell values with tab space
    #     print(worksheet.cell_value(i, j),"==", end='\t')
    print('')