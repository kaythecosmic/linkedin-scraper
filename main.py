# Make sure to populate the `payload` file before running
import requests
from bs4 import BeautifulSoup
from payload import cookies, headers
from json import loads

# input your target linkedin profile link
# for example, below is the link to Lex Fridman's LinkedIn
target = "https://www.linkedin.com/in/lexfridman/"


def fetchUserData(link: str):
    """
    Scrapes user name and title of the user form their LinkedIn Profile.

    Parameters:
    link (string): Link to user profile.

    Returns:
    userData (dictionary): dictionary with keys: (name, title).
    """
    try:
        response = requests.get(link, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.findAll("code")
        jsonData = loads(data[len(data) - 3].text)
        jdIncluded = jsonData["included"]

        # setting default values to "Not Found", can be handled in case of any anomaly
        name = "Not Found"
        title = "Not Found"
        for item in jdIncluded:
            try:
                if "profilePicture" in dict.keys(item):
                    name = item["profilePicture"]["a11yText"]
                    if "headline" in dict.keys(item):
                        title = item["headline"]
            except Exception as e:
                print("Inner Error: ", e)
                pass
        userData = {"name": name, "title": title}
        return userData
    except Exception as e:
        print("Error: ", e)
        pass


# returns an object of schema: obj(name: string, title: string)
targetData = fetchUserData(target)
print(targetData)
