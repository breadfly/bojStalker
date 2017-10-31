from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

hdr = {'User-Agent': 'Mozilla/5.0'}

user_url = "https://www.acmicpc.net/vs/"
my_id = input("내 아이디 : ");
user_id = input("상대 아이디 : ");
print("wait")
user_url = user_url + user_id + '/' + my_id; # 두번째로 있는 것

req = Request(user_url,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, "html.parser")

editData = soup.find_all('div', {'class':'panel-body'})[1]
problem_list = editData.find_all('span', {'class':'problem_number'})

for problem_id in problem_list:
	status_url = "https://www.acmicpc.net/status?problem_id=" + problem_id.get_text() + "&user_id=" + user_id + "&language_id=-1&result_id=4"
	req = Request(status_url, headers=hdr)
	page = urlopen(req)
	soup = BeautifulSoup(page, "html.parser")

	editData = soup.find('table', {'id':'status-table'})
	tr_list = editData.find_all('tr')
	td_list = tr_list[-1].find_all('td')
	print(td_list[8].find()["title"])

# 2017년 7월 26일 19시 48분 09초
"""
def dateToNum(date):
	ret = []
	idx = 0
	ret[idx] = int(date[2:4])
	idx += 1
	num1 = -1
	num2 = -1

	for i in range(5, len(date)) :
		if(date[i] >= '1' && date[i] <= '9'):
			if(num1 == -1) :
				num1 = int(date[i])
			else :
				num2 = int(date[i])
		else if(date[i] != ' ') :
			if(num2 == -1) 

	month = 0
	if(date.find('월') == 7) :
		month = int(date[6])
	else :
		month = int(date[6:8])
"""
#	year = date[0] * 1000 + date[1] * 100 + date[2] * 10 + date[3]

	#return year