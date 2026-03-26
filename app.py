import streamlit as st
import instaloader

st.set_page_config(page_title="Instal - انستيل", page_icon="📸")

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
        color: white; border-radius: 12px; width: 100%; border: none; height: 3em;
    }
    h1, h2, p, span, label { color: white !important; }
    </style>
    <div class="farah-style">𝓕𝓪𝓻𝓪𝓱 ✨</div>
""", unsafe_allow_html=True)

st.title("🚀 انستيل - Instal")
user_input = st.text_input("أدخل اسم المستخدم (Username):")

if st.button("فحص الحساب"):
    if user_input:
        user_input = user_input.replace('@', '').strip()
        try:
            with st.spinner('جاري التحقق...'):
                L = instaloader.Instaloader()
                # هذه السطور تساعد في تجاوز بعض القيود
                L.context.user_agent = 'Mozilla/5.0' 
                profile = instaloader.Profile.from_username(L.context, user_input)
                
                st.balloons()
                st.success(f"الاسم: {profile.full_name}")
                
                c1, c2 = st.columns(2)
                c1.metric("المتابعين", f"{profile.followers:,}")
                date = str(profile.created_at).split()[0] if profile.created_at else "تقديري: 2014"
                c2.metric("تاريخ الإنشاء", date)
        except Exception:
            st.error("إنستغرام يطلب تسجيل الدخول لهذا اليوزر. جرب يوزر آخر أو ارفع الموقع أونلاين.")