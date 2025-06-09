import streamlit as st

# MBTI별 색상
mbti_colors = {
    "INTP": "#B2EBF2",
    "INFJ": "#F8BBD0",
    "ESTJ": "#FFF9C4",
    "ESFP": "#FFCDD2",
}

# 추천 사유
mbti_reasons = {
    "INTP": "지적 호기심과 깊이 있는 사고를 자극하는 영화들입니다.",
    "INFJ": "감성과 철학이 조화된 서사를 좋아하는 INFJ에게 딱 맞는 작품들입니다.",
    "ESTJ": "논리적이고 실용적인 시각을 가진 ESTJ에게 통찰을 주는 영화들입니다.",
    "ESFP": "에너지 넘치고 감각적인 ESFP에게 매력적인 경험을 선사합니다.",
}

# 영화 데이터 (desc: 툴팁 / summary: 상세 줄거리)
mbti_movies = {
    "INTP": [
        {
            "title": "굿 윌 헌팅",
            "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png",
            "rating": 4.8,
            "desc": "수학 천재와 심리학자의 우정 이야기",
            "summary": "천재적인 두뇌를 지녔지만 방황하던 윌이 심리학자 숀을 만나면서 인생의 방향을 찾아가는 이야기입니다.",
        },
        {
            "title": "엑스 마키나",
            "img": "https://i.namu.wiki/i/gp_84CU2vOQcnuSoNTZphSTBbNZK7vZPQGwaOKgS9Onj3Z_FPjd6Y5KexEFAedU4MwNVR2eKyiSlNKqFDRFe7g.webp",
            "rating": 4.6,
            "desc": "AI와 인간의 철학적 경계",
            "summary": "젊은 프로그래머가 세계적 기업의 CEO 실험실에 초대되어 인간 같은 AI 로봇을 테스트하면서 벌어지는 심리 게임.",
        },
        {
            "title": "인터스텔라",
            "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
            "rating": 4.9,
            "desc": "사랑과 과학을 넘나드는 우주여행",
            "summary": "지구 멸망 위기 속, 우주로 떠난 파일럿 쿠퍼와 딸 머피의 시간과 공간을 초월한 이야기.",
        },
    ],
    # 다른 유형도 동일하게 확장 가능
}

# 페이지 설정
st.set_page_config(page_title="MBTI 영화 추천", layout="wide")
st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>MBTI로 찾는 과학·수학 명작 영화 🎬</h1>", unsafe_allow_html=True)
st.markdown("### MBTI 유형을 선택하세요")

# MBTI 버튼
cols = st.columns(4)
for i, mbti in enumerate(mbti_colors.keys()):
    with cols[i]:
        if st.button(mbti, key=mbti):
            st.session_state.selected_mbti = mbti

# 결과 출력
selected = st.session_state.get("selected_mbti", None)
if selected:
    st.markdown("---")
    st.markdown(f"### {selected} 유형을 위한 추천 영화")
    st.markdown(f"📝 *{mbti_reasons[selected]}*")

    movies = mbti_movies[selected]
    cols = st.columns(3)

    for i, movie in enumerate(movies):
        with cols[i]:
            html_img = f"""
                <img src="{movie['img']}" alt="{movie['title']}" title="{movie['desc']}" width="180" style="border-radius:10px;">
            """
            st.markdown(html_img, unsafe_allow_html=True)
            st.markdown(f"**{movie['title']}**")
            stars = "⭐" * int(round(movie["rating"]))
            st.markdown(f"{stars} ({movie['rating']:.1f}/5.0)")
            with st.expander("📖 줄거리 보기"):
                st.write(movie["summary"])

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
