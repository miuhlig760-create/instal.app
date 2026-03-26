import streamlit as st
import httpx
import re

st.set_page_config(page_title="Instal Pro", page_icon="✨")

# الستايل الفخم اللي طلبته
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1 { color: #00d2ff !important; text-align: center; font-family: 'Cairo', sans-serif; font-size: 45px; font-weight: bold; }
    .stButton>button { 
        background: linear-gradient(45deg, #00d2ff, #3a7bd5); 
        color: white !important; border-radius: 12px; width: 100%; border: none; height: 3.5em; font-weight: bold; font-size: 22px;
    }
    input { font-size: 22px !important; font-weight: bold !important; text-align: center !important; color: #00d2ff !important; background-color: #111 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("انستيل - INSTAL")

user_input = st.text_input("أدخل اسم المستخدم:")

if st.button("فحص الحساب الآن 🔍"):
    if user_input:
        user_input = user_input.replace('@', '').strip()
        try:
            with st.spinner('جاري تخطي الحواجز...'):
                # هذه الـ Headers توهم إنستغرام أنك تستخدم متصفح حقيقي من جهاز كمبيوتر
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "none",
                    "Upgrade-Insecure-Requests": "1"
                }
                
                url = f"https://www.instagram.com/{user_input}/"
                
                # استخدام Session للحفاظ على الاتصال
                with httpx.Client(headers=headers, follow_redirects=True, timeout=10.0) as client:
                    response = client.get(url)
                    
                    if response.status_code == 200:
                        # استخراج البيانات من الـ Meta Tags
                        meta = re.search(r'meta content="([\d,.]+[KMB]?) Followers', response.text)
                        
                        if meta:
                            st.balloons()
                            st.success(f"تم العثور على: {user_input}")
                            st.metric("المتابعين", meta.group(1))
                        else:
                            st.warning("إنستغرام يطلب تسجيل الدخول لرؤية هذا الحساب.")
                    else:
                        st.error("السيرفر محظور حالياً من قبل إنستغرام.")
                        st.info("💡 نصيحة: جرب تفتح الموقع من 'بيانات الهاتف' وليس الواي فاي.")
        except Exception as e:
            st.error("حدث خطأ في الاتصال.")
    else:
        st.warning("دخل اليوزر يا غالي!")

# تفاعل فرح
if st.button("𝓕𝓪𝓻𝓪𝓱 ✨"):
    st.balloons()
    st.snow()
