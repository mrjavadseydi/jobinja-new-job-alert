import requests
import bs4
import collections
collections.Callable = collections.abc.Callable

from bs4 import BeautifulSoup 
urls = [
    "https://jobinja.ir/jobs?&filters%5Bkeywords%5D%5B0%5D=laravel&filters%5Bkeywords%5D%5B0%5D=laravel&filters%5Bremote%5D=1&preferred_before=1705846951&sort_by=relevance_desc",
    "https://jobinja.ir/jobs?&filters%5Bkeywords%5D%5B0%5D=php&filters%5Bkeywords%5D%5B0%5D=laravel&filters%5Bremote%5D=1&preferred_before=1705846951&sort_by=relevance_desc"
]
bot_token = ""
chat_id = ""


last_jobs = ""
f = open("last_jobs.txt", "r")
last_jobs = f.read()
f.close()
#json decode from last_jobs.txt

for url in urls:
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    jobs = soup.find_all("h2", {"class": "o-listView__itemTitle"})
    for job in jobs:
        job_id = job.find("a", {"class": "c-jobListView__titleLink"})
        job_title = job_id.text
        job_link = job_id["href"]
        #trim job_title
        job_title = job_title.strip()
        job_link = job_link.strip()
        text_to_save = job_title + " " + job_link
        if job_link not in last_jobs:
            f = open("last_jobs.txt", "a")
            f.write(text_to_save + "\n")
            f.close()
            requests.get("https://api.telegram.org/bot"+bot_token+"/sendMessage?chat_id="+chat_id+"&text=JOB ALERT : " + text_to_save)
        
