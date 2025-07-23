import streamlit as st

# 페이지 구성: 사이드바에서 페이지 선택
st.set_page_config(page_title="IB 학습자상 스탬프북", layout="centered")

# 페이지 1: 학습자상 기록
st.title("📘 IB 학습자상 스탬프북")
st.subheader("✨ 나의 실천이 자라나는 앱 - 1단계")

# 1줄: 학습자상 이름 입력
st.markdown("### 1️⃣ 목표로 하는 IB 학습자상을 작성하세요")
learner_profile = st.text_input("예: Risk-taker (도전가), Caring (배려하는 사람) 등")

# 2줄: 관련 사진 업로드
st.markdown("### 2️⃣ 학습자상과 관련된 활동 사진을 올려보세요")
uploaded_image = st.file_uploader("활동 사진 업로드", type=["png", "jpg", "jpeg"])

# 3줄: 설명과 되고 싶은 이유 입력
st.markdown("### 3️⃣ 이 학습자상이 되고 싶은 이유와 설명을 적어보세요")
description = st.text_area("학습자상에 대한 설명과 되고 싶은 이유를 자유롭게 작성하세요.")

# 저장 버튼
if st.button("💾 저장하기"):
    if learner_profile and uploaded_image and description:
        st.success("✅ 성공적으로 저장되었습니다!")
    else:
        st.warning("⚠️ 모든 항목을 입력해야 저장할 수 있습니다.")

# 이미지 미리보기
if uploaded_image:
    st.image(uploaded_image, caption="업로드한 사진", use_column_width=True)
