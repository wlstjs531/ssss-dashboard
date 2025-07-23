import streamlit as st

# IB 학습자상 명칭과 설명
ib_profiles = [
    {"name": "Inquirer", "desc": "호기심이 많고, 탐구하는 자세를 가진 학습자"},
    {"name": "Knowledgeable", "desc": "지식이 풍부하고, 다양한 주제에 대해 이해하는 학습자"},
    {"name": "Thinker", "desc": "비판적으로 사고하고, 문제를 해결하는 학습자"},
    {"name": "Communicator", "desc": "의사소통이 뛰어나고, 다양한 방식으로 생각을 표현하는 학습자"},
    {"name": "Principled", "desc": "정직하고, 공정하며, 책임감 있는 학습자"},
    {"name": "Open-minded", "desc": "다양성을 존중하고, 열린 마음을 가진 학습자"},
    {"name": "Caring", "desc": "배려심이 많고, 타인을 돕는 학습자"},
    {"name": "Risk-taker", "desc": "도전정신이 강하고, 새로운 것에 도전하는 학습자"},
    {"name": "Balanced", "desc": "균형 잡힌 삶을 추구하는 학습자"},
    {"name": "Reflective", "desc": "자신을 성찰하고, 발전을 위해 노력하는 학습자"},
]

st.title("IB 학습자상 실천 체크리스트")

for profile in ib_profiles:
    st.subheader(profile["name"])
    st.write(profile["desc"])
    checked = st.checkbox(f"{profile['name']} 관련 활동을 실천했나요?", key=profile["name"])
    if checked:
        st.success(f"{profile['name']} 활동을 실천하셨군요! 👍")
    st.markdown("---")
   