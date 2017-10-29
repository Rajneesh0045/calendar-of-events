# importing pdf library and regular expression library

import PyPDF2
import re
import datetime

tday = datetime.date.today()
pday = int(tday.day)
pmonth = int(tday.month)

# open a file in read mode and assign it to an object

fileObj = open('coe.pdf', 'rb')

# creating pdf object from file object

pdfReader = PyPDF2.PdfFileReader(fileObj)

pageObj2 = pdfReader.getPage(2)
pageObj3 = pdfReader.getPage(3)
pageObj4 = pdfReader.getPage(4)

infoText2 = pageObj2.extractText()
infoText3 = pageObj3.extractText()
infoText4 = pageObj4.extractText()


data2 = infoText2.replace("\n", "")
data3 = infoText3.replace("\n", "")
data4 = infoText4.replace("\n", "")

# print(data)

newdata = data2.split()
newdata.extend(data3.split())
newdata.extend(data4.split())

# print(newdata)

# Exctracting list of date into a new list

Cdate = []
Cday = []
dateReg = re.compile(r'\d\d.\d\d.\d\d')

for i in range(len(newdata)):
    if(dateReg.search(newdata[i])):
        Cdate.append(newdata[i])
        Cday.append(newdata[i+2])



print(Cdate)
print(Cday)

writeFile = open('coeExtracted.txt', 'w')
writeFile.write(str(Cdate))
writeFile.write(str(Cday))
#
# print(dir(Cdate[1]))

dayList = []
monthList = []
yearList = []

for i in Cdate:
    tday, tmonth, tyear = i.split(".")
    dayList.append(tday)
    monthList.append(tmonth)
    yearList.append("20" + tyear)

# print(dayList)
# print(monthList)
# print(yearList)

# print(type(int(monthList[40])))
# print(type(int(tday.day)))

for i in range(len(Cdate)):
    if int(monthList[i]) == pmonth and int(dayList[i]) == pday:
        print("Day " + Cday[i])
        break