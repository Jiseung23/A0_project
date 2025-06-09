import streamlit as st

# 배경 스타일 (파스텔톤)
st.markdown("""
    <style>
    body {
        background-color: #FDF6EC;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<h1 style='text-align: center; color: #7A9E9F;'>🎬 MBTI별 과학·수학 명작 영화 추천 🍿</h1>", unsafe_allow_html=True)
st.write("")

# 영화 추천 데이터
mbti_movies = {
    "INTP": [
        {"title": "《굿 윌 헌팅》", "img": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"},
        {"title": "《엑스 마키나》", "img": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg"},
        {"title": "《인터스텔라》", "img": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"}
    ],
    "INTJ": [
        {"title": "《이미테이션 게임》", "img": "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg"},
        {"title": "《테슬라》", "img": "https://upload.wikimedia.org/wikipedia/en/f/f9/Tesla_film_poster.jpg"},
        {"title": "《컨택트》", "img": "https://upload.wikimedia.org/wikipedia/en/b/b0/Contact_ver2.jpg"}
    ],
    "ENTP": [
        {"title": "《마션》", "img": "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg"},
        {"title": "《인셉션》", "img": "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg"},
        {"title": "《쥬라기 공원》", "img": "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg"}
    ],
    "ENTJ": [
        {"title": "《오펜하이머》", "img": "https://upload.wikimedia.org/wikipedia/en/7/7f/Oppenheimer_%282023%29.jpg"},
        {"title": "《에니그마》", "img": "https://upload.wikimedia.org/wikipedia/en/d/db/Enigma_%282001_film%29.jpg"},
        {"title": "《아이언맨》", "img": "https://upload.wikimedia.org/wikipedia/en/0/00/Iron_Man_poster.jpg"}
    ],
    "INFP": [
        {"title": "《루시》", "img": "https://upload.wikimedia.org/wikipedia/en/1/14/Lucy_%282014_film%29_poster.jpg"},
        {"title": "《가타카》", "img": "https://upload.wikimedia.org/wikipedia/en/b/bb/Gattaca_Movie_Poster.jpg"},
        {"title": "《월터의 상상은 현실이 된다》", "img": "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Secret_Life_of_Walter_Mitty_2013_poster.jpg"}
    ],
    "INFJ": [
        {"title": "《컨택트》", "img": "https://upload.wikimedia.org/wikipedia/en/b/b0/Contact_ver2.jpg"},
        {"title": "《테슬라》", "img": "https://upload.wikimedia.org/wikipedia/en/f/f9/Tesla_film_poster.jpg"},
        {"title": "《갈릴레오의 딸》", "img": "https://i.imgur.com/K9nZBFl.jpg"}
    ],
    "ENFP": [
        {"title": "《히든 피겨스》", "img": "https://upload.wikimedia.org/wikipedia/en/4/4f/Hidden_Figures_%28film%29.png"},
        {"title": "《아이언맨》", "img": "https://upload.wikimedia.org/wikipedia/en/0/00/Iron_Man_poster.jpg"},
        {"title": "《루시》", "img": "https://upload.wikimedia.org/wikipedia/en/1/14/Lucy_%282014_film%29_poster.jpg"}
    ],
    "ENFJ": [
        {"title": "《체인 리액션》", "img": "https://upload.wikimedia.org/wikipedia/en/3/33/Chain_reaction_poster.jpg"},
        {"title": "《빅 히어로》", "img": "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg"},
        {"title": "《컨테이젼》", "img": "https://upload.wikimedia.org/wikipedia/en/b/b0/Contagion_Poster.jpg"}
    ],
    "ISTP": [
        {"title": "《그래비티》", "img": "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg"},
        {"title": "《로보캅》", "img": "https://upload.wikimedia.org/wikipedia/en/0/0c/RoboCop_%282014_film%29_poster.jpg"},
        {"title": "《매트릭스》", "img": "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg"}
    ],
    "ISFP": [
        {"title": "《로켓맨》", "img": "https://upload.wikimedia.org/wikipedia/en/3/3e/Rocketman_film_poster.png"},
        {"title": "《월-E》", "img": "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg"},
        {"title": "《에레멘탈》", "img": "https://upload.wikimedia.org/wikipedia/en/0/0f/Elemental_%282023_film%29.png"}
    ],
    "ESTP": [
        {"title": "《지오스톰》", "img": "https://upload.wikimedia.org/wikipedia/en/f/f7/Geostorm.png"},
        {"title": "《아마겟돈》", "img": "https://upload.wikimedia.org/wikipedia/en/f/fc/Armageddon-poster06.jpg"},
        {"title": "《테넷》", "img": "https://upload.wikimedia.org/wikipedia/en/1/14/Tenet_movie_poster.jpg"}
    ],
    "ESFP": [
        {"title": "《빅 히어로》", "img": "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg"},
        {"title": "《픽셀》", "img": "https://upload.wikimedia.org/wikipedia/en/2/20/Pixels_2015_poster.jpg"},
        {"title": "《백 투 더 퓨처》", "img": "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg"}
    ],
    "ISTJ": [
        {"title": "《뷰티풀 마인드》", "img": "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg"},
        {"title": "《이미테이션 게임》", "img": "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg"},
        {"title": "《더 맨 후 뉴 인피니티》", "img": "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Man_Who_Knew_Infinity_%28film%29.png"}
    ],
    "ISFJ": [
        {"title": "《어웨이크닝》", "img": "https://upload.wikimedia.org/wikipedia/en/e/e1/Awakenings_poster.jpg"},
        {"title": "《갈릴레오의 딸》", "img": "https://i.imgur.com/K9nZBFl.jpg"},
        {"title": "《로켓맨》", "img": "https://upload.wikimedia.org/wikipedia/en/3/3e/Rocketman_film_poster.png"}
    ],
    "ESTJ": [
        {"title": "《체인 리액션》", "img": "https://upload.wikimedia.org/wikipedia/en/3/33/Chain_reaction_poster.jpg"},
        {"title": "《그래비티》", "img": "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg"},
        {"title": "《타이타닉》", "img": "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg"}
    ],
