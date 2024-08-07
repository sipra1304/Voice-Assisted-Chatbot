import test_sif as T
import streamlit as st

def main():
    st.title("Voice Assistant Triumph")

    text = T.rec_audio()
    intent = T.get_intent(text)
    speak = T.handle_intent(intent, text)

    st.write("Assistant Response:")
    st.write(speak)

if __name__ == "__main__":
    main()
