import requests,bs4,re,csv
country_code='2'


#print len(D)

States={'5':'Andhra Pradesh','6':'Arunachal Pradesh','7':'Assam','8':'Bihar','9':'Chandigarh','10':'Chattisgarh','11':'Delhi','13':'Goa','14':'Gujrat','15':'Haryana','16':'Himachal Pradesh','17':'Jharkhand','18':'Karnataka','19':'Kerela','20':'Madhya Pradesh','21':'Maharashtra','22':'Manipur','23':'Meghalaya','25':'Nagaland','27':'Oddisa','28':'Ponducherry','29':'Punjab','30':'Rajasthan','32':'Sikkim','34':'Tamil Nadu','3696':'Telangana','35':'Tripura','36':'Uttar Pradesh','37':'Uttarakhand','38':'West Benagal'}

with open('./data.csv','wb') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow(["country Id","State Id","School Id","School Name","School Address","School Contacts","School Email","School Domain","School Category","School Type","School's Head"])
	for state_code,state in States.items():
		export_address="http://www.cisce.org/locate-search.aspx?country=2&state="+state_code+"&dist=0&city=0&location=&schooltype=&cve=&isc=&icse=&schoolclassi=&school=Enter%20School%20Name&search=search"
		response=requests.get(export_address)
		response.raise_for_status()
		cluster=bs4.BeautifulSoup(response.text,"lxml")
		D=cluster.select('td')
		i=5	
		while i<len(D):
			print "*******************************    ",i," **************************"
			DATA=[]
			DATA.append("2")
			DATA.append(state)
			######## Address of School #######
			School_name="".join(D[i].getText().split())
			School_name=School_name.split(",")
			Sid = School_name[0][:5]
			name = School_name[0][5:]
			name = name.encode('ascii','ignore')
			address = School_name[1][:len(School_name[1])-7]
			address = address.encode('ascii','ignore') 
			print address.encode('ascii','ignore')	
			
			#a.encode('ascii','ignore')
			DATA.append(Sid)
			DATA.append(name)
			DATA.append(address)





			######## Contact info of School ######
			
			School_contact="".join(D[i+1].getText().split())
			School_contact=str(School_contact)
			School_contact=School_contact.replace("[O]",";")
			School_contact=School_contact.replace("[F]",";")
			School_contact=School_contact.split(";" and "[Domain]")
			temp=School_contact[0].split("," and "[E]")
			#print School_contact[1]
			t=temp[0][1:].split(";")

			DATA.append(",".join(t))
			try:
				DATA.append(temp[1])
			except IndexError:
				DATA.append('')	
			DATA.append(School_contact[1])





			####### Categories of School ######
			C=[]
			School_category=D[i+2].getText().split()
			for j in range(len(School_category)):
				#print str(School_category[j])
				School_category[j]=School_category[j].encode("ascii","ignore")
				C.append(School_category[j])	
			DATA.append(",".join(C))





			###### Type Of board in school ######

			School_type=D[i+3].getText().split()
			#print str(School_type[0])
			School_type[0]=School_type[0].encode("ascii","ignore")
			DATA.append(School_type[0])




			###### Head of School #######

			School_head=D[i+4].getText()
			#print str(School_head)
			School_head=School_head.encode("ascii","ignore")
			DATA.append(School_head)
			i=i+5
			print DATA
			
			writer.writerow(DATA)



#################  DEBUGGING OPTIONS ############

# School_name="".join(D[695].getText().split())
# School_name=School_name.split(",")
# #print School_name[0][5:]
# print School_name[0][:5]
# print School_name[0][5:]
# print School_name[1][:len(School_name[1])-7]


################################################

# School_contact="".join(D[251].getText().split())
# School_contact=str(School_contact)
# School_contact=School_contact.replace("[O]",";")
# School_contact=School_contact.replace("[F]",";")
# School_contact=School_contact.split(";" and "[Domain]")
# print School_contact
# temp=School_contact[0].split("," and "[E]")
# #print School_contact[1]
# t=temp[0][1:].split(";")

# DATA=[]
# DATA.append(",".join(t))
# try:
# 	DATA.append(str(temp[1]))
# except IndexError:
# 	DATA.append('')
# DATA.append(str(School_contact[1]))
# print DATA

#################################################
