import streamlit as st
import httpx
import re

# إعدادات الواجهة مع ستايل "فرح" التفاعلي
st.set_config(page_title="Instal Pro", page_icon="✨")

st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1 { color: #00d2ff !important; text-align: center; font-family: 'Cairo', sans-serif; }
    .stButton>button { 
        background: linear-gradient(45deg, #00d2ff, #3a7bd5); 
        color: white; border-radius: 10px; width: 100%; border: none; height: 3em;
    }
    .farah-touch { color: #f8a5c2; font-weight: bold; cursor: pointer; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 انستيل - النسخة السريعة")

user_input = st.text_input("أدخل اسم المستخدم (بدون @):")

if st.button("تحليل الآن 🔍"):
    if user_input:
        user_input = user_input.strip()
        try:
            with st.spinner('جاري كسر الحظر وجلب البيانات...'):
                # استخدام متصفح وهمي متطور لتجاوز الحماية
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Accept-Language": "en-US,en;q=0.9"
                }
                
                # جلب البيانات مباشرة من رابط JSON العام لإنستغرام
                url = f"https://www.instagram.com/{user_input}/?__a=1&__d=dis"
                
                with httpx.Client(headers=headers, follow_redirects=True) as client:
                    response = client.get(url)
                    
                    if response.status_code == 200:
                        data = response.json()
                        user_data = data['graphql']['user']
                        
                        st.balloons()
                        st.success(f"تم العثور على: {user_data['full_name']}")
                        
                        col1, col2 = st.columns(2)
                        col1.metric("المتابعين", f"{user_data['edge_followed_by']['count']:,}")
                        # حساب تقريبي لتاريخ الإنشاء بناءً على الـ ID (تقنية احترافية)
                        insta_id = int(user_data['id'])
                        year = "2010-2012" if insta_id < 20000000 else "2013-2015" if insta_id < 500000000 else "2016-2024"
                        col2.metric("فترة الإنشاء", year)
                    else:
                        st.error("إنستغرام لا يزال يرفض الاتصال المباشر.")
                        st.info("💡 **جرب هذه الخدعة:** ادخل على الموقع من متصفح (Incognito) أو "نافذة خاصة" في موبايلك وسيشتغل!")
        except Exception as e:
            st.warning("الحساب خاص (Private) أو اليوزر غير صحيح.")
    else:
        st.warning("اكتب اليوزر أولاً!")

# تفاعل فرح
if st.button("𝓕𝓪𝓻𝓪𝓱 ✨"):
    st.snow()
    st.write("❤️ تحية من المطورة فرح ❤️")
