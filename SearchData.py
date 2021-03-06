import os
import numpy
import pandas

Clgact=['about','admission','eca','nss','department','contact','naac','placement','principal']

data=[]

dataclg=['Acharya Narendra Dev College','Hansraj College','Kirori Mal College','Deshbandhu College','Deen Dayal Upadhyay College','Ramjas College','Miranda House']

#pages =["http://andcollege.du.ac.in" , "http://www.hansrajcollege.ac.in/" , "http://www.kmcollege.ac.in/" , "http://www.deshbandhucollege.ac.in" , "https://www.dducollegedu.ac.in" , "http://ramjas.du.ac.in" , "http://www.mirandahouse.ac.in/"]


Clgfile=['andcollege.txt','hansrajcollege.txt','kmcollege.txt','deshbandhucollege.txt','dducollegedu.txt','ramjas.txt','mirandahouse.txt']

'''
a1=0
if 'About' in open('jdm.txt').read():
  a1=1
print(a1)
'''

for j in range(0,7):
  L = [0] * 9
  #print(L)
  for i in range(0,9):
      if Clgact[i] in open(Clgfile[j]).read():
          L[i]=1

  #print("details of",Clgfile[j]," ",L)
  data.append(L)

#all colleges data in data
#print(data)

pandas.set_option('max_columns',10)
pandas.set_option('max_rows',10)
pandas.set_option('expand_frame_repr',False)

df=pandas.DataFrame(data,columns=['About Us','Admission','ECA','NSS','Departments','Contact Us','NAAC/NIRF','Placement Cell','Principal\'s Desk'],index=['Acharya Narendra Dev College','Hansraj College','Kirori Mal College','Deshbandhu College','Deen Dayal Upadhyay College','Ramjas College','Miranda House'])

df['Points']=df['About Us']+df['Admission']+df['ECA']+df['NSS']+df['Departments']+df['Contact Us']+df['NAAC/NIRF']+df['Placement Cell']+df['Principal\'s Desk']
print(df)

#dfList=df['Points'].tolist()
#list(zip(dataclg,dfList))
#b=pandas.DataFrame(a,columns=['College Name','Total Points'],index=['*','*','*','*','*','*','*'])
#print(b)
