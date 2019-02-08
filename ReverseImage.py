__author__ = 'Jason'
import pysftp as sftp
import urllib
from urllib.request import urlopen
from http.cookiejar import CookieJar
import time
import re

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]



#will be for raspberry pi eventually :D
def imageLookup():
    #s = sftp.Connection(host = "pythonprogamming.net",username = "python", password = "rules")
    #localpath = '/home/pi/imagerec.jpg'
    #numToAdd = str(int(time.time()))
    #remotepath = '/var/www/image/rec/currentImage' + numToAdd+'.jpg'
    #s.put(localpath,remotepath)
    #s.close()

    #http://puu.sh/CqIWa/c6124e2327.jpg
    #goog = 'http://images.google.com/searchbyimage?image_url=http://puu.sh/CqIWa/c6124e2327.jpg'
    #imagepath = 'http://pythonprogamming.net/imagerec/currentImage' + numToAdd + '.jpg'
    imagepath ='http://puu.sh/CqIWa/c6124e2327.jpg'
    imagepath2 = 'http://puu.sh/CqKzd/0b1b938de2.jpg' #tzuyu
    googlepath = 'http://images.google.com/searchbyimage?image_url='+imagepath2
    sourceCode = opener.open(googlepath).read().decode('utf-8')
    findLink = re.findall(r'<a href="https://kprofiles.com/(.*?)/"',sourceCode)
    print(sourceCode)
    print(findLink)
    if len(findLink) !=0:
        print('https://kprofiles.com/'+findLink[0])

#takes in an image and reverse image searches into google. Takes the result and appends "kprofiles" to it and searches
#It up in google.
#It will print all kprofiles results for the user to
#parameter link to an image of kmember
def kprofileLookup(imagepath):

    #imagepathEx ='http://puu.sh/CqIWa/c6124e2327.jpg'
    #imagepathEx2 = 'http://puu.sh/CqKzd/0b1b938de2.jpg' #tzuyu

    googlepath = 'http://images.google.com/searchbyimage?image_url='+imagepath
    sourceCode = opener.open(googlepath).read().decode('utf-8')
    print(sourceCode)
    findSearchQuery = re.findall(r'title="Search" value="(.*?)"',sourceCode)
    newQuery = findSearchQuery[0]+ '%20kprofiles.com'
    newQuery = newQuery.replace(' ','%20')
    googleQueryLink = 'https://www.google.com/search?q='

    newGooglePath = googleQueryLink + newQuery
    print(newGooglePath)
    newSourceCode = opener.open(newGooglePath).read().decode('utf-8')
    findLink = re.findall(r'<a href="https://kprofiles.com/(.*?)/"', newSourceCode)

    for x in findLink:
        print('https://www.kprofiles.com/'+ x)
    return findLink


#done using google
#link to image or product
#takes in an image, reverse image searches it then finds an amazon link for it.
def amazonLookup(imagepath):
    imagepathEx = 'https://i5.walmartimages.com/asr/4a83f68a-cb6f-4de3-8e34-e1319ae21c61_2.44a65ab1f90f5bc0522610cc4b501fc1.png?odnHeight=450&odnWidth=450&odnBg=FFFFFF' #example link
    googlepath = 'http://images.google.com/searchbyimage?image_url=' + imagepath #url that will have a link to an image appeneded to it to reverse image serach
    sourceCode = opener.open(googlepath).read().decode('utf-8')#opens the link to the reverse image searched picture , has a lot of information tied to it
    findSearchQuery = re.findall(r'title="Search" value="(.*?)"', sourceCode) #finds the search value that the image came out with
    newQuery = findSearchQuery[0] + '%20amazon.com' #appends amazon.com to it to refine the serach
    newQuery = newQuery.replace(' ', '%20')#replaces the spaces in the query with %20 to be able to append to google query link
    googleQueryLink = 'https://www.google.com/search?q=' #url to do a  regular google search
    newGooglePath = googleQueryLink + newQuery #combined the new terms

    print("The search query: " + newGooglePath)  #link to the google query

    newSourceCode = opener.open(newGooglePath).read().decode('utf-8')
    findLink = re.findall(r'<a href="https://www.amazon.com/(.*?)"', newSourceCode) #a list of all the google results with amazon
    print(newSourceCode)

    print("Heres the list of all the values in findLink: " + str(findLink))
    print("Here are all the links: ")
    for x in findLink:
        print('https://www.amazon.com/' + x) #prints to terminal all the results
    return findLink #returns the list of the resulting urls
amazonLookup('https://cdn.discordapp.com/attachments/515376967176945701/531968680217542676/reeses.jpg')