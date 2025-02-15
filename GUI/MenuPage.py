import streamlit as st
import sys
import os

# Ensure Streamlit can find LoadData.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LoadData import LoadData  

class Page:
    def __init__(self):
        self.obj = LoadData()
        self.obj.load() 
    
    def SearchBox(self):
        st.text_input("Or enter product name:", "")

    def products(self):
        products = self.obj.allProducts()  
        for i in products:
            print(i)

        # if not products:
        #     st.write("No products found.")
        #     return

        # card_css = """
        # <style>
        #     .product-card {
        #         display: flex;
        #         flex-direction: column;
        #         align-items: center;
        #         text-align: center;
        #         background: white;
        #         padding: 15px;
        #         border-radius: 12px;
        #         box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        #         transition: transform 0.2s ease-in-out;
        #         margin-bottom: 10px;
        #     }
        #     .product-card:hover {
        #         transform: scale(1.05);
        #     }
        #     .product-image {
        #         width: 150px;
        #         height: 150px;
        #         object-fit: contain;
        #         border-radius: 10px;
        #     }
        #     .product-title {
        #         font-size: 16px;
        #         font-weight: bold;
        #         margin-top: 10px;
        #     }
        #     .product-price {
        #         font-size: 14px;
        #         color: green;
        #         margin-top: 5px;
        #     }
        # </style>
        # """

        # st.markdown(card_css, unsafe_allow_html=True)  # Apply CSS

        # # **Display products in a grid layout**
        # cols = st.columns(3)  # 3 cards per row

        # for i in products:
        #     print(type(i))
        #     if isinstance(i, dict):
        #         with cols[index % 3]:  # Place in grid
        #             st.markdown(
        #                 f"""
        #                 <div class="product-card">
        #                     <img class="product-image" src=">
        #                     <div class="product-title">{i['title']}</div>
        #                     <div class="product-price">💲 </div>
        #                 </div>
        #                 """,
        #                 unsafe_allow_html=True,
        #             )
        #     else:
        #         print('no dict')

obj = Page()
obj.SearchBox()
obj.products()
