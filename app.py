import streamlit as st
import instaloader

# إعدادات الصفحة
st.set_page_config(page_title="Instal - انستيل", page_icon="✨")

# كود الجافا سكريبت للحلفية التفاعلية (Particles.js)
# هذا الكود يجعل الخلفية تتفاعل مع اللمس والماوس
st.markdown("""
    <canvas id="canvas" style="position: fixed; top: 0; left: 0; z-index: -1;"></canvas>
    <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    let particlesArray = [];

    const mouse = { x: null, y: null, radius: 150 };

    window.addEventListener('mousemove', function(event) {
        mouse.x = event.x;
        mouse.y = event.y;
    });

    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 5 + 1;
            this.speedX = Math.random() * 3 - 1.5;
            this.speedY = Math.random() * 3 - 1.5;
        }
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            if (this.size > 0.2) this.size -= 0.1;
            
            // التفاعل مع الماوس
            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let distance = Math.sqrt(dx*dx + dy*dy);
            if (distance < mouse.radius) {
                this.x -= dx/10;
                this.y -= dy/10;
            }
        }
        draw() {
            ctx.fillStyle = '#f8a5c2'; // لون قلوب فرح
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function init() {
        for (let i = 0; i < 100; i++) { particlesArray.push(new Particle()); }
    }
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particlesArray.length; i++) {
            particlesArray[i].update();
            particlesArray[i].draw();
            if (particlesArray[i].size <= 0.3) {
                particlesArray.splice(i, 1);
                i--;
                particlesArray.push(new Particle());
            }
        }
        requestAnimationFrame(animate);
    }
    init();
    animate();
    </script>
    
    <style>
    .stApp { background: transparent; }
    h1 { color: #00d2ff !important; text-align: center; font-size: 45px; font-weight: 800; }
    .stButton>button {
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white; border-radius: 15px; height: 3em; width: 100%; border: none;
    }
    .farah-btn {
        color: #f8a5c2; font-size: 25px; font-weight: bold; cursor: pointer; text-align: center; display: block;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>انستيل - INSTAL</h1>", unsafe_allow_html=True)

user_input = st.text_input("أدخل اليوزر للفحص:")

if st.button("بدء الفحص 🔍"):
    if user_input:
        st.write("جاري العمل على طلبك...")
        # هنا تضع كود الـ instaloader اللي عملناه سابقاً
    else:
        st.warning("دخل اليوزر يا غالي!")

st.write("---")
# اسم فرح كتفاعل إضافي
if st.button("𝓕𝓪𝓻𝓪𝓱 ✨"):
    st.balloons()
    st.success("شكراً لدعمك!")
