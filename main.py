import streamlit as st

# 4개 MBTI와 파스텔톤 색상
mbti_colors = {
    "INTP": "#B2EBF2",
    "INFJ": "#F8BBD0",
    "ESTJ": "#FFF9C4",
    "ESFP": "#FFCDD2",
}

# 추천 사유 (한 줄 설명)
mbti_reasons = {
    "INTP": "지적 호기심과 깊이 있는 사고를 자극하는 영화들입니다.",
    "INFJ": "감성과 철학이 조화된 서사를 좋아하는 INFJ에게 딱 맞는 작품들입니다.",
    "ESTJ": "논리적이고 실용적인 시각을 가진 ESTJ에게 통찰을 주는 영화들입니다.",
    "ESFP": "에너지 넘치고 감각적인 ESFP에게 매력적인 경험을 선사합니다.",
}

# 영화 추천 목록
mbti_movies = {
    "INTP": [
        {"title": "굿 윌 헌팅", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"},
        {"title": "엑스 마키나", "img": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg"},
        {"title": "인터스텔라", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"}
    ],
    "INFJ": [
        {"title": "뷰티풀 마인드", "img": "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg"},
        {"title": "컨택트", "img": "https://i.namu.wiki/i/eau9zbUvBKKIQVU0e_Ag6xa1NijN1FRvoYXnNHSK4DxTCWrw8nRAuj0vbzD4RXUU4YHDWnx9aPj3Rl8ogT62cA.webp"},
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

# 버튼 생성 및 클릭 감지
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

# 선택 결과
selected = st.session_state.get("selected_mbti", None)
if selected:
    st.markdown("---")
    st.markdown(f"### {selected} 유형을 위한 추천 영화")
    st.markdown(f"📝 *{mbti_reasons[selected]}*")
    movies = mbti_movies[selected]
    cols = st.columns(3)
    for i, movie in enumerate(movies):
        with cols[i]:
            st.image(movie["img"], width=180)
            st.markdown(f"**{movie['title']}**")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
