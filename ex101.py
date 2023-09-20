import requests
#  Write a Python program to access and print a URL's content to the console.

def url_cont(url):
    res = requests.get(url)
    return res.text

if __name__ == "__main__":
    link = "https://www.duckduckgo.com"
    print(url_cont(link))