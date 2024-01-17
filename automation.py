import csv 
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

 

with open('csv', 'r') as csv_file:#<-- Put your CSV file in here 
    csv_reader = csv.reader(csv_file) 


    for line in csv_reader:
        driver = webdriver.Chrome()
        driver.get('')#Put your Google form link in here
        
        time.sleep(1)
            
        sname = 'Name'#write ypur name here
        name =driver.find_element('xpath' , '????')#<--Xpath from Google form
        name.send_keys(sname)
        
        s1name = 'Name of the Newspaper'#Write the name of your newspaper
        naame =driver.find_element('xpath' , '?????')#<--Xpath from Google form
        naame.send_keys(s1name)
        
        date = driver.find_element('xpath' , '????')#<--Xpath from Google form
        date.send_keys(line[0])
        
        
        headlines = driver.find_element('xpath' , '?????')#<--Xpath from Google form
        headlines.send_keys(line[1])
        
        ctext = driver.find_element('xpath' , '?????')#<--Xpath from Google form
        ctext.send_keys(line[3])  
        
        text = driver.find_element('xpath' , '?????')#<--Xpath from Google form
        text.send_keys(line[4])
      
        
        category = driver.find_element('xpath', '????')#<--Xpath from Google form
        category.click()
            
        submit = driver.find_element('xpath' , '????')#<--Xpath from Google form
        submit.click()