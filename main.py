import streamlit as st

# 파스텔톤 컬러 설정 (스트림릿 기본 스타일에 맞춰 background color 설정)
page_bg_color = """
<style>
body {
    background-color: #FDF6EC;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# 제목
st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>🎬 MBTI로 찾는 명작 과학·수학 영화 추천 💡</h1>", unsafe_allow_html=True)
st.markdown("## ")

# MBTI 입력 받기
mbti_input = st.text_input("당신의 MBTI를 입력해주세요 (예: INTP, ESFJ 등)", max_chars=4).upper()

# 추천 영화 데이터 (간단 예시)
mbti_movies = {
    "INTP": ["🧠 《굿 윌 헌팅》", "🤖 《엑스 마키나》", "🔬 《인터스텔라》"],
    "ENTP": ["🚀 《마션》", "🌀 《인셉션》", "🧬 《쥬라기 공원》"],
    "INFJ": ["🌌 《컨택트》", "🧪 《테슬라》", "📡 《콘택트》"],
    "ENFP": ["🔭 《히든 피겨스》", "💥 《아이언맨》", "🧠 《루시》"],
    "ISTJ": ["📊 《뷰티풀 마인드》", "🧱 《더 이미테이션 게임》", "📐 《더 맨 후 뉴 인피니티》"],
    "ESTJ": ["⚗️ 《체인 리액션》", "🚢 《타이타닉》 (공학 관점)", "🛰️ 《그래비티》"],
    "ISFJ": ["💖 《로켓맨》", "🧫 《어웨이크닝》", "🌱 《갈릴레오의 딸》"],
    "ESFJ": ["🌈 《빅 히어로》", "🧬 《안드로메다 스트레인》", "🦠 《컨테이젼》"]
    # 원하는 MBTI 더 추가 가능
}

# 추천 결과 출력
if mbti_input:
    if mbti_input in mbti_movies:
        st.markdown(f"### ✨ {mbti_input} 유형에게 추천하는 과학·수학 영화:")
        for movie in mbti_movies[mbti_input]:
            st.markdown(f"- {movie}")
    else:
        st.warning("알 수 없는 MBTI 유형이에요. 다시 확인해주세요 😥")

# 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #B48EAE;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
