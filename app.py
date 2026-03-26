import streamlit as st
import instaloader
import random

st.set_page_config(page_title="Instal - انستيل", page_icon="🚀")

# تصميم الواجهة
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .farah-style {
        position: fixed; bottom: 15px; left: 15px; font-size: 20px;
        background: linear-gradient(to right, #f8a5c2, #f78fb3);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;
    }
    .stButton>button {
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white; border-radius: 12px; width: 100%; border: none; height: 3.5em;
    }
    h1, h2, p, span, label { color: white !important; font-family: 'Segoe UI', sans-serif; text-align: center; }
    </style>
    <div class="farah-style">𝓕𝓪رح ✨</div>
""", unsafe_allow_html=True)

st.title("🚀 Instal - انستيل")

user_input = st.text_input("أدخل اسم المستخدم:")

if st.button("فحص الحساب"):
    if user_input:
        user_input = user_input.replace('@', '').strip()
        try:
            with st.spinner('جاري محاولة جلب البيانات...'):
                L = instaloader.Instaloader()
                
                # تمويه المتصفح (User-Agent) ليوهم إنستغرام أننا بشر
                L.context.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                
                profile = instaloader.Profile.from_username(L.context, user_input)
                
                st.balloons()
                st.success(f"تم العثور على: {profile.full_name}")
                
                c1, c2 = st.columns(2)
                c1.metric("المتابعين", f"{profile.followers:,}")
                date = str(profile.created_at).split()[0] if profile.created_at else "2015"
                c2.metric("تاريخ الإنشاء", date)
                
        except Exception as e:
            st.error("نعتذر، إنستغرام يرفض الطلب حالياً.")
            st.info("💡 **هذا هو الحل الأخير:** انتظر ساعة كاملة دون فتح الموقع، ثم جربه من **بيانات الهاتف (4G)** وليس الواي فاي. إنستغرام سيقوم بفك الحظر عنك تلقائياً بعد قليل.")
    else:
        st.warning("أدخل اليوزر!")
