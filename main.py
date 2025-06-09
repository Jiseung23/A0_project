import streamlit as st

# 🌸 파스텔톤 배경 적용
page_bg_color = """
<style>
body {
    background-color: #FDF6EC;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# 🎬 제목
st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>🎬 MBTI로 찾는 명작 과학·수학 영화 추천 💡</h1>", unsafe_allow_html=True)
st.markdown("## ")

# MBTI 리스트
mbti_types = [
    "INTP", "ENTP", "INFJ", "ENFP",
    "ISTJ", "ESTJ", "ISFJ", "ESFJ"
]

# 🎯 라디오 버튼으로 MBTI 선택
selected_mbti = st.radio("당신의 MBTI를 선택해주세요:", mbti_types, horizontal=True)

# 🎥 MBTI별 영화 추천 데이터
mbti_movies = {
    "INTP": ["🧠 《굿 윌 헌팅》", "🤖 《엑스 마키나》", "🔬 《인터스텔라》"],
    "ENTP": ["🚀 《마션》", "🌀 《인셉션》", "🧬 《쥬라기 공원》"],
    "INFJ": ["🌌 《컨택트》", "🧪 《테슬라》", "📡 《콘택트》"],
    "ENFP": ["🔭 《히든 피겨스》", "💥 《아이언맨》", "🧠 《루시》"],
    "ISTJ": ["📊 《뷰티풀 마인드》", "🧱 《더 이미테이션 게임》", "📐 《더 맨 후 뉴 인피니티》"],
    "ESTJ": ["⚗️ 《체인 리액션》", "🚢 《타이타닉》 (공학 관점)", "🛰️ 《그래비티》"],
    "ISFJ": ["💖 《로켓맨》", "🧫 《어웨이크닝》", "🌱 《갈릴레오의 딸》"],
    "ESFJ": ["🌈 《빅 히어로》", "🧬 《안드로메다 스트레인》", "🦠 《컨테이젼》"]
}

# 🎁 추천 영화 표시
st.markdown(f"### ✨ {selected_mbti} 유형에게 추천하는 과학·수학 영화:")
for movie in mbti_movies[selected_mbti]:
    st.markdown(f"- {movie}")

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
