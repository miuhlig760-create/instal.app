import streamlit as st
import httpx
import re

# إعدادات الصفحة
st.set_page_config(page_title="Instal Pro", page_icon="✨")

# الستايل المحدث (بدون صاروخ، خط عريض، وتفاعل فرح)
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1 { color: #00d2ff !important; text-align: center; font-family: 'Cairo', sans-serif; font-size: 45px; font-weight: 800; }
    .stButton>button { 
        background: linear-gradient(45deg, #00d2ff, #3a7bd5); 
        color: white !important; border-radius: 12px; width: 100%; border: none; height: 3.5em; font-weight: bold; font-size: 22px;
    }
    input { font-size: 22px !important; font-weight: bold !important; text-align: center !important; color: #00d2ff !important; }
    .farah-btn { color: #f8a5c2; font-size: 30px; font-weight: bold; cursor: pointer; text-align: center; display: block; margin-top: 20px; text-decoration: none; }
    </style>
""", unsafe_allow_html=True)

st.title("انستيل - INSTAL")

user_input = st.text_input("أدخل اسم المستخدم:")

if st.button("فحص الحساب الآن 🔍"):
    if user_input:
        user_input = user_input.replace('@', '').strip()
        try:
            with st.spinner('جاري جلب البيانات...'):
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
                url = f"https://www.instagram.com/{user_input}/"
                
                with httpx.Client(headers=headers, follow_redirects=True) as client:
                    response = client.get(url)
                    
                    if response.status_code == 200:
                        # استخراج المتابعين والمنشورات من كود الصفحة
                        meta = re.search(r'meta content="([\d,.]+[KMB]?) Followers, ([\d,.]+[KMB]?) Following, ([\d,.]+[KMB]?) Posts', response.text)
                        
                        if meta:
                            st.balloons()
                            st.success(f"الحساب: {user_input}")
                            c1, c2 = st.columns(2)
                            c1.metric("المتابعين", meta.group(1))
                            c2.metric("المنشورات", meta.group(3))
                        else:
                            st.warning("الحساب خاص أو لم يتم العثور على بيانات.")
                    else:
                        st.error("تعذر الاتصال بإنستغرام حالياً.")
        except Exception as e:
            st.error("حدث خطأ أثناء الفحص.")
    else:
        st.warning("يرجى إدخال اليوزر!")

# زر فرح التفاعلي
st.write("---")
if st.button("𝓕𝓪𝓻𝓪𝓱 ✨"):
    st.balloons()
    st.snow()
    st.markdown("<h2 style='text-align: center; color: #f8a5c2;'>❤️ 𝓕𝓪𝓻𝓪𝓱 ❤️</h2>", unsafe_allow_html=True)
