# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:44:00 2015

@author: b
"""


import os
import csv  
import urllib2
from bs4 import BeautifulSoup


#directory='/Users/b/Documents/Betting/test'
#if not os.path.exists(directory):
#    os.makedirs(directory)
#

#os.chdir(directory)




## scraper function to scrape from tables in html

def scrape(team, source, yr, urlz):
    

    tableclass='sortable row_summable stats_table'

     
    #fname='ky2015.csv'
    fname=team+source+str(yr)+'.csv' 
           
    outfile  = open(fname, "wb")
    writer = csv.writer(outfile, delimiter=',')
    
    
    # or if you're using BeautifulSoup4:
    # from bs4 import BeautifulSoup
    
    
    #urlz='http://www.sports-reference.com/cbb/schools/kentucky/2015-gamelogs.html'
    soup = BeautifulSoup(urllib2.urlopen(urlz).read(),'html5lib')

    data=[]
    
    for index, row in enumerate(soup('table', {'class': tableclass})[0].thead('tr')):
        ths = row('th')
        #    print tds.string
        crow=[]
        
        for cr in ths:
            #            print cr.string    
            data.append(cr.string)
            crow.append(cr.string)
            
            
        ths = soup('table', {'class': tableclass})[1].thead('tr')[index]('th')
        #    print tds.string
        #crow=[]
        
        for cr in ths:
            #            print cr.string    
            data.append(cr.string)
            crow.append(cr.string)
            
            
        writer.writerow(crow)
    
    for index, row in enumerate(soup('table', {'class': tableclass})[0].tbody('tr')):
        tds = row('td')
        #    print tds.string
        crow=[]
        
        for cr in tds:           
            #            print cr.string    
            data.append(cr.string)
            crow.append(cr.string)

        tds = soup('table', {'class': tableclass})[1].tbody('tr')[index]('td')
        #    print tds.string
        #crow=[]
        
        for cr in tds:
            #            print cr.string    
            data.append(cr.string)
            crow.append(cr.string)
            
        
        writer.writerow(crow)
    
    outfile.close()
    #    soup=None
    #    data=None
    #return crow
    #return data
    #return soup