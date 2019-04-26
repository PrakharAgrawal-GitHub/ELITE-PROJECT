import urllib
import urllib.request
from bs4 import BeautifulSoup
import os


pages =["http://andcollege.du.ac.in" , "http://www.hansrajcollege.ac.in/" , "http://www.kmcollege.ac.in/" , "http://www.deshbandhucollege.ac.in" , "https://www.dducollegedu.ac.in" , "http://ramjas.du.ac.in" , "http://www.mirandahouse.ac.in/"]

thepage1 = urllib.request.urlopen(pages[0])
thepage2 = urllib.request.urlopen(pages[1])
thepage3 = urllib.request.urlopen(pages[2])
thepage4 = urllib.request.urlopen(pages[3])
thepage5 = urllib.request.urlopen(pages[4])
thepage6 = urllib.request.urlopen(pages[5])
thepage7 = urllib.request.urlopen(pages[6])


soup1 = BeautifulSoup(thepage1, "html.parser")
soup2 = BeautifulSoup(thepage2, "html.parser")
soup3 = BeautifulSoup(thepage3, "html.parser")
soup4 = BeautifulSoup(thepage4, "html.parser")
soup5 = BeautifulSoup(thepage5, "html.parser")
soup6 = BeautifulSoup(thepage6, "html.parser")
soup7 = BeautifulSoup(thepage7, "html.parser")


data1 = soup1.body.text
data2 = soup2.body.text
data3 = soup3.body.text
data4 = soup4.body.text
data5 = soup5.body.text
data6 = soup6.body.text
data7 = soup7.body.text

#print(data1)


'''data = soup.find('div',{"id":"andc"}).text'''

'''data = soup.find('div',{"id":"wrapper"}).text'''



file = open(os.path.expanduser("andcollege.txt"),'wb')
file.write(bytes(data1, encoding="ascii", errors='ignore').lower())

file = open(os.path.expanduser("hansrajcollege.txt"),'wb')
file.write(bytes(data2, encoding="ascii", errors='ignore').lower())

file = open(os.path.expanduser("kmcollege.txt"),'wb')
file.write(bytes(data3, encoding="ascii", errors='ignore').lower())

file = open(os.path.expanduser("deshbandhucollege.txt"),'wb')
file.write(bytes(data4, encoding="ascii", errors='ignore').lower())

file = open(os.path.expanduser("dducollegedu.txt"),'wb')
file.write(bytes(data5, encoding="ascii", errors='ignore').lower())

file = open(os.path.expanduser("ramjas.txt"),'wb')
file.write(bytes(data6, encoding="ascii", errors='ignore').lower())

file = open(os.path.expanduser("mirandahouse.txt"),'wb')
file.write(bytes(data7, encoding="ascii", errors='ignore').lower())



