import streamlit as st

# 🎨 MBTI별 파스텔톤 색상
mbti_colors = {
    "INTP": "#B2EBF2", "INTJ": "#B2EBF2", "ENTP": "#B2EBF2", "ENTJ": "#B2EBF2",  # NT
    "INFP": "#F8BBD0", "INFJ": "#F8BBD0", "ENFP": "#F8BBD0", "ENFJ": "#F8BBD0",  # NF
    "ISTJ": "#FFF9C4", "ISFJ": "#FFF9C4", "ESTJ": "#FFF9C4", "ESFJ": "#FFF9C4",  # SJ
    "ISTP": "#C8E6C9", "ISFP": "#C8E6C9", "ESTP": "#C8E6C9", "ESFP": "#C8E6C9",  # SP
}

# 🎬 MBTI별 추천 영화 데이터
mbti_movies = {
    "INTP": [
        {"title": "굿 윌 헌팅", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"},
        {"title": "엑스 마키나", "img": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg"},
        {"title": "인터스텔라", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"}
    ],
    "INTJ": [
        {"title": "이미테이션 게임", "img": "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg"},
        {"title": "테슬라", "img": "https://upload.wikimedia.org/wikipedia/en/f/f9/Tesla_film_poster.jpg"},
        {"title": "컨택트", "img": "https://upload.wikimedia.org/wikipedia/en/b/b0/Contact_ver2.jpg"}
    ],
    "ENTP": [
        {"title": "마션", "img": "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg"},
        {"title": "인셉션", "img": "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg"},
        {"title": "트랜센던스", "img": "https://upload.wikimedia.org/wikipedia/en/f/f0/Transcendence2014Poster.jpg"}
    ],
    "ENTJ": [
        {"title": "소셜 네트워크", "img": "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg"},
        {"title": "스티브 잡스", "img": "https://upload.wikimedia.org/wikipedia/en/b/b9/Steve_Jobs_film_poster.jpg"},
        {"title": "에니그마", "img": "https://upload.wikimedia.org/wikipedia/en/f/fb/Enigma_movie_poster.jpg"}
    ],
    "INFP": [
        {"title": "콘택트", "img": "https://upload.wikimedia.org/wikipedia/en/b/b0/Contact_ver2.jpg"},
        {"title": "허", "img": "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg"},
        {"title": "월터의 상상은 현실이 된다", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/The_Secret_Life_of_Walter_Mitty_2013_poster.jpg"}
    ],
    "INFJ": [
        {"title": "어라이벌", "img": "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival_%282016_film%29.jpg"},
        {"title": "어벤져스: 인피니티 워", "img": "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg"},
        {"title": "뷰티풀 마인드", "img": "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg"}
    ],
    "ENFP": [
        {"title": "빅 히어로", "img": "https://upload.wikimedia.org/wikipedia/en/4/4e/Big_Hero_6_%28film%29_poster.jpg"},
        {"title": "월-E", "img": "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg"},
        {"title": "파이 이야기", "img": "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg"}
    ],
    "ENFJ": [
        {"title": "인터스텔라", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"},
        {"title": "굿 윌 헌팅", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"},
        {"title": "히든 피겨스", "img": "https://upload.wikimedia.org/wikipedia/en/4/4f/Hidden_Figures_%28film%29.png"}
    ],
    "ISTJ": [
        {"title": "마션", "img": "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg"},
        {"title": "퍼스트 맨", "img": "https://upload.wikimedia.org/wikipedia/en/b/bd/First_Man_%282018_film%29.png"},
        {"title": "이미테이션 게임", "img": "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg"}
    ],
    "ISFJ": [
        {"title": "히든 피겨스", "img": "https://upload.wikimedia.org/wikipedia/en/4/4f/Hidden_Figures_%28film%29.png"},
        {"title": "뷰티풀 마인드", "img": "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg"},
        {"title": "아폴로 13", "img": "https://upload.wikimedia.org/wikipedia/en/9/9f/Apollo_thirteen_movie.jpg"}
    ],
    "ESTJ": [
        {"title": "돈 룩 업", "img": "https://upload.wikimedia.org/wikipedia/en/0/0f/Don%27t_Look_Up_2021_film_poster.jpg"},
        {"title": "퍼스트 맨", "img": "https://upload.wikimedia.org/wikipedia/en/b/bd/First_Man_%282018_film%29.png"},
        {"title": "소셜 네트워크", "img": "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg"}
    ],
    "ESFJ": [
        {"title": "히든 피겨스", "img": "https://upload.wikimedia.org/wikipedia/en/4/4f/Hidden_Figures_%28film%29.png"},
        {"title": "콘택트", "img": "https://upload.wikimedia.org/wikipedia/en/b/b0/Contact_ver2.jpg"},
        {"title": "굿 윌 헌팅", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"}
    ],
    "ISTP": [
        {"title": "인셉션", "img": "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg"},
        {"title": "인터스텔라", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"},
        {"title": "테넷", "img": "https://upload.wikimedia.org/wikipedia/en/1/11/Tenet_movie_poster.jpg"}
    ],
    "ISFP": [
        {"title": "월터의 상상은 현실이 된다", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/The_Secret_Life_of_Walter_Mitty_2013_poster.jpg"},
        {"title": "월-E", "img": "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg"},
        {"title": "파이 이야기", "img": "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg"}
    ],
    "ESTP": [
        {"title": "테넷", "img": "https://upload.wikimedia.org/wikipedia/en/1/11/Tenet_movie_poster.jpg"},
        {"title": "마션", "img": "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg"},
        {"title": "엑스 마키나", "img": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg"}
    ],
    "ESFP": [
        {"title": "빅 히어로", "img": "https://upload.wikimedia.org/wikipedia/en/4/4e/Big_Hero_6_%28film%29_poster.jpg"},
        {"title": "월-E", "img": "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg"},
        {"title": "히든 피겨스", "img": "https://upload.wikimedia.org/wikipedia/en/4/4f/Hidden_Figures_%28film%29.png"}
    ],
}

# 📌 앱 제목
st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>MBTI로 찾는 과학·수학 명작 영화</h1>", unsafe_allow_html=True)
st.markdown("### MBTI 유형을 선택하세요")

# 📌 4열 버튼 그리드
mbti_list = list(mbti_movies.keys())
selected_mbti = st.session_state.get("selected_mbti", "")
cols = st.columns(4)

for i, mbti in enumerate(mbti_list):
    with cols[i % 4]:
        st.markdown(
            f"""
            <style>
            div[data-testid="stButton"] > button[title="{mbti}"] {{
                background-color: {mbti_colors[mbti]};
                border-radius: 8px;
                border: 1px solid #ccc;
                width: 100%;
                font-weight: bold;
                color: #333;
                padding: 0.4em 0.8em;
                margin-bottom: 4px;
            }}
            </style>
            """, unsafe_allow_html=True
        )
        if st.button(mbti, key=mbti):
            st.session_state.selected_mbti = mbti
            selected_mbti = mbti

# 📌 결과 출력
if selected_mbti:
    st.markdown("---")
    st.markdown(f"### {selected_mbti} 유형을 위한 추천 영화")

    movies = mbti_movies[selected_mbti]
    cols = st.columns(3)
    for i, movie in enumerate(movies):
        with cols[i]:
            st.image(movie["img"], width=180)
            st.markdown(f"**{movie['title']}**")

# 📌 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
