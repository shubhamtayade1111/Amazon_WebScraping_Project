#!/usr/bin/env python
# coding: utf-8

# # Import libraries 

# In[ ]:


from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# ## Connecting to website and pulling in data for Apple Watch

# In[78]:


URL = 'https://www.amazon.ca/Apple-Watch-Smartwatch-Silver-Aluminum/dp/B07J2TQY8N/ref=lp_7012516011_1_2'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='corePrice_feature_div').get_text()








# In[79]:


print(title)


# In[80]:


print(price)


# ## Clean up the data a little bit

# In[81]:


price = price.strip()[:7][1:]
title = title.strip()

print(title)
print(price)


# ## Create a Timestamp for your output to track when data was collected

# In[82]:


import datetime

today = datetime.date.today()

print(today)


# ## Creating CSV, specifying headers and loading data into the file 
# ### Do not run this! It'll delete the data in csv.

# In[83]:


import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScrapingDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    


# In[90]:


import pandas as pd

df = pd.read_csv(r'C:\Users\q\AmazonWebScrapingDataset.csv')

print(df)


# ## Now we are appending data to the csv

# In[89]:


with open('AmazonWebScrapingDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# ## Combining all of the above code into one function

# In[91]:


URL = 'https://www.amazon.ca/Apple-Watch-Smartwatch-Silver-Aluminum/dp/B07J2TQY8N/ref=lp_7012516011_1_2'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


def check_price():
  
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='corePrice_feature_div').get_text()

    price = price.strip()[:7][1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScrapingDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if(price < 180):
        send_mail()
 
    


# ## Running check_price after a set time and inputs data into our CSV

# In[ ]:


while(True):
    check_price()
    time.sleep(86400) 


# In[93]:


import pandas as pd

df = pd.read_csv(r'C:\Users\q\AmazonWebScrapingDataset.csv')

print(df)


# # Send an email when Price goes down to 180

# In[89]:




def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('shubhtay044@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'shubhtay044@gmail.com',
        msg
     
    )


# In[ ]:




