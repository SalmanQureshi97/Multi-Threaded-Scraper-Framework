import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from multiprocessing import Pool

MAX_PROCESSES = 2  ### TOTAL NUMBER OF PROCESSES TO BE LAUNCHED
LINKS = []


### THIS FUNCTION HELPS IN PASSING MORE THAN ONE ARGUMENT TO THE SCRAP FUNCTIONS ###
### FOR INSTANCE, LINKS CAN BE A LIST OF TUPLES THAT HAVE CERTAIN ARGUMENTS      ###
### THE HELPER FUNCTION WILL OPEN THE TUPLE UP AND PASS IN EACH VALUE AS AN ARGUMENT ###
def helper(args):
    scrape(args[0],args[1]...)


###  THIS IS WHERE YOU WOULD WRITE THE TEMPLATE FOR SCRAPING EACH PAGE  ###
def scrape(args...):
	return

	
def genURLS():
	url = 'DEFINE THE MAIN URL THAT YOU WILL USE TO GET ALL THE PAGE LINKS THAT NEED TO BE SCRAPED'

	### SCRAPE THAT URL FOR ALL THE LINKS AND STORE THEM IN 'LINKS' ###
	

	### START MULTI-PROCESSING ON THE LINKS ###
	p = Pool(MAX_PROCESSES)
	p.map(helper,LINKS)
	p.terminate()
	p.join()


### THIS IS NEEDED IN ORDER TO AVOID CHILD PROCESSES LAUNCHING MORE CHILD PROCESSES WHICH CAN LEAD TO ZOMBIE PROCESSES ###
if __name__ == '__main__':
    genURLS()

    ### POST PROCESSING ###



