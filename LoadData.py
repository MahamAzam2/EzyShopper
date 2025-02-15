import json
import os
class LoadData:
    def __init__(self):
        self.data = []
        self.path = 'F:\\Projects\\EzyShopper\\DataBase\\carts.json'  

        
    def load(self):
        with open(self.path, 'r') as f:
            self.data = json.load(f)
            
    def GetTitle(self):
        titlelist =[]
        for i in self.data:
            for product in i["products"]:
                titlelist.append(product['title'])
        return titlelist
    def allProducts(self):
        productsList = []
        for i in self.data:
            for product in i["products"]:
                productsList.append({
                "title": product.get("title"),
                "price": product.get("price"),
                "thumbnail": product.get("thumbnail"),
                })
        return productsList                    
    def PrintData(self):
        for i in self.data.items():
            print(i['title'])
            print('------------------------')
        
