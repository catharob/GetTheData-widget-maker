import bs4
import requests

def makeCode(folder, sheet):
    x = requests.get(folder)
    x.raise_for_status()
    gitSoup = bs4.BeautifulSoup(x.text)
    files = gitSoup.select('.js-directory-link') #get tag with URL for each file
    
    urls = []
    for f in files:
        urls.append(f.get('href')) #put urls into list
   
    for u in urls:
        if "README.md" in u:
            urls.remove(u) #get README out of list
            
    halfUrls = []
    for v in urls:
        if "/InsideEnergy/Data-for-stories/blob/master" in v:
            w = v.replace("/InsideEnergy/Data-for-stories/blob/master", "")
            halfUrls.append(w) #strip extra stuff off front of url
    csvFile = halfUrls[0]
    codeHasCsv = "http://rawgit.com/insideenergy/Data-for-stories/master%s" % csvFile
    xlsFile = halfUrls[1]
    codeHasXls = "http://rawgit.com/insideenergy/Data-for-stories/master%s" % xlsFile

    #now concatonate the code together
    widgetCode = "<small><strong> Get the data: <a href='" + codeHasCsv + "'>CSV</a> | <a href='" + codeHasXls + "'>XLS</a> | <a href='" + sheet + "' target='_blank'>Google Sheets</a> | Source and notes: <a href='" + folder + "'>Github</a> </strong></small>"       
    print widgetCode

print 'Make the "Get the Data" widget code.'
print "Enter GitHub ULR of your new folder inside 'Data-for-stories':"
myFolder = raw_input()
print "Enter Google Sheets URL for public viewing:"
mySheet = raw_input()
print "~~~~~~~~~~Widget Code - Paste this below your chart~~~~~~~~~~"
makeCode(myFolder, mySheet)
