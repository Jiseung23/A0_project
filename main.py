import streamlit as st

# 🎨 배경색 설정 (파스텔톤)
st.markdown(
    """
    <style>
    body {
        background-color: #FDF6EC;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎬 제목
st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>🍿 MBTI로 찾는 과학·수학 명작 영화 🎥</h1>", unsafe_allow_html=True)
st.write("")

# 📚 추천 영화 데이터: 영화제목 + 이미지 링크
mbti_movies = {
    "INTP": [
        {"title": "🎬 《굿 윌 헌팅》", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"},
        {"title": "🎥 《엑스 마키나》", "img": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg"},
        {"title": "📽️ 《인터스텔라》", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"}
    ],
    "ENTP": [
        {"title": "🎬 《마션》", "img": "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg"},
        {"title": "🌀 《인셉션》", "img": "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg"},
        {"title": "🦕 《쥬라기 공원》", "img": "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg"}
    ],
    # ⚠️ 다른 MBTI들도 여기에 추가 가능 (간략화 위해 생략)
}

# MBTI 목록
mbti_list = list(mbti_movies.keys())

# 선택 상태 저장
selected_mbti = st.session_state.get("selected_mbti", "")

# 🔘 버튼 스타일로 MBTI 선택
cols = st.columns(4)
for i, mbti in enumerate(mbti_list):
    with cols[i % 4]:
        if st.button(mbti, key=mbti):
            st.session_state.selected_mbti = mbti
            selected_mbti = mbti

# 🎁 영화 추천 결과 출력
if selected_mbti:
    st.markdown("---")
    st.markdown(f"### 🎯 {selected_mbti} 유형에게 추천하는 영화 리스트:")

    for movie in mbti_movies[selected_mbti]:
        st.markdown(f"**{movie['title']}**")
        st.image(movie["img"], width=200)
        st.markdown("")

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)

# 🧾 카드 버튼 스타일
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #FCE4EC;
        color: #4A4A4A;
        border: 2px solid #F8BBD0;
        border-radius: 12px;
        padding: 0.5em 1em;
        margin: 0.2em;
        font-size: 16px;
        font-weight: bold;
        transition: 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #F8BBD0;
        color: white;
        border-color: #F48FB1;
    }
    </style>
    """,
    unsafe_allow_html=True
)
