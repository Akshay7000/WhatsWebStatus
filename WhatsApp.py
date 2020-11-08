from selenium import webdriver
import time
from playsound import playsound

name = input("Enter the contact name: ")
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
time.sleep(10)


target_contact = driver.find_element_by_xpath("//span[.='" + name + "']").click()

play = "play"
offline = "off"
def online():
	global a,play,offline

	def status():
		global play,offline
		element_status = driver.find_element_by_xpath("//*[@id='main']/header/div[2]/div[2]/span").get_attribute("innerHTML").splitlines()[0]
		if (element_status == "online"):
			contact_name = driver.find_element_by_xpath("//*[@id='main']/header/div[2]/div/div/span").text
			if (play == "play"):
				print(contact_name +" is online")
				playsound('play.mp3')
				play = "noplay"
				offline = "off"
	try:
		status()
	except:
		if (offline == "off"):
				print("offline")
				#playsound('play.mp3')
				offline = "on"
		else:
			play = "play"

while true:
	online()
