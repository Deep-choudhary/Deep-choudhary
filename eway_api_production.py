import requests
import json
import time
from datetime import datetime, timedelta
now = datetime.now()
current_time = now.strftime("%H:%M:%S") 
print("time at the starting of the process:-",current_time)

### token...no.....####





















url = "https://einvapi.charteredinfo.com/v1.03/dec/auth?action=ACCESSTOKEN&aspid=1683991922&password=Sequelstring@123&gstin=09AAACL2470J1ZG&username=Lohiacorpk_API_CLI&ewbpwd=Lohia@123"
result = {}
res = requests.get(url, data=json.dumps(result))
result = json.loads(res.text)
# print(result)
# print(type(result["authtoken"]))
# print((result["authtoken"]))
# print(result["sek"])
authtoken_api = result["authtoken"]
print(authtoken_api,"<---------------token no_______")



date_eway="19/07/2022"



# url = f"http://gstsandbox.charteredinfo.com/ewaybillapi/dec/v1.03/ewayapi?action=GetEwayBillGeneratedByConsigner&aspid=1683991922&password=Sequelstring@123&gstin=34AACCC1596Q002&username=TaxProEnvPON&authtoken={authtoken_api}&docType={docType}&docNo={docNo}"
####production url#####
url = f"https://einvapi.charteredinfo.com/v1.03/dec/ewayapi?action=GetEwayBillsofOtherParty&aspid=1683991922&password=Sequelstring@123&gstin=09AAACL2470J1ZG&username=Lohiacorpk_API_CLI&authtoken={authtoken_api}&date={date_eway}"
result = {}
res = requests.get(url, data=json.dumps(result))
result = json.loads(res.text)
print("success")
print(result)
# print("%d total eway_bill no for today" % len(lmb))
# print(result["ewbNo"][0],"<---------ye ewayBillNo------",current_time)
# print(result["ewayBillDate"],"<---------ye ewayBill date------",current_time)

count = 0
for dict_values in result:
	count = count+1
	if dict_values["docNo"] == '2004':
	# if dict_values["totInvValue"] >= 50000 and dict_values['status']=='ACT':
		print("\n===========================================")
		print(f"eway_bill no:---------------->",dict_values['ewbNo'])
		print("eway_bill_date------------->",dict_values['ewayBillDate'])
		print("eway_bill_status----------->",dict_values['status'])
		print("eway_bill_rejectStatus----------->",dict_values["rejectStatus"])
		print("invoice no----------->",dict_values["docNo"])
		print("invoice date----------->",dict_values["docDate"]) 
		print("eway_bill_grand_total----------->",dict_values["totInvValue"])
		print("\n===========================================")



print("time at the end  of the process:-",current_time)