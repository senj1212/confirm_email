import requests
from bs4 import BeautifulSoup


class TempMail:
	def __init__(self):
		self.base_url = "https://10minutemail.net/"
		self._session = None
		self.current_email = None

	def _create_session(self):
		self._session = requests.Session()
		self._session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"
		}
		self.current_email = None

	#create new email
	def create(self):
		self._create_session()
		r = self._session.get(self.base_url)
		soup = BeautifulSoup(r.text, 'html.parser')
		self.current_email = soup.find('input', id='fe_text')['value']
		return self.current_email

	def _query(self, url):
		if not self.current_email:
			self.create()
		return self._session.get(url)

	def _update_time(self):
		self._query("https://10minutemail.net/more.html")

	def _pars_text_from_mail(self, url_mail):
		r = self._query(url_mail)
		soup = BeautifulSoup(r.text, 'html.parser')
		return soup.find('div', class_='mailinhtml').text

	def _pars_mail_line(self, lines):
		mails = []
		for line in lines:
			mail_line = line.find_all('td')
			mail_url = self.base_url + mail_line[0].find('a')['href']
			text = self._pars_text_from_mail(mail_url)
			mail = {
				"from": mail_line[0].text,
				"title": mail_line[1].text,
				"time": mail_line[2].text,
				"text": text

			}
			mails.append(mail)
		return mails

	# Return all mails from email
	def get_mails(self):
		r = self._query(self.base_url)
		soup = BeautifulSoup(r.text, 'html.parser')
		table = soup.find('table', id='maillist')
		lines = table.find_all('tr')[1:]
		self._update_time()
		return self._pars_mail_line(lines)


tm = TempMail()
print(tm.create())
print(tm.get_mails())

while True:
	try:
		eval(input(">>> "))
	except Exception as e:
		print(e)
