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

# 영화 추천 목록 (별점 포함)
mbti_movies = {
    "INTP": [
        {"title": "굿 윌 헌팅", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png", "rating": 4.8},
        {"title": "엑스 마키나", "img": "https://i.namu.wiki/i/gp_84CU2vOQcnuSoNTZphSTBbNZK7vZPQGwaOKgS9Onj3Z_FPjd6Y5KexEFAedU4MwNVR2eKyiSlNKqFDRFe7g.webp", "rating": 4.6},
        {"title": "인터스텔라", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "rating": 4.9}
    ],
    "INFJ": [
        {"title": "뷰티풀 마인드", "img": "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg", "rating": 4.7},
        {"title": "컨택트", "img": "https://i.namu.wiki/i/eau9zbUvBKKIQVU0e_Ag6xa1NijN1FRvoYXnNHSK4DxTCWrw8nRAuj0vbzD4RXUU4YHDWnx9aPj3Rl8ogT62cA.webp", "rating": 4.5},
        {"title": "이터널 선샤인", "img": "https://i.namu.wiki/i/9es4tXG1Dh2SjMzjk0KWtxVSuGCMZa5uKPCLutgd7bLn_J1TmEMESD5RdQqsLUtjiUsU1cELe5LKbpZQE-BpEg.webp", "rating": 4.6}
    ],
    "ESTJ": [
        {"title": "인셉션", "img": "https://i.namu.wiki/i/O2uuv7bO0Hc33rLHS7t3OGhc5_guUiIyY6VThmyKSP8lC1kwtN6vS8KsiUIbda5n46DAVy7_Z2_c2KRR_mUYEw.webp", "rating": 4.7},
        {"title": "소셜 네트워크", "img": "https://i.namu.wiki/i/VL7PFy33XiC2XYIlqKwF7O5Ftj_Hp6AxGA6WW652pyxYSB9bjNOEO1B4mfQKD00pFvhFlnUY2k3T2KRcra9c5g.webp", "rating": 4.4},
        {"title": "굿 윌 헌팅", "img": "https://i.namu.wiki/i/a9JF44HxhY_5spS7W9KZmil4WTPJ1pUcYj3yQW4YXkj0eeqoPfkJZyduXDOZhfacUei8amB1zFA75gSIDzM8Jw.webp", "rating": 4.8}
    ],
    "ESFP": [
        {"title": "옥자", "img": "https://i.namu.wiki/i/5JAru7W0xhmR8FO3_2EbD8G0ZO2FFCFlH40kO8ikDkfJj8eEXQW0oAZnsIVrwnunISgTS2A-ddWz4dU-jTfwyQ.webp", "rating": 4.2},
        {"title": "월터의 상상은 현실이 된다", "img": "https://i.namu.wiki/i/mxw5oOwRXHPADzoWNKJUALTiD7tSI32DEO4Jmj3fhATRYyh3SNqnh8Z_ObNaUkJjMiVaq5zolNFmjQIiHd0kWQ.webp", "rating": 4.3},
        {"title": "월드워Z", "img": "https://i.namu.wiki/i/hoSMs-F6OgDLAIoI4yJk37Gz8r9TxvntEhaecQd5jl70mzHXG6V3q4rr8CnB9xVuytUaaksyFcoAlervQUz0dQ.webp", "rating": 4.1}
    ],
}

# 페이지 설정
st.set_page_config(page_title="MBTI 영화 추천", layout="wide")

st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>MBTI로 찾는 과학·수학 명작 영화 🎬</h1>", unsafe_allow_html=True)
st.markdown("### MBTI 유형을 선택하세요")

# MBTI 버튼 UI
cols = st.columns(4)
for i, mbti in enumerate(mbti_colors.keys()):
    with cols[i]:
        btn = st.button(mbti, key=mbti)
        if btn:
            st.session_state.selected_mbti = mbti

# 추천 결과 출력
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
            stars = "⭐" * int(round(movie["rating"]))
            st.markdown(f"{stars} ({movie['rating']:.1f}/5.0)")

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
