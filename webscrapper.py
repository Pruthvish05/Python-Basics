import requests
from bs4 import BeautifulSoup

url =input("Enter the URL of the website to scrape: ")
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    txt = soup.get_text()
    text= txt.replace('\n', ' ').replace('\r', '').strip()
    sum=text[:1000]
    print(f"First 1000 characters of the webpage:\n{sum}")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")