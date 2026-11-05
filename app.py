import streamlit as st
from utils import calculate_average, calculate_percentage, convert_length

st.set_page_config(page_title="Talaba Yordamchisi", page_icon="🎓", layout="centered")
st.title("🎓 Talaba Yordamchisi")
st.caption("O‘zbek tilidagi oddiy va bepul o‘quv kalkulyatorlari")

tab1, tab2, tab3 = st.tabs(["📚 O‘rtacha baho", "％ Foiz", "📏 Uzunlik"])

with tab1:
    st.subheader("Baholarning o‘rtacha qiymati")
    raw = st.text_input("Baholarni vergul bilan kiriting", "5, 4, 5, 3")
    try:
        grades = [float(x.strip()) for x in raw.split(",") if x.strip()]
        if grades:
            st.metric("O‘rtacha baho", f"{calculate_average(grades):.2f}")
        else:
            st.info("Kamida bitta baho kiriting.")
    except ValueError:
        st.error("Faqat son kiriting. Masalan: 5, 4, 3")

with tab2:
    st.subheader("Foizni hisoblash")
    a = st.number_input("Son", min_value=0.0, value=200.0)
    b = st.number_input("Foiz (%)", min_value=0.0, value=15.0)
    st.metric(f"{a:g} ning {b:g} foizi", f"{calculate_percentage(a, b):g}")

with tab3:
    st.subheader("Uzunlik birliklarini aylantirish")
    value = st.number_input("Qiymat", min_value=0.0, value=100.0)
    source = st.selectbox("Qaysi birlikdan?", ["mm", "cm", "m", "km"])
    target = st.selectbox("Qaysi birlikka?", ["mm", "cm", "m", "km"], index=2)
    st.metric("Natija", f"{convert_length(value, source, target):g} {target}")

st.divider()
st.caption("Loyiha ochiq kodli. Taklif va xatolar uchun GitHub Issues bo‘limidan foydalaning.")
