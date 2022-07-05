from bs4 import BeautifulSoup
import requests


url = "https://en.wikipedia.org/wiki/Environmental_racism"


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="vector-body")
    all_p_tags = results.find_all("p")
    result = 0
    for tag_p in all_p_tags:
        tag_content = tag_p.text
        if "citation needed" in tag_content:
            result += 1
    return result


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="vector-body")
    all_p_tags = results.find_all("p")
    result = ""
    for p_tag in all_p_tags:
        tag_content = p_tag.text
        if "citation needed" in tag_content:
            result += tag_content
            result += "\n\n"
    return result


if __name__ == "__main__":
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
