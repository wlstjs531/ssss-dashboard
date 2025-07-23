import streamlit as st

# 페이지 선택
page = st.sidebar.selectbox(
    "페이지를 선택하세요",
    ["나의 2학기 목표 학습자상", "기후위기에 대응하는 식생활 습관 미션"]
)

if page == "나의 2학기 목표 학습자상":
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

elif page == "기후위기에 대응하는 식생활 습관 미션":
    st.title("에코 그린 식습관 미션")

    # 1줄: 기후위기에 대응하는 식생활 습관 미션 만들기
    st.markdown("#### 1. 기후위기에 대응하는 식생활 습관 미션 체크")
    mission1 = st.checkbox("채식 식단 선택")
    mission2 = st.checkbox("잔반 없이 먹기")
    mission3 = st.checkbox("텀블러 사용")
    mission4 = st.checkbox("지역 농산물 먹기")
    mission5 = st.checkbox("가공식품 줄이기")
    mission6 = st.checkbox("비닐봉투 사용 줄이기")

    # 2줄: MY 학습자상 관련한 식생활 습관 미션 활동 내용 작성
    st.markdown("#### 2. MY 학습자상 관련한 식생활 습관 미션 활동 내용 작성")
    activity_content = st.text_area("실천한 식생활 습관 미션 활동 내용을 작성하세요")

    # 3줄: 인증샷 올리기
    st.markdown("#### 3. 인증샷 올리기")
    uploaded_photo = st.file_uploader("인증샷을 업로드하세요", type=["png", "jpg", "jpeg"])
    if uploaded_photo is not None:
        st.image(uploaded_photo, caption="인증샷", use_column_width=True)

    # 4줄: 미션 스탬프 사진 올리기
    st.markdown("#### 4. 미션 스탬프 사진 올리기")
    stamp_photo = st.file_uploader("미션 스탬프 사진을 업로드하세요", type=["png", "jpg", "jpeg"], key="stamp")
    if stamp_photo is not None:
        st.image(stamp_photo, caption="미션 스탬프", use_column_width=True)