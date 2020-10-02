# coding : utf-8

'''Automate Google Search'''

from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WAIT = 20

questions = [
	"Comment étudier en France sans garant ?",
	"Comment réussir à avoir un Visa pour étudier en France ?",
	"Comment financer mes études en France ?",
	"Comment obtenir un logement étudiant en France ?",
	"Comment faire pour ouvrir un compte bancaire en France ?",
	"Quelle est le meilleur service d'assurance pour les étudiants ?"
]

class GoogleResearch():
	driver = webdriver.Chrome()
	# driver = webdriver.Firefox()
	google_url = 'https://www.google.com/'

	def __init__(self):
		pass

	def go_to_google(self):
		print('Loading Google Page...')
		self.driver.get(self.google_url)

	@staticmethod
	def get_studely_xpath(soup):
		res_soup = soup.find('div', {'id': 'res'})
		res_list = res_soup.find_all('div', {'class': 'g'})
		for i, result in enumerate(res_list):
			try:
				a = result.find('a')
				# print(a)
				href = a.get('href')
				print('Href: ', href)
				if 'https://www.studely.com' in href:
					# print('Yes')
					# h3 = a.find('h3')
					# print(h3)
					# h3_class = h3.get('class')[0]
					# print('H3 Class: ', h3_class)
					return i-1
			except:
				pass
		return None

	def search(self, question):
		self.go_to_google()
		self.driver.find_element(By.NAME, "q").send_keys(question)
		print('Waiting for results...')
		self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
		# sleep(WAIT)
		search_soup = BeautifulSoup(self.driver.page_source, 'html.parser')
		xpath = self.get_studely_xpath(search_soup)
		# className, xpath = self.get_studely_xpath(search_soup)
		if xpath:
			try:
				# self.driver.find_element(By.CSS_SELECTOR, f".g:nth-child({xpath}) .{className} > span").click()
				self.driver.find_element(By.CSS_SELECTOR, f".g:nth-child({xpath}) .LC20lb > span").click()
				# sleep(WAIT)
			except Exception as e:
				print(e)
		

def main():
	# Launch navigator
	print('Launching navigator...')
	google = GoogleResearch()
	for question in questions:
		print('Q: ', question)
		google.search(question)
		# break

	# Close session
	google.driver.close()


if __name__ == '__main__':
	main()
