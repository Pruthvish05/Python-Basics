import requests
from bs4 import BeautifulSoup as bs 

github_user = input("Enter the GitHub username:")
url = f"https://github.com/{github_user}"
respose = requests.get(url)
soup = bs(respose.text, "html.parser")
img_tag = soup.find("img", {"class": "avatar avatar-user width-full border color-bg-default"})
#print(f"https://github.com/{github_user}.png")
if img_tag:
    img = img_tag.get("src")
    print(img)
else:
    print("Avatar image not found")