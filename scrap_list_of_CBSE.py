import requests,bs4,csv
export_from="http://www.thelearningpoint.net/home/crawledinformation/a-list-of-cbse-schools-in-india/a-list-of-cbse-schools-in-"


States=[]
States.append("andaman-and-nicobar")
States.append("andhra-pradesh")
States.append("arunanchal-pradesh")
States.append("assam")
States.append("bihar")
States.append("chandigarh")
States.append("karnataka")
States.append("jharkhand")
States.append("jammu-and-kashmir")
States.append("himanchal-pradesh")
States.append("harayana")
States.append("gujarat")
States.append("foreign-countries-outside-india")
States.append("delhi")
States.append("daman-and-diu")
States.append("dadar-and-nagar-haveli")
States.append("chattisgarh")
States.append("punjab")
States.append("pondicherry")
States.append("orissa")
States.append("nagaland")
States.append("mizoram")
States.append("meghalaya")
States.append("manipur")
States.append("madhya-pradesh")
States.append("lakshadweep")
States.append("kerala")
States.append("west-bengal")
States.append("uttar-pradesh")
States.append("uttaranchal")
States.append("tripura")
States.append("tamil-nadu")
States.append("sikkim")
States.append("rajasthan")
States=sorted(States)



with open('./dataCbse.csv','wb') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow(["School Id","School Name","School State","School District","School Address","School PIN","STD code","Phone Office","Phone residence","School Email","School Website","School Head","School Trust"])

	for state in range(len(States)):

		response=requests.get(export_from+States[state])
		response.raise_for_status()
		cluster=bs4.BeautifulSoup(response.text,"lxml")
		D=cluster.select('tr')
		print "************************************************************************"
		print "Number of Schools in ",States[state]," are :",len(D)
		#print D[4]
		for row in range(4,len(D)):

			CSVROW=[]
			###########################################################
			DATA=D[row].select('td')

			################ School code and Name ################

			School_code = DATA[0].getText().strip().encode("ascii","ignore")
			School_code = "".join(c for c in School_code if c.isdigit())
			School_name = DATA[0].getText().strip().encode("ascii","ignore")
			School_name = "".join(c for c in School_name if c.isdigit() == False)[20:]
			CSVROW.append(School_code)
			CSVROW.append(School_name)
			#print School_code, School_name
			#print School_code

			################ School Address ################

			s = DATA[1].getText().strip().encode('ascii', 'ignore')
			s = s.replace("State:",";").replace("Dist.:",";").replace("Address:",";").replace("Pin Code:",";")[1:].split(";")
			School_state = s[0]
			School_dist = s[1]
			School_address = s[2]
			School_pin = s[3]
			CSVROW.append(School_state)
			CSVROW.append(School_dist)
			CSVROW.append(School_address)
			CSVROW.append(School_pin)
			#print s 

			############### School Contacts ###############

			temp = DATA[2].getText().strip().encode('ascii','ignore')
			temp = temp.replace("Std Code:",";").replace("Phone (Office):",";").replace("Phone (Residence):",";")[1:].split(";")
			Std_code = temp[0]
			Phone_office = temp[1]
			Phone_res = temp[2]
			CSVROW.append(Std_code)
			CSVROW.append(Phone_office)
			CSVROW.append(Phone_res)
			#print Phone_res

			############## Email and Website ##############

			E = DATA[3].getText().strip().encode('ascii','ignore')
			E = E.replace("Email:",";").replace("Website:",";")[1:].split(";")
			School_email = E[0]
			School_website = E[1]
			CSVROW.append(School_email)
			CSVROW.append(School_website)
			#print School_email, School_website

			############### School Head ################

			H = DATA[4].getText().strip().encode('ascii','ignore')
			H = H.replace("Principal:",";").replace("Trust/Society:",";")[1:].split(";")
			School_head = H[0]
			School_trust = H[1]
			CSVROW.append(School_head)
			CSVROW.append(School_trust)
			print School_head
			writer.writerow(CSVROW)

			#####################################################################################
