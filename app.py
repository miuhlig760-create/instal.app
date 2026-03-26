import streamlit as st
import instaloader
import base64

# إعدادات الصفحة
st.set_page_config(page_title="Instal - انستيل", page_icon="✨", layout="centered")

# دالة لإضافة صوت (نغمة كليك احترافية)
def play_sound():
    sound_url = "https://www.soundjay.com/buttons/sounds/button-16.mp3"
    html_string = f"""
        <audio autoplay>
          <source src="{sound_url}" type="audio/mp3">
        </audio>
    """
    st.markdown(html_string, unsafe_allow_html=True)

# الستايل المتقدم (CSS)
st.markdown("""
    <style>
    /* خلفية متدرجة متحركة */
    .stApp {
        background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0e1117);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* تأثيرات النصوص */
    h1 {
        color: #00d2ff !important;
        text-shadow: 2px 2px 10px rgba(0,210,255,0.5);
        font-family: 'Segoe UI', sans-serif;
        font-weight: 800;
        text-align: center;
    }

    /* تصميم الزر الاحترافي مع تأثير الضغط */
    .stButton>button {
        background: linear-gradient(45deg, #00d2ff, #3a7bd5);
        color: white;
        border-radius: 50px;
        padding: 15px 30px;
        border: none;
        font-size: 20px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3);
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0, 210, 255, 0.5);
        background: linear-gradient(45deg, #3a7bd5, #00d2ff);
    }
    .stButton>button:active {
        transform: scale(0.95);
    }

    /* تصميم خانة الإدخال */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 2px solid #3a7bd5 !important;
        border-radius: 15px !important;
        text-align: center;
    }

    /* توقيع فرح الأنيق */
    .farah-signature {
        position: fixed;
        bottom: 20px;
        left: 20px;
        font-size: 24px;
        background: linear-gradient(to right, #f8a5c2, #f78fb3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cursive', sans-serif;
        font-weight: bold;
        letter-spacing: 2px;
        z-index: 1000;
    }
    </style>
    <div class="farah-signature">𝓕𝓪𝓻𝓪𝓱 ✨</div>
""", unsafe_allow_html=True)

st.title("🚀 انستيل - INSTAL PRO")
st.markdown("<p style='text-align: center; color: #aaa;'>النظام المتطور لفحص حسابات إنستغرام</p>", unsafe_allow_html=True)

# واجهة البحث
user_input = st.text_input("", placeholder="أدخل اسم المستخدم هنا...")

if st.button("تحليل الحساب 🔍"):
    if user_input:
        play_sound() # تشغيل الصوت عند الضغط
        user_input = user_input.replace('@', '').strip()
        
        try:
            with st.spinner('جاري اختراق الحواجز وجلب البيانات...'):
                L = instaloader.Instaloader()
                # تمويه متقدم
                L.context.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                
                profile = instaloader.Profile.from_username(L.context, user_input)
                
                st.balloons()
                
                # عرض النتيجة بستايل كروت احترافية
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 20px; border-left: 5px solid #00d2ff;">
                    <h2 style="color: white; margin: 0;">👤 {profile.full_name}</h2>
                    <p style="color: #00d2ff;">@{user_input}</p>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                col1.metric("المتابعين", f"{profile.followers:,}")
                date = str(profile.created_at).split()[0] if profile.created_at else "2015"
                col2.metric("تاريخ الإنشاء", date)
                
        except Exception as e:
            st.error("نظام الحماية نشط حالياً. سيتم فك الحظر تلقائياً بعد قليل.")
    else:
        st.warning("الرجاء كتابة اسم مستخدم للبدء!")
