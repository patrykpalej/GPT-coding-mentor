import streamlit as st


def create_sidebar():
    st.sidebar.markdown("# Coding mentor")
    st.sidebar.markdown("It will **help you** to solve the problem. It **will not** write the code"
                        " for you (unless you ask for the general advice which is"
                        " not a specific exercise).")
    st.sidebar.markdown("Just enter an exercise you're trying to solve.")

    st.sidebar.warning("Note that Assistants API currently doesn't support streaming output")

    st.sidebar.markdown("---")
    api_key = st.sidebar.text_input("Your API key", type="password")

    st.sidebar.markdown("### How to get the key")
    st.sidebar.markdown("1. Sign up on [OpenAI](https://openai.com/)")
    st.sidebar.markdown(
        "2. Go to [billing settings](https://platform.openai.com/account/billing/overview)")
    st.sidebar.markdown("3. Define your payment method")
    st.sidebar.markdown("4. Add credits (min. $5)")
    st.sidebar.markdown("5. Create an [API key](https://platform.openai.com/api-keys)")
    st.sidebar.markdown("6. Paste it above")

    return api_key
