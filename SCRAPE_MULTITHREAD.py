import json
import re
import time
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import concurrent.futures

MAX_THREADS = 2		### TOTAL NUM OF THREADS TO BE LAUNCHED ###
LINKS = []			### USE THIS AS A GLOBAL POINTER TO ALL THE LINKS TO BE SCRAPPED ###


def mutlithreader(arglist):
	### LAUNCH THREAD FOR EACH LINK IN 'arglist'
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        executor.map(helper,arglist)


### THIS FUNCTION HELPS IN PASSING MORE THAN ONE ARGUMENT TO THE SCRAP FUNCTIONS ###
### FOR INSTANCE, LINKS CAN BE A LIST OF TUPLES THAT HAVE CERTAIN ARGUMENTS      ###
### THE HELPER FUNCTION WILL OPEN THE TUPLE UP AND PASS IN EACH VALUE AS AN ARGUMENT ###
def helper(args):
    scrape(args[0],args[1]...)



###  THIS IS WHERE YOU WOULD WRITE THE TEMPLATE FOR SCRAPING EACH PAGE  ###
def scrape(args...):
	return

url = 'DEFINE THE MAIN URL THAT YOU WILL USE TO GET ALL THE PAGE LINKS THAT NEED TO BE SCRAPED'

### SCRAPE THAT URL FOR ALL THE LINKS AND STORE THEM IN 'LINKS' ###

mutlithreader(LINKS)


### POST PROCESSING ###