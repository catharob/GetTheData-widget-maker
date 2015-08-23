import bs4
import requests

def makeCode(folder):
    x = requests.get(folder)
    x.raise_for_status()
    gitSoup = bs4.BeautifulSoup(x.text)
    files = gitSoup.select('.js-directory-link') #get tag with URL for each file
    
    urls = [f.get('href') for f in files if 'README.md' not in f.get('href')] #put urls in list without readme filr

    halfUrls = []
    for v in urls:
        if "/InsideEnergy/Data-for-stories/blob/master" in v:
            w = v.replace("/InsideEnergy/Data-for-stories/blob/master", "")
            halfUrls.append(w) #strip extra stuff off front of url

    justFolders = []
    for x in halfUrls:
        if ".csv" in x:
            y = x.replace(".csv", "")
            justFolders.append(y)
        if ".xlsx" in x:
            z = x.replace(".xlsx", "")
            justFolders.append(z) #gets file extensions off 
    
    noDuplicates = []
    for z in justFolders:
        if z not in noDuplicates:
            noDuplicates.append(z) #gets rid of duplicates
    
    #now concatonate a code for each folder name, and ask for corresponding Google Sheets URL
    for i in noDuplicates:
        print "Enter the Google Sheets URL for public viewing that corresponds with " + i
        mySheet = raw_input()
        print "~~~~~~~~~~Widget code for " + i + "~~~~~~~~~~"
        print
        print '<small><strong> Get the data: <a href="http://rawgit.com/insideenergy/Data-for-stories/master' + i + '.csv">CSV</a> | <a href="http://rawgit.com/insideenergy/Data-for-stories/master' + i + '.xlsx">XLS</a> | <a href="' + mySheet + '" target="_blank">Google Sheets</a> | Source and notes: <a href="' + folder + '">Github</a> </strong></small>'
        print
        
        
print 'Make the "Get the Data" widget code.'
print "Enter GitHub ULR of your new folder inside 'Data-for-stories':"
myFolder = raw_input()
makeCode(myFolder)