#!/usr/bin/env python
# coding: utf-8

# In[98]:


# If you don't have Beautiful Soup, install with 'conda install beautifulsoup' in terminal
# Python requires us to explicitly load the libraries that we want to use:
import requests
import bs4
import re


# In[99]:


# Load a webpage into python so that we can parse it and manipulate it.
URL = 'https://www.icc-ccs.org/index.php/piracy-reporting-centre/live-piracy-report'


# In[100]:


# Control of Connection
# We just turned the website code into a Python object. 
response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, "html.parser")


# In[101]:


# find all the tags with class city or number
data = soup.findAll(attrs={'class':['jos_fabrik_icc_ccs_piracymap2016___narrations']})


# In[102]:


f = open('piracy_reporting_centre.csv','w') # open new file, make sure path to your data file is correct
f.write("Date\tTime\tPosition\tArea\tCountry" + "\n") # write headers


# In[103]:


# Clear HTML tag and insert text in array
results = []
for element in data:
     TAG_RE = re.compile(r'<[^>]+>')
     text = TAG_RE.sub('', str(element))
     results.append(text)


# In[104]:


# Clear \r \n \t to prepare string variable to clear Narrations: and insert text in array
results_patten = []
results_explode = [] 
results_2 = []
for element in results:
     item = ''
     item = str(element)
     item = item.replace('\r', '').replace('\n', '').replace('\t', '')
     if item != 'Narrations:':
          results_explode = item.split(".")
          i = 0 
          for result in results_explode:
                i = i + 1
                if i <= 5: results_2.append(result)


# In[105]:


# Prepare string variables Date, Time, Position, Area and Country, replace characters to insert character | and insert text in array
i = 0
results = []
for element in results_2:
    i = i + 1
    if i == 1: 
        data1 = str(element)
    if i == 2: 
        data2 = str(data1) + '.' + str(element)
    if i == 3: 
        date = data2 + '.' + str(element)
    if i == 4: 
        position = str(element)
    if i == 5: 
        country = str(element)
        item = date.replace(': Posn : ', '|').replace(': Posn: ', '|').replace(': ', '|') + '.' + position.replace(' – ', '|') + '.' + country.replace('E, ', 'E|').replace('W, ', 'W|')
        item = item.replace('N – ', 'N|').replace('W, ', 'W|')
        results.append(item)
        i = 0


# In[106]:


# Split to elements to array results for character | and Write to file items Date, Time, Position, Area and Country
for element in results:
       item = element.split("|")
       i = 0
       for element1 in item:
            i = i + 1
            if i == 1: 
                date = str(element1)
                f.write(date + "\t") # fecha date and add tabulator
            if i == 2: 
                time = str(element1)
                f.write(time + "\t") # fecha time and add tabulator
            if i == 3: 
                position = str(element1)
                f.write(position + "\t") # fecha position and add tabulator
            if i == 4: 
                area = str(element1)
                f.write(area + "\t") # fecha area and add tabulator
            if i == 5: 
                country = str(element1)
                f.write(country + "\t\n") # fecha country and add tabulator                


# In[107]:


# Close file
f.close() # close file


# In[ ]:




