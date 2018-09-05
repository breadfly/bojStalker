from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

f = open("result.txt", 'w')

hdr = {'User-Agent': 'Mozilla/5.0'}

my_id = input("내 아이디 : ");
user_id = input("상대 아이디 : ");
print("wait")
vs_url = "https://www.acmicpc.net/vs/" + user_id + '/' + my_id; # 두번째로 있는 것

req = Request(vs_url,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, "html.parser")

editData = soup.find('div', {'class':'panel-body'}) # find_all()[0]
problem_list = editData.find_all('span', {'class':'problem_number'})

already = {}
result = []

for problem_id in problem_list:
	already[int(problem_id.get_text())] = 1

status_url = "https://www.acmicpc.net/status?problem_id=&user_id=" + user_id + "&language_id=-1&result_id=4"

while 1 :
	req = Request(status_url, headers=hdr)
	page = urlopen(req)
	soup = BeautifulSoup(page, "html.parser")

	editData = soup.find('table', {'id':'status-table'})
	tr_list = editData.find_all('tr')

	for idx in range(1, len(tr_list)) :
#		problem_id = tr_list[idx].find_all('td')[2].find()["title"]
		problem_id = int(tr_list[idx].find_all('td')[2].get_text())
		if not(problem_id in already) :
			result.append(problem_id)
			already[problem_id] = 1

	next_tag = soup.find('a', {'id':'next_page'})

	if next_tag != None:
		status_url = "https://www.acmicpc.net" + next_tag['href']
	else :
		break

result.reverse()

for x in result :
	f.write("https://boj.kr/" + str(x) + "\n")

print("done")
f.close()
