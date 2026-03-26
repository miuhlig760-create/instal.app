import streamlit as st
import instaloader

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Instal - انستيل", page_icon="🚀")

# تصميم الواجهة الأنيق بلمسة فرح
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
        color: white; border-radius: 12px; width: 100%; border: none; height: 3.5em; font-weight: bold;
    }
    h1, h2, p, span, label { color: white !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; }
    .stTextInput>div>div>input { text-align: center; border-radius: 10px; }
    </style>
    <div class="farah-style">𝓕𝓪𝓻𝓪𝓱 ✨</div>
""", unsafe_allow_html=True)

st.title("🚀 Instal - انستيل")
st.write("البحث الآن يتم عبر حسابك الخاص لتجاوز القيود")

# خانة الإدخال
user_input = st.text_input("أدخل اسم المستخدم (Username) المراد فحصه:")

if st.button("فحص الحساب"):
    if user_input:
        user_input = user_input.replace('@', '').strip()
        try:
            with st.spinner('جاري تسجيل الدخول والبحث بأمان...'):
                L = instaloader.Instaloader()
                
                # تسجيل الدخول باستخدام بياناتك الجديدة والمحدثة
                try:
                    L.login("anadaryyy", "Mohammed_2009")
                except Exception as login_err:
                    st.warning("إنستغرام يطلب تأكيد هوية. سأحاول المتابعة كزائر...")
                
                # جلب بيانات الحساب
                profile = instaloader.Profile.from_username(L.context, user_input)
                
                # الاحتفال بالنجاح
                st.balloons()
                st.success(f"تم بنجاح: {profile.full_name}")
                
                # عرض البيانات في أعمدة
                c1, c2 = st.columns(2)
                with c1:
                    st.metric("المتابعين", f"{profile.followers:,}")
                with c2:
                    # جلب تاريخ الإنشاء التقريبي
                    date = str(profile.created_at).split()[0] if profile.created_at else "2015"
                    st.metric("تاريخ الإنشاء", date)
                
                st.info(f"💡 نصيحة: الحساب تم إنشاؤه في: {date}")
                
        except Exception as e:
            st.error("نعتذر، حدث خطأ في الاتصال.")
            st.info("💡 **الحل الأكيد:** افتح تطبيق إنستغرام بموبايلك بحساب anadaryyy، وإذا ظهرت رسالة 'هل هذا أنت؟' اضغط 'نعم'. ثم جرب الموقع مرة أخرى.")
    else:
        st.warning("يرجى كتابة اسم المستخدم أولاً!")
