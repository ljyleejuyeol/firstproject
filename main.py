import streamlit as st
import random

# --- 기본 설정 ---
st.set_page_config(
    page_title="🎮 가위바위보 챌린지!",
    page_icon="🎲",
    layout="centered",
)

# --- 제목 영역 ---
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>🎮 가위 ✌️ 바위 ✊ 보 🖐 게임!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #6a5acd;'>운을 시험해보세요! 당신은 컴퓨터를 이길 수 있을까요? 💥</h3>", unsafe_allow_html=True)
st.divider()

# --- 게임 선택 영역 ---
st.markdown("## 🙋‍♂️ 당신의 선택은?")
choices = {
    "가위 ✌️": "scissors",
    "바위 ✊": "rock",
    "보 🖐": "paper"
}

player_choice = st.radio(
    "무엇을 내시겠어요?",
    list(choices.keys()),
    index=0,
    horizontal=True
)

# --- 게임 로직 ---
def get_winner(player, computer):
    if player == computer:
        return "비겼어요! 😐"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "당신이 이겼어요! 🎉"
    else:
        return "컴퓨터가 이겼어요! 😢"

# --- 게임 실행 버튼 ---
if st.button("🎲 대결 시작!"):
    player = choices[player_choice]
    computer = random.choice(["rock", "paper", "scissors"])
    
    # --- 이모지 매칭 ---
    emoji_dict = {
        "rock": "✊",
        "paper": "🖐",
        "scissors": "✌️"
    }

    st.markdown("### 🆚 결과")
    st.markdown(f"🙋‍♂️ 당신: **{emoji_dict[player]}**")
    st.markdown(f"💻 컴퓨터: **{emoji_dict[computer]}**")
    
    result = get_winner(player, computer)
    st.markdown(f"## 🔥 결과: **{result}**")

    st.balloons()

# --- 푸터 ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Made with ❤️ using <strong>Streamlit</strong></p>",
    unsafe_allow_html=True
)
