from selenium import webdriver
import time
from playsound import playsound
driver = webdriver.Chrome('F:\Hacks\WhatsAppOnline\chromedriver.exe')
driver.get('https://web.whatsapp.com')
time.sleep(10)
a=0
target_contact = driver.find_element_by_xpath("//span[text()='anjiii']").click()

def online():
	global a
	def status():	
		
		element_status = driver.find_element_by_xpath("//*[@id='main']/header/div[2]/div[2]/span").get_attribute("innerHTML").splitlines()[0]
	
		if  (element_status == "online"):
			playsound('F:\Hacks\WhatsAppOnline\play.mp3')
		
		'''text_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]")
		text_box.send_keys("You are under surveillance. Current Status "+ element_status)
		send_button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
		'''
		
	try:
		status()
	except:
		a = 0
		
	
while a==0:
	online()
	