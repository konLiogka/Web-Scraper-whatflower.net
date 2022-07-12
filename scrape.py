import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data=[]   
    string = soup.find_all('figure', class_= "wp-caption alignleft")

    for i in string:
        item = {}
        for k in i.find_all('figcaption', class_ = "wp-caption-text"):
            item["Names"] = k.get_text()   
        for j in i.find_all('a'):
            link = "https://whatflower.net" + j['href']
            item["Info"] = link
        data.append(item)                  
    return data
    
def export_data(data):
    df = pd.DataFrame(data)
    df.to_excel("plant_names.xlsx")
if __name__ == '__main__':
    data = get_data("https://whatflower.net/")
    export_data(data)
    print("done")


        
    






 
 
