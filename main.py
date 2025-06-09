import streamlit as st

# 색상 정의 (MBTI 그룹별 파스텔톤)
mbti_colors = {
    "INTP": "#B2EBF2", "INTJ": "#B2EBF2", "ENTP": "#B2EBF2", "ENTJ": "#B2EBF2",  # NT
    "INFP": "#F8BBD0", "INFJ": "#F8BBD0", "ENFP": "#F8BBD0", "ENFJ": "#F8BBD0",  # NF
    "ISTJ": "#FFF9C4", "ISFJ": "#FFF9C4", "ESTJ": "#FFF9C4", "ESFJ": "#FFF9C4",  # SJ
    "ISTP": "#C8E6C9", "ISFP": "#C8E6C9", "ESTP": "#C8E6C9", "ESFP": "#C8E6C9",  # SP
}

mbti_list = list(mbti_colors.keys())

st.set_page_config(page_title="MBTI 영화 추천", layout="wide")

st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>MBTI로 찾는 과학·수학 명작 영화</h1>", unsafe_allow_html=True)
st.markdown("### MBTI 유형을 선택하세요")

selected_mbti = None
cols = st.columns(4)

for i, mbti in enumerate(mbti_list):
    color = mbti_colors[mbti]
    with cols[i % 4]:
        if st.markdown(
            f"""
            <form action="" method="post">
                <button name="mbti" value="{mbti}" style="
                    background-color: {color};
                    border: none;
                    padding: 10px 20px;
                    width: 100%;
                    margin-bottom: 8px;
                    border-radius: 10px;
                    font-weight: bold;
                    font-size: 16px;
                    color: #333;
                    cursor: pointer;
                ">{mbti}</button>
            </form>
            """, unsafe_allow_html=True):
            pass

# 폼 전송 감지 (쿼리 파싱을 통해 MBTI 선택 추적)
query_params = st.experimental_get_query_params()
if "mbti" in query_params:
    selected_mbti = query_params["mbti"][0]

# 세션 상태를 통해 안정적으로 유지
if selected_mbti:
    st.session_state.selected_mbti = selected_mbti
elif "selected_mbti" in st.session_state:
    selected_mbti = st.session_state.selected_mbti

# 영화 추천 정보 (위에서 제공한 mbti_movies 딕셔너리를 여기에 넣으면 완성됨)
mbti_movies = {
    # 예시로 INTP만 넣음 — 전체는 앞서 제공된 코드를 붙여넣으세요.
    "INTP": [
        {"title": "굿 윌 헌팅", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"},
        {"title": "엑스 마키나", "img": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg"},
        {"title": "인터스텔라", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"}
    ],
    # ... 나머지 MBTI는 앞서 제공된 mbti_movies 그대로 삽입!
}

# 추천 결과 출력
if selected_mbti:
    st.markdown("---")
    st.markdown(f"### {selected_mbti} 유형을 위한 추천 영화")
    movies = mbti_movies.get(selected_mbti, [])
    cols = st.columns(3)
    for i, movie in enumerate(movies):
        with cols[i]:
            st.image(movie["img"], width=180)
            st.markdown(f"**{movie['title']}**")

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
