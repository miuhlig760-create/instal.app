import streamlit as st
import instaloader
import time

# إعدادات الصفحة
st.set_page_config(page_title="Instal - انستيل", page_icon="✨")

# دالة لتشغيل صوت الكليك
def play_click():
    sound_url = "https://www.soundjay.com/buttons/sounds/button-16.mp3"
    st.markdown(f'<audio autoplay><source src="{sound_url}" type="audio/mp3"></audio>', unsafe_allow_html=True)

# الستايل المتقدم
st.markdown("""
    <style>
    /* خلفية داكنة فخمة */
    .stApp {
        background-color: #050505;
    }

    /* تحسين الخط وجعله واضحاً جداً */
    h1, h2, p, span, label, input {
        font-family: 'Cairo', sans-serif;
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    /* تصميم خانة الإدخال - خط واضح وعريض */
    .stTextInput>div>div>input {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #00d2ff !important;
        background-color: #111 !important;
        border: 2px solid #3a7bd5 !important;
        border-radius: 15px !important;
        text-align: center;
    }

    /* الزر بستايل جديد وبدون أيقونات */
    .stButton>button {
        background: linear-gradient(45deg, #ff00cc, #3333ff);
        color: white !important;
        border-radius: 15px;
        padding: 20px;
        font-size: 24px !important;
        border: none;
        width: 100%;
        transition: 0.3s;
    }

    /* تأثير الضغط على اسم فرح (القلوب) */
    .farah-btn {
        background: none;
        border: none;
        color: #f8a5c2;
        font-size: 30px;
        font-family: 'Cursive', sans-serif;
        font-weight: bold;
        cursor: pointer;
        transition: 0.5s;
        text-decoration: none;
    }
    
    /* إخفاء الصاروخ وأي أيقونات إضافية */
    .st-emotion-cache-10trblm { display: none; } 
    </style>
""", unsafe_allow_html=True)

# العنوان
st.markdown("<h1 style='text-align: center; font-size: 50px;'>انستيل - INSTAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px; color: #888;'>الفحص المتقدم للحسابات</p>", unsafe_allow_html=True)

# واجهة البحث
user_input = st.text_input("ادخل اسم المستخدم:")

if st.button("بدء التحليل"):
    if user_input:
        play_click()
        user_input = user_input.replace('@', '').strip()
        try:
            with st.spinner('جاري العمل...'):
                L = instaloader.Instaloader()
                L.context.user_agent = "Mozilla/5.0"
                profile = instaloader.Profile.from_username(L.context, user_input)
                
                st.success(f"الاسم: {profile.full_name}")
                c1, c2 = st.columns(2)
                c1.metric("المتابعين", f"{profile.followers:,}")
                date = str(profile.created_at).split()[0] if profile.created_at else "2015"
                c2.metric("التاريخ", date)
        except:
            st.error("الموقع في حالة حظر مؤقت، جرب لاحقاً.")

# الجزء الخاص بـ "فرح" والقلوب
st.write("---")
col_f, _ = st.columns([1, 4])
with col_f:
    if st.button("𝓕𝓪𝓻𝓪𝓱"):
        st.balloons() # سيظهر بالونات على شكل قلوب وألوان احتفالية
        st.snow() # تأثير إضافي ناعم
        st.markdown("<h3 style='color: #ff00cc; text-align: center;'>❤️ ✨ ❤️</h3>", unsafe_allow_html=True)
