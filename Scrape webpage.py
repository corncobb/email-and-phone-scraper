##################################################
# Webpage scraper by Cameron Cobb                #
# Scrapes for phone and emails and places in     # 
# spreadsheet.                                   #
# Python 3 required                              #
##################################################

#!/usr/bin/env python3


from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request
import time
from openpyxl import Workbook
import os
from datetime import datetime

def function():
       
    scrape = BeautifulSoup(page, 'html.parser')
    scrape = scrape.get_text()
    
    phone_numbers = set(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",scrape)) #"set" removes duplicates
    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",scrape))

    nodupnumber = len(list(phone_numbers))
    nodupemail = len(list(emails))

    dupnumber = len(list(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",scrape))) 
    dupemail = len(list(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",scrape)))

    number_of_dup_number = int(dupnumber) - int(nodupnumber) 
    number_of_dup_email = int(dupemail) - int(nodupemail)

    email_list = list(emails)

    if len(phone_numbers) == 0:
        print ("No phone number(s) found.")

        print("-----------------------------\n")
    else :
        count = 1
        for item in phone_numbers:
            print ('Phone number #' + str(count) + ': ' + item )
            count += 1

    print("-----------------------------\n")

    if len(emails) == 0:
        print("No email address(es) found.")
        print("-----------------------------\n")
    else:
        
        count = 1
        for item in emails:
            print('Email address #' + str(count) + ': ' + item)
            count += 1

    if (save_excel == True):
        for row in zip(email_list):
            sheet.append(row)
        excel_file = (name_the_file + ".xlsx")
        book.save(excel_file) 
       
    print("\nDuplicates have been removed from list.")
    print("Total phone numbers: ", nodupnumber)
    print("Total email addresses: ", nodupemail)
    print("There were " + str(number_of_dup_number) + " duplicate phone numbers.")
    print("There were " + str(number_of_dup_email) + " duplicate email addresses.")

    if(save_excel == True):
        print("\n\nData has been stored inside of an Excel spreadsheet named: " + excel_file + " in this directory: " + os.getcwd())
        mod_time = os.stat(excel_file).st_mtime
        print("\nCompleted at: " + str(datetime.fromtimestamp(mod_time)))
        print("\nSize of file: " + str(os.stat(excel_file).st_size) + " KB")


save_excel = False #Change to "True" to save email into Excel

webpage = input("Paste the webpage you would like to scrape (include http/https): ")

if (save_excel == True):
    book = Workbook()
    sheet = book.active
    name_the_file = input("Name the file you would like to save the data in (don't include .xlsx): ")
    

print("\n\nWebpage is currently being scrapped... please wait...")

try:
    page = urlopen(webpage) 
    function()
    
except:
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(webpage,headers=hdr)
    page = urlopen(req)
    function()

    
    



