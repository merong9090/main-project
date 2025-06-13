import streamlit as st

# 체형에 따른 추천 딕셔너리
body_shape_recommendations = {
    "사과형": {
        "설명": "상체가 발달한 체형으로 허리는 굵고 하체는 상대적으로 슬림합니다.",
        "추천 스타일": [
            "A라인 원피스",
            "허리선을 강조하지 않는 루즈핏 상의",
            "V넥 블라우스"
        ]
    },
    "배형": {
        "설명": "복부에 지방이 많은 체형입니다.",
        "추천 스타일": [
            "허리라인을 커버하는 블라우스",
            "하이웨이스트 팬츠",
            "롱 재킷"
        ]
    },
    "모래시계형": {
        "설명": "가슴과 엉덩이가 크고 허리가 잘록한 이상적인 체형입니다.",
        "추천 스타일": [
            "허리 라인을 강조한 원피스",
            "슬림 핏 셔츠",
            "벨트로 포인트 주기"
        ]
    },
    "역삼각형": {
        "설명": "어깨가 넓고 하체가 좁은 체형입니다.",
        "추천 스타일": [
            "A라인 스커트",
            "밸런스를 맞추는 와이드 팬츠",
            "라운드넥 상의"
        ]
    },
    "직사각형": {
        "설명": "허리 라인이 명확하지 않고 전체적으로 직선적인 체형입니다.",
        "추천 스타일": [
            "허리에 포인트를 주는 옷",
            "셔링이 있는 원피스",
            "레이어드 코디"
        ]
    },
    "pear형 (하체비만)": {
        "설명": "상체는 슬림하지만 하체가 발달한 체형입니다.",
        "추천 스타일": [
            "어깨에 볼륨을 준 상의",
            "플레어 스커트",
            "시선을 상체로 유도하는 코디"
        ]
    }
}

# 앱 제목
st.title("👗 체형 분석 기반 코디 추천")

# 이미지 업로드 (선택 사항)
uploaded_file = st.file_uploader("체형이 드러난 전신 사진을 업로드하세요 (선택사항)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="업로드한 이미지", use_column_width=True)

# 체형 선택
st.subheader("당신의 체형을 선택하세요")
selected_shape = st.selectbox("체형 유형을 선택하세요", list(body_shape_recommendations.keys()))

# 추천 결과 표시
if selected_shape:
    st.markdown(f"### ✅ {selected_shape} 체형 분석 결과")
    st.write(body_shape_recommendations[selected_shape]["설명"])

    st.markdown("#### 👕 추천 스타일:")
    for item in body_shape_recommendations[selected_shape]["추천 스타일"]:
        st.write(f"- {item}")

    # 예시 이미지 또는 링크
    st.markdown("#### 📸 스타일 예시 이미지 (참고용)")
    st.image(f"https://source.unsplash.com/400x300/?fashion,{selected_shape}")

