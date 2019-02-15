# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:44:00 2015

@author: b
"""


import os
import csv  
import urllib2
from bs4 import BeautifulSoup
#import lxml
#os.chdir('/Users/b/Documents/Betting/ACC')




## scraper function to scrape from tables in html

def scrape_cover(team, source, yr, urlz):
    
    #assert source=='TR' or source=='SR'
    tableclass='data'
     
    fname=team+source+str(yr)+'.csv' 
           
    outfile  = open(fname, "wb")
    writer = csv.writer(outfile, delimiter=',')
    
    
    # or if you're using BeautifulSoup4:
    # from bs4 import BeautifulSoup
    
    #urlz='http://www.covers.com/pageLoader/pageLoader.aspx?page=/data/ncb/teams/pastresults/2014-2015/team2188.html'
    soup = BeautifulSoup(urllib2.urlopen(urlz).read(),'html5lib')
    
    #data=[]
    
    tables=soup('table', {'class': tableclass})
    for tablenum in range(len(tables)):
        if tablenum==0:
            current_table=tables[tablenum]('tr')
        else:
            current_table=tables[tablenum]('tr', {'class': 'datarow'})
        for row in current_table:
            tds = row('td')
            #    print tds.string
            crow=[]
            
            for cr in tds:           
                #            print cr.string    
                #data.append(cr.string)
                crow.append(cr.string)
            
            writer.writerow(crow)
        
    outfile.close()
    #    soup=None
    #    data=None
    #return crow
    #return data
    #return soup