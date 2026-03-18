import streamlit as st


def render_sidebar(options: list[str], selected: str = None, on_logout=None):
    st.sidebar.title("Navigation")
    st.sidebar.markdown("---")
    choice = st.sidebar.radio("", options, index=options.index(selected) if selected in options else 0)
    st.session_state.subpage = choice

    st.sidebar.markdown("---")
    if st.sidebar.button("Logout"):
        if on_logout:
            on_logout()
        else:
            st.session_state.clear()
            st.session_state.page = "landing"
