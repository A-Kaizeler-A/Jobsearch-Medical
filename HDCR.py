from bs4 import BeautifulSoup
import requests
import time
from plyer import notification

try:
    site = requests.get('https://www.net-empregos.com/pesquisa-empregos.asp?chaves=&cidade=Lisboa&categoria=14&zona=1&tipo=0').text
except:
    print("Check your internet")

soup = BeautifulSoup(site, 'lxml')

ffile = open('C:/Users/Xano/Desktop/JOBS.txt', 'a', encoding="utf-8")

#f_writer = csv.writer(ffile)
#f_writer.writerow(['Job Title', 'Job Link'])

for offer in soup.find_all("div", {"class":"job-item media"}):

    jobtitle = str(offer.h2.a.text)

    #print(jobtitle)

    try:
        joblink = str(offer.h2.a)
        joblink = joblink.split(" ")[1]
        joblink = joblink.split("\"")[1]
        jlink = str(f"https://www.net-empregos.com/{joblink}")

    except Exception as E:
        jlink = None

    #print(jlink)

    #print()
    with open('C:/Users/Xano/Desktop/JOBS.txt', 'r', encoding="utf-8") as filer:
        if str(jobtitle) in filer.read():
            print("No new jobs")
        else:
            ffile.write(f"{jobtitle} \n {jlink}")
            ffile.write("\n")
            ffile.write("\n")
            notification.notify(title="There are new Jobs!", message=f"{jobtitle}", timeout=30)

    time.sleep(60*60)

ffile.close()