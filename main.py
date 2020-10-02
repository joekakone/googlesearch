# coding : utf-8

'''Automation of Studely Page Visiting'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# principal domain
BASE_URL = 'https://www.studely.com'
# total visit for each page
N_TOURS = 10000
# seconds between two visits
# WAIT = 10

# pages urls
urls = [
	'https://www.studely.com/faq/',
	'https://www.studely.com/nos-services/ma-caution-bancaire/',
	'https://www.studely.com/article/un-projet-d-etudes-en-france-oui-mais-comment-le-financer/',
	'https://www.studely.com/nos-services/mon-logement/',
	'https://www.studely.com/nos-services/mon-compte-bancaire/',
	'https://www.studely.com/article/rentree-2020-avez-vous-pense-a-souscrire-a-des-assurances-completes/'
]

# Launch navigator
print('Launching navigator...')
browser = webdriver.Firefox()

def tour():
	'''Visit all pages once'''
	for url in urls:
		try:
			print(f'Visiting {url}...')
			browser.get(url)
		except Exception as e:
			pass
#		sleep(WAIT)

def main():
	# test url - visit principal domain
	print(f'Visiting {BASE_URL}...')
	browser.get(BASE_URL)

	# visit all pages N_TOURS times
	for i in range(N_TOURS):
		print(f'*** Tour {i+1} ***')
		tour()

	# Close navigator
	print('Closing navigator...')
	browser.quit()

if __name__ == '__main__':
	main()
