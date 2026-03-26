import streamlit as st
import httpx
import re
import json

# إعدادات الصفحة
st.set_page_config(page_title="Instal Pro", page_icon="✨")

# الستايل المحدث (بدون صاروخ، خط عريض، وتفاعل فرح)
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1 { color: #00d2ff !important; text-align: center; font-family: 'Cairo', sans-serif; font-size: 40px; }
    .stButton>button { 
        background: linear-gradient(45deg, #00d2ff, #3a7bd5); 
        color: white !important; border-radius: 12px; width: 100%; border: none; height: 3.5em; font-weight: bold; font-size: 20px;
    }
    input { font-size: 20px !important; font-weight: bold !important; text-align: center !important; }
    .farah-btn { color: #f8a5c2; font-size: 30px; font-weight: bold; cursor: pointer; text-align: center; display: block; margin-top: 20px; text-decoration: none; }
    </style>
""", unsafe_allow_html=True)

st.title("انستيل - INSTAL")

user_input = st.text_input("أدخل اسم المستخدم:")

if st.button("فحص الحساب الآن"):
    if user_input:
        user_input = user_input.replace('@', '').strip()
        try:
            with st.spinner('جاري استخراج البيانات...'):
                # إرسال طلب كأننا متصفح حقيقي تماماً
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Referer": "https://www.google.com/"
                }
                
                url = f"https://www.instagram.com/{user_input}/"
                
                with httpx.Client(headers=headers, follow
