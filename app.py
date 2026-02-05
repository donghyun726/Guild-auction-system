import streamlit as st
from streamlit_local_storage import LocalStorage

# 1. 초기 설정
localS = LocalStorage()
st.title("🛡️ 우리 길드 경매 시스템")

# 2. ID 인식 로직 (주소창 -> 사물함 -> 직접입력 순)
url_id = st.query_params.get("id")
saved_id = localS.getItem("guild_user_id")

if url_id:
    user_id = url_id
    localS.setItem("guild_user_id", user_id)
elif saved_id:
    user_id = saved_id
else:
    user_id = st.text_input("길드 닉네임을 입력해주세요:")
    if user_id:
        localS.setItem("guild_user_id", user_id)
        st.rerun()

# 3. 메인 화면 (ID가 있을 때만 작동)
if user_id:
    st.write(f"👋 반갑습니다, **{user_id}**님!")
    
    # 아이템 선택 (예시 데이터)
    item_list = ["전설의 검", "희귀 강화석", "영웅의 갑옷"]
    selected_item = st.selectbox("경매 아이템 선택", item_list)
    
    if st.button(f"{selected_item} 입찰 신청"):
        # 여기에 구글 시트로 데이터를 보내는 코드가 들어갑니다.
        st.success(f"{selected_item} 신청 완료! (로그 기록 중...)")