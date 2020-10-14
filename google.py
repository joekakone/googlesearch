# coding : utf-8

'''Automate Google Search -  https://gitlab.rintio.com/joekakone/automation.git'''

from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TOURS = 1000
LIMITS = 5
WAIT = 15
WAIT_STUDELY = 20

questions = [
	"Comment réussir à avoir un Visa pour étudier en France ?",
	"Comment étudier en France sans garant ?",
	"Comment financer mes études en France ?",
	"Comment obtenir un logement étudiant en France ?",
	"Comment faire pour ouvrir un compte bancaire en France ?",
	"Quelle est le meilleur service d'assurance pour les étudiants ?"
]

class GoogleResearch():
	driver = webdriver.Firefox()
	google_url = 'https://www.google.com/'

	def go_to_google(self):
		print('Loading Google Page...')
		self.driver.get(self.google_url)

	@staticmethod
	def get_studely_xpath(soup):
		"""
		input: results page
		output: first studely page link
		"""
		fld = soup.find('span', {'id': 'fld'})
		res_soup = soup.find('div', {'id': 'res'})
		res_list = res_soup.find_all('div', {'class': 'g'})
		for i, result in enumerate(res_list):
			try:
				a = result.find('a')
				href = a.get('href')
				if 'https://www.studely.com' in href:
					print('Studely found !')
					return href
			except:
				pass
		print('Studely not found !')
		return None

	def search(self, question):
		self.go_to_google()
		self.driver.find_element(By.NAME, "q").send_keys(question)
		print('Waiting for results...')
		self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)

		# pagination
		n_page = 1
		while n_page < LIMITS: # limit pages to 4
			try:
				print(f'Page {n_page}')
				sleep(WAIT)
				search_soup = BeautifulSoup(self.driver.page_source, 'html.parser')
				studely = self.get_studely_xpath(search_soup)
				print('Link:', studely)
				if studely:
					print('Loading Studely Page...')
					self.driver.find_element_by_xpath(f'//a[@href="{studely}"]').click()
					sleep(WAIT_STUDELY)
					break # after visiting the page, skip to next research
			except Exception as e:
				print(e)
			n_page += 1
			button = self.driver.find_element(By.XPATH, '//span[text()="Suivant"]')
			button.click()


def main():
	# Launch navigator
	print('Launching navigator...')
	google = GoogleResearch()
	for i in range(TOURS):
		print(f'** Tour n°{i+1} **')
		for question in questions:
			try:
				print('----------------------------------------')
				print('Q: ', question)
				google.search(question)
			except Exception as e:
				print(e):

	# Close session
	google.driver.close()


if __name__ == '__main__':
	main()
