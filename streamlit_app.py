import streamlit as st

# 페이지 선택
page = st.sidebar.selectbox("페이지를 선택하세요", ["나의 IB 학습자상 목표", "기타 페이지(추후 구현)"])

if page == "나의 IB 학습자상 목표":
    st.title("MY 학습자상 Green_에코 미션 app")

    # 1줄: 목표 학습자상 작성
    st.markdown("#### 1. 내가 목표로 하는 IB 학습자상")
    learner_profile = st.text_input("목표 학습자상을 입력하세요 (예: Inquirer, Thinker 등)")

    # 2줄: 학습자상 관련 사진 업로드
    st.markdown("#### 2. 학습자상과 관련된 사진을 올려보세요")
    uploaded_file = st.file_uploader("사진을 업로드하세요", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="업로드한 사진", use_column_width=True)

    # 3줄: 설명과 되고 싶은 이유 작성
    st.markdown("#### 3. 학습자상 설명과 되고 싶은 이유")
    description = st.text_area("학습자상에 대한 설명과 내가 되고 싶은  이유를 작성하세요")