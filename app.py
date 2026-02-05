import streamlit as st
from streamlit_local_storage import LocalStorage
import time

# 1. 초기 세팅
localS = LocalStorage()
st.set_page_config(page_title="길드 경매 시스템", layout="centered")

# 세션 상태 초기화 (메모리 로딩 확인용)
if "initialized" not in st.session_state:
    st.session_state.initialized = False
if "user_id" not in st.session_state:
    st.session_state.user_id = None

# ---------------------------------------------------------
# 2. 브라우저 사물함에서 데이터 읽어오기
# ---------------------------------------------------------
# 브라우저가 사물함을 열 시간을 아주 잠깐(0.1초) 기다려줍니다.
saved_id = localS.getItem("guild_user_id")

# 만약 세션에는 없는데 사물함에서 데이터를 찾았다면? -> 자동 로그인 성공
if saved_id and not st.session_state.user_id:
    st.session_state.user_id = saved_id
    st.session_state.initialized = True
    st.rerun()

# ---------------------------------------------------------
# 3. 화면 표시 로직
# ---------------------------------------------------------

# 케이스 A: 이미 누군지 알고 있는 경우 (자동 로그인 완료)
if st.session_state.user_id:
    st.title(f"🛡️ {st.session_state.user_id}님, 환영합니다!")
    st.info("이 핸드폰에서는 이제 항상 자동으로 로그인됩니다.")
    
    # [메인 기능들]
    st.write("---")
    st.subheader("📦 오늘 올라온 경매 아이템")
    # ... 경매 로직 ...

    # 혹시 이름을 바꿔야 할 때를 위한 버튼
    if st.sidebar.button("ID 재설정/로그아웃"):
        localS.deleteItem("guild_user_id")
        st.session_state.user_id = None
        st.rerun()

# 케이스 B: 처음 왔거나 정보를 못 찾은 경우
else:
    st.title("🛡️ 길드 경매 시스템")
    st.write("처음 한 번만 본인의 길드 닉네임을 등록해주세요.")
    
    new_id = st.text_input("닉네임 입력", placeholder="예: 유동현")
    
    if st.button("등록 및 시작하기"):
        if new_id:
            # 브라우저 사물함에 영구 저장
            localS.setItem("guild_user_id", new_id)
            # 현재 화면 메모리에도 저장
            st.session_state.user_id = new_id
            st.success("등록되었습니다! 이제 이 주소로 그냥 들어오시면 됩니다.")
            time.sleep(1) # 확인 메시지 보여줄 시간
            st.rerun()
