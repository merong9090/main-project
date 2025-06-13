import streamlit as st

# 체형 분류 함수
def predict_body_shape(answers):
    # 매우 간단한 규칙 기반 분류
    if answers["어깨 발달"] and not answers["하체 발달"]:
        return "역삼각형"
    elif answers["하체 발달"] and not answers["어깨 발달"]:
        return "pear형 (하체비만)"
    elif answers["허리 있음"] and answers["곡선형"]:
        return "모래시계형"
    elif answers["배 나옴"]:
        return "배형"
    elif not answers["허리 있음"] and not answers["곡선형"]:
        return "직사각형"
    elif answers["상체 발달"] and answers["배 나옴"]:
        return "사과형"
    else:
        return "직사각형"  # 기본값

# 체형별 추천
body_shape_recommendations = {
    "사과형": {
        "설명": "상체가 발달한 체형으로 허리는 굵고 하체는 상대적으로 슬림합니다.",
        "추천 스타일": [
            "A라인 원피스", "루즈핏 상의", "V넥 블라우스"
        ]
    },
    "배형": {
        "설명": "복부에 지방이 많은 체형입니다.",
        "추천 스타일": [
            "롱 재킷", "하이웨이스트 팬츠", "허리라인 커버"
        ]
    },
    "모래시계형": {
        "설명": "가슴과 엉덩이가 크고 허리가 잘록한 체형입니다.",
        "추천 스타일": [
            "벨트가 있는 원피스", "허리 강조 스타일", "슬림 셔츠"
        ]
    },
    "역삼각형": {
        "설명": "어깨가 넓고 하체가 좁은 체형입니다.",
        "추천 스타일": [
            "A라인 스커트", "와이드 팬츠", "라운드넥 상의"
        ]
    },
    "직사각형": {
        "설명": "전체적으로 직선적인 체형입니다.",
        "추천 스타일": [
            "셔링 원피스", "허리 강조", "레이어드 코디"
        ]
    },
    "pear형 (하체비만)": {
        "설명": "상체는 슬림하지만 하체가 발달한 체형입니다.",
        "추천 스타일": [
            "플레어 스커트", "상체에 시선 유도", "볼륨감 있는 상의"
        ]
    }
}

# Streamlit 앱 시작
st.title("👗 체형 테스트 기반 코디 추천")

st.markdown("아래 간단한 테스트를 통해 당신의 체형을 분석합니다.")

# 테스트 문항
answers = {}
answers["상체 발달"] = st.radio("상체(어깨/가슴)가 하체보다 발달했나요?", ["예", "아니오"]) == "예"
answers["하체 발달"] = st.radio("하체(엉덩이/허벅지)가 상체보다 발달했나요?", ["예", "아니오"]) == "예"
answers["허리 있음"] = st.radio("허리 라인이 눈에 띄게 들어가 있나요?", ["예", "아니오"]) == "예"
answers["배 나옴"] = st.radio("복부가 나와 있는 편인가요?", ["예", "아니오"]) == "예"
answers["곡선형"] = st.radio("몸이 곡선형(곡선미 있음)인가요, 직선형인가요?", ["곡선형", "직선형"]) == "곡선형"
answers["어깨 발달"] = st.radio("어깨가 넓거나 뚜렷한 편인가요?", ["예", "아니오"]) == "예"

# 체형 예측
if st.button("체형 분석하기"):
    predicted_shape = predict_body_shape(answers)
    st.markdown(f"### ✅ 예측된 체형: **{predicted_shape}**")
    st.write(body_shape_recommendations[predicted_shape]["설명"])

    st.markdown("#### 👕 추천 스타일:")
    for item in body_shape_recommendations[predicted_shape]["추천 스타일"]:
        st.write(f"- {item}")

    # 예시 이미지
    st.markdown("#### 📸 스타일 예시 이미지 (참고용)")
    st.image(f"https://source.unsplash.com/400x300/?fashion,{predicted_shape}")
