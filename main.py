import streamlit as st

# MBTI별 파스텔 색상
mbti_colors = {
    "INTP": "#B2EBF2", "INTJ": "#AEDFF7", "ENTP": "#B2DFDB", "ENTJ": "#B39DDB",
    "INFP": "#F8BBD0", "INFJ": "#CE93D8", "ENFP": "#FFCCBC", "ENFJ": "#FFAB91",
    "ISTJ": "#FFF9C4", "ISFJ": "#DCEDC8", "ESTJ": "#FFD54F", "ESFJ": "#FFF176",
    "ISTP": "#C8E6C9", "ISFP": "#A5D6A7", "ESTP": "#80CBC4", "ESFP": "#FFCDD2",
}

# 영화 추천 목록
mbti_movies = {
    "INTP": [
        {"title": "굿 윌 헌팅", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"},
        {"title": "엑스 마키나", "img": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg"},
        {"title": "인터스텔라", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"}
    ],
    # 나머지 15개 유형도 이전 응답에서 이어 붙이세요.
}

st.set_page_config(page_title="MBTI 영화 추천", layout="wide")

st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>MBTI로 찾는 과학·수학 명작 영화</h1>", unsafe_allow_html=True)
st.markdown("### MBTI 유형을 선택하세요")

# 4열 버튼 UI 구성
mbti_list = list(mbti_colors.keys())
cols = st.columns(4)

# 상태 저장
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

for i, mbti in enumerate(mbti_list):
    with cols[i % 4]:
        btn_style = f"""
        <style>
        div[data-testid="stButton"] button#{mbti} {{
            background-color: {mbti_colors[mbti]};
            border: none;
            border-radius: 10px;
            color: #333;
            font-weight: bold;
            width: 100%;
            height: 3em;
        }}
        </style>
        """
        st.markdown(btn_style, unsafe_allow_html=True)
        if st.button(mbti, key=mbti):
            st.session_state.selected_mbti = mbti

# 결과 출력
selected = st.session_state.selected_mbti
if selected:
    st.markdown("---")
    st.markdown(f"### {selected} 유형을 위한 추천 영화")
    movies = mbti_movies.get(selected, [])
    cols = st.columns(3)
    for i, movie in enumerate(movies):
        with cols[i]:
            st.image(movie["img"], width=200)
            st.markdown(f"**{movie['title']}**")

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
