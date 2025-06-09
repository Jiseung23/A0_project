import streamlit as st

# MBTI별 색상 매핑
mbti_colors = {
    "INTP": "#B2EBF2", "INTJ": "#B2EBF2", "ENTP": "#B2EBF2", "ENTJ": "#B2EBF2",  # NT: 파랑
    "INFP": "#F8BBD0", "INFJ": "#F8BBD0", "ENFP": "#F8BBD0", "ENFJ": "#F8BBD0",  # NF: 핑크
    "ISTJ": "#FFF9C4", "ISFJ": "#FFF9C4", "ESTJ": "#FFF9C4", "ESFJ": "#FFF9C4",  # SJ: 노랑
    "ISTP": "#C8E6C9", "ISFP": "#C8E6C9", "ESTP": "#C8E6C9", "ESFP": "#C8E6C9",  # SP: 그린
}

# 배경 스타일
st.markdown("""
    <style>
    body {
        background-color: #FDF6EC;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>🍿 MBTI로 찾는 과학·수학 명작 영화 🎬</h1>", unsafe_allow_html=True)
st.write("")

# 영화 추천 데이터 (생략된 예시, 전체 데이터는 앞 대화 참고)
mbti_movies = {
    "INTP": [
        {"title": "《굿 윌 헌팅》", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"},
        {"title": "《엑스 마키나》", "img": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg"},
        {"title": "《인터스텔라》", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"}
    ],
    # ... 모든 16유형 포함 (이전 답변 참고)
}

mbti_list = list(mbti_movies.keys())
selected_mbti = st.session_state.get("selected_mbti", "")

# 🔘 유형 버튼 표시
st.markdown("### 🧠 MBTI 유형 선택")

button_cols = st.columns(4)
for i, mbti in enumerate(mbti_list):
    with button_cols[i % 4]:
        button_style = f"""
            <style>
            div[data-testid="stButton"] > button {{
                background-color: {mbti_colors[mbti]};
                border-radius: 12px;
                border: 2px solid #ccc;
                padding: 0.5em 1em;
                margin: 0.2em 0;
                width: 100%;
                font-weight: bold;
            }}
            </style>
        """
        st.markdown(button_style, unsafe_allow_html=True)
        if st.button(mbti, key=mbti):
            st.session_state.selected_mbti = mbti
            selected_mbti = mbti

# 🎬 결과 출력
if selected_mbti:
    st.markdown("---")
    st.markdown(f"### 🎯 {selected_mbti} 유형에게 추천하는 영화")

    movie_data = mbti_movies[selected_mbti]
    cols = st.columns(3)
    for i, movie in enumerate(movie_data):
        with cols[i]:
            st.image(movie["img"], width=180)
            st.markdown(f"**🎬 {movie['title']}**")

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
