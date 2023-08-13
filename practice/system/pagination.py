import requests
import json

def total_page(url):
    response = requests.get(url, verify=True)
    data = response.json()
    total_pages = data["total_pages"]
    return total_pages

def get_data(url):
    all_data = []
    total_pages = total_page(url)
    
    for page_num in range(1,total_pages+1):
        # url with parameter
        url_ = url + f"?page={page_num}"
        
        response = requests.get(url_)
        data = response.json()["data"]
        all_data.append(data)
        
    return all_data
    
url = "https://jsonmock.hackerrank.com/api/transactions"
print (get_data(url))
