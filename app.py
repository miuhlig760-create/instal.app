import streamlit as st
import instaloader

st.set_page_config(page_title="Instal - انستيل", page_icon="📸")

# تصميم الواجهة الأنيق
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
    h1, h2, p, span, label { color: white !important; font-family: 'Segoe UI', sans-serif; }
    </style>
    <div class="farah-style">𝓕𝓪𝓻𝓪𝓱 ✨</div>
""", unsafe_allow_html=True)

st.title("🚀 انستيل - Instal")
st.write("البحث الآن يتم عبر حسابك الخاص لتجاوز القيود")

user_input = st.text_input("أدخل اسم المستخدم (Username) المراد فحصه:")

if st.button("فحص الحساب"):
    if user_input:
        user_input = user_input.replace('@', '').strip()
        try:
            with st.spinner('جاري تسجيل الدخول والبحث بأمان...'):
                L = instaloader.Instaloader()
                
                # تسجيل الدخول باستخدام حسابك الجديد
                L.login("anadaryyy", "mohammed_2009") 
                
                profile = instaloader.Profile.from_username(L.context, user_input)
                
                st.balloons()
                st.success(f"تم بنجاح: {profile.full_name}")
                
                c1, c2 = st.columns(2)
                c1.metric("المتابعين", f"{profile.followers:,}")
                
                # جلب تاريخ الإنشاء التقريبي
                date = str(profile.created_at).split()[0] if profile.created_at else "2015"
                c2.metric("تاريخ الإنشاء", date)
                
        except Exception as e:
            # رسالة مساعدة في حال طلب إنستغرام تأكيد هوية
            st.error("حدث خطأ! قد يحتاج إنستغرام لتأكيد هويتك.")
            st.info("💡 افتح تطبيق إنستغرام على موبايلك بحساب anadaryyy، وإذا ظهرت رسالة 'هل هذا أنت؟' اضغط 'نعم'. ثم جرب الموقع مرة أخرى.")
    else:
        st.warning("يرجى كتابة اليوزر!")
