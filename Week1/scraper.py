from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/573.36"
}

def fetch_website_contents(url):
    """
    Return the title and contents of the website from the given url;
    Truncate to 2,000 characters as a sensible limit.
    """

    response = requests.get(url, headers= header)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.title.string if soup.title else "No title found"

    if soup.body:
        for irrelevant in soup.body(['script', 'style', 'img', 'input']):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    return (title + "\n\n" + text)[:2000]


def fetch_website_links(url):
    """
    Return the links on the website at the given url.
    """

    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]


if __name__ == "__main__":
    print(fetch_website_contents("https://edwarddonner.com"))
    print(fetch_website_links("https://edwarddonner.com"))