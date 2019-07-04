# import only system from os 
from os import system, name 
import time
import requests
from bs4 import BeautifulSoup


fs = open("youtubelog.txt", "w")
def Youtube() :
    print ("""


    __     __            _           _             _       _                _____         _                       _  _                         _____                      _   
    \ \   / /           | |         | |           | |     (_)              / ____|       | |                     (_)| |                       / ____|                    | |  
     \ \_/ /___   _   _ | |_  _   _ | |__    ___  | |      _ __   __ ___  | (___   _   _ | |__   ___   ___  _ __  _ | |__    ___  _ __  ___  | |      ___   _   _  _ __  | |_ 
      \   // _ \ | | | || __|| | | || '_ \  / _ \ | |     | |\ \ / // _ \  \___ \ | | | || '_ \ / __| / __|| '__|| || '_ \  / _ \| '__|/ __| | |     / _ \ | | | || '_ \ | __|
       | || (_) || |_| || |_ | |_| || |_) ||  __/ | |____ | | \ V /|  __/  ____) || |_| || |_) |\__ \| (__ | |   | || |_) ||  __/| |   \__ \ | |____| (_) || |_| || | | || |_ 
       |_| \___/  \__,_| \__| \__,_||_.__/  \___| |______||_|  \_/  \___| |_____/  \__,_||_.__/ |___/ \___||_|   |_||_.__/  \___||_|   |___/  \_____|\___/  \__,_||_| |_| \__|

                                                                                                                                                  Created By : Mohit Tanwani                            


           """)
    string = raw_input("Enter Youtube Channel URL : ")
    page = requests.get(string)
    #r=requests.get(string).text
    # Create a BeautifulSoup object
    bs = BeautifulSoup(page.text, 'lxml')
    bs=str(bs)

    #yourstring = r.encode('ascii', 'ignore').decode('ascii')
    #fs.write(yourstring)
        
    step2=bs.find("""epic-nav-item-heading">""")
    step2+=len("""epic-nav-item-heading">""")
    start=step2
    while bs[step2]!="<":
        step2+=1
    Channel_Name = bs[start:step2]
    Channel_Name = Channel_Name.lstrip()

    print "Channel Name : ",Channel_Name

    while True:
        # Collect first page of artists’ list
       
        page = requests.get(string)

        # Create a BeautifulSoup object
        bs = BeautifulSoup(page.text, 'lxml')
        #bs=str(bs)
        #fs.write(bs)
        step1=bs.find(class_="yt-subscription-button-subscriber-count-branded-horizontal subscribed yt-uix-tooltip")
        print(step1.get("aria-label"))

        
        #fs.write(step1.get("aria-label")
        time.sleep(1)
  
def Instagram() :
    
    username=raw_input("Enter Instagram User Name : ")
    string="""https://www.instagram.com/"""+username+"/"
    page = requests.get(string)
    r=requests.get(string).text

    bs = BeautifulSoup(page.text, 'lxml')
    bs=str(bs)

    start=bs.find("""full_name""")
    start+=len("""full_name""")
    end=bs.find("""has_channel""")
    Name=bs[start+3:end-3]
    print "\nUser Name : ",Name

    start=bs.find("""biography""")
    start+=len("""biography""")
    end=bs.find("""blocked_by_viewer""")
    bio=bs[start+3:end-3]
    print "\nBio : ",bio.encode(encoding='UTF-8',errors='strict')

    start=bs.find("""followed_by_viewer""")
                  
    start+=len("""followed_by_viewer""")+len(""""edge_follow":{  "count":""")+3
    end=bs.find("""follows_viewer""")
    following=bs[start+3:end-3]
    print "\nFollowing : ",following

    start=bs.find("""profile_pic_url_hd""")
    start+=len("""profile_pic_url_hd""")
    end=bs.find("""requested_by_viewer""")
    Profile=bs[start+3:end-3]
    print "\nProfile Image : ",Profile
    
    start= bs.find(""""edge_followed_by":{"count":""")
    start+=len("""edge_followed_by":{"count":""")+1
    end=bs.find("""},"followed_by_viewer""")
    followers=bs[start:end]
    followers.lstrip()
    print "\nFollowers : ",followers

def Twitter() :

    user = raw_input("Enter Twitter username : ")
    page = requests.get('https://twitter.com/'+user)
    bs = BeautifulSoup(page.text, 'lxml')
    follow_box = bs.find('li', {'class': 'ProfileNav-item ProfileNav-item--followers'})
    followers = follow_box.find('a').find('span', {'class':'ProfileNav-value'})
    twitter_follower = followers.get('data-count')
    
    print "Followers : ",twitter_follower


try:
    a=True
    while a:
        print "1. Youtube Live Subscribers Count"
        print "2. Instagram Followers Details"
        print "3. Twitter Followers Details"
        print "4. Exit"
        inp=raw_input("Choose from Above")
        if(inp=="1"):
            Youtube()
        elif (inp=="2"):
            Instagram()
        elif (inp=="3"):
            Twitter()
        elif (inp=="4"):
            a=False
        else :
            print "Wrong Choice" 
except:
    print "Something Went Wrong"
