import streamlit as st

# 4개 MBTI와 파스텔톤 색상
mbti_colors = {
    "INTP": "#B2EBF2",  # 파란 계열
    "INFJ": "#F8BBD0",  # 분홍 계열
    "ESTJ": "#FFF9C4",  # 노란 계열
    "ESFP": "#FFCDD2",  # 연한 빨강 계열
}

# 영화 추천 데이터 (간단하게 3개씩)
mbti_movies = {
    "INTP": [
        {"title": "굿 윌 헌팅", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"},
        {"title": "엑스 마키나", "img": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg"},
        {"title": "인터스텔라", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"}
    ],
    "INFJ": [
        {"title": "뷰티풀 마인드", "img": "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg"},
        {"title": "컨택트", "img": "https://upload.wikimedia.org/wikipedia/en/d/dc/Arrival%2C_2016_film_poster.jpg"},
        {"title": "이터널 선샤인", "img": "https://upload.wikimedia.org/wikipedia/en/0/0b/Eternal_Sunshine_of_the_Spotless_Mind_poster.jpg"}
    ],
    "ESTJ": [
        {"title": "인셉션", "img": "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg"},
        {"title": "소셜 네트워크", "img": "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg"},
        {"title": "굿 윌 헌팅", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"}
    ],
    "ESFP": [
        {"title": "옥자", "img": "https://upload.wikimedia.org/wikipedia/en/2/23/Okja_poster.jpg"},
        {"title": "월터의 상상은 현실이 된다", "img": "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Secret_Life_of_Walter_Mitty_poster.jpg"},
        {"title": "월드워Z", "img": "https://upload.wikimedia.org/wikipedia/en/f/fb/World_War_Z_film_poster.jpg"}
    ],
}

st.set_page_config(page_title="MBTI 영화 추천", layout="wide")

st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>MBTI로 찾는 과학·수학 명작 영화 🎬</h1>", unsafe_allow_html=True)
st.markdown("### MBTI 유형을 선택하세요")

cols = st.columns(4)

# 클릭 시 세션 상태에 저장하도록 버튼 만들기 (버튼마다 고유 key 필수!)
for i, mbti in enumerate(mbti_colors.keys()):
    with cols[i]:
        style = f"""
            background-color: {mbti_colors[mbti]};
            border: none;
            border-radius: 10px;
            padding: 10px;
            font-weight: bold;
            font-size: 18px;
            color: #333;
            width: 100%;
            cursor: pointer;
        """
        if st.button(mbti, key=mbti):
            st.session_state.selected_mbti = mbti

# 선택된 MBTI 영화 추천 보여주기
selected = st.session_state.get("selected_mbti", None)
if selected:
    st.markdown("---")
    st.markdown(f"### {selected} 유형을 위한 추천 영화")
    movies = mbti_movies[selected]
    cols = st.columns(3)
    for i, movie in enumerate(movies):
        with cols[i]:
            st.image(movie["img"], width=180)
            st.markdown(f"**{movie['title']}**")

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
