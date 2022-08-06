from bs4 import BeautifulSoup
import requests
import pandas as pd

articles = []


page_no = 1

for page_no in range(1, 51):
    url = "https://www.jugantor.com/all-news/sports/cricket?page=" + str(page_no)
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    name_box = soup.find_all('div', attrs={'class': 'col-8 align-self-end pl-4'})

    # empty list
    my_list = []

    for x in name_box:
        y = x.find('h6', attrs={'class': 'text-body'})
        l = x.find('a').get('href')
        my_list.append(l)

    print(my_list)

    for item in my_list:
        
        url = item
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        contentbox = soup.find('div', attrs={'id': 'myText'})

        title = soup.find('h3', attrs={'class': 'font-weight-bolder'})
        title = title.text

        para = contentbox.find_all('p')
        
        c = ""
        for x in para:
            c = c + x.text

        article_dict = {
            "title": title,
            "category": "cricket",
            "article": c
        }
        print("articles addeing----")
        articles.append(article_dict)

    print("page completed:" + str(page_no))



dataframe = pd.DataFrame(articles)
dataframe.to_csv(r"C:\\Users\Saifur\Desktop\\Project\srapper\\news.csv", mode="a", index=False)