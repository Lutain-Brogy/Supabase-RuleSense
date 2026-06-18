import streamlit as st

st.title('Supabase Rulesense')

choice = st.selectbox(
    "Choose the rule type you want",
    ["Read", "Edit/Delete"]
)


if choice == "Read":
    A = st.text_input("The user's UI (user_id)")
    B = st.text_input("Rule name")
    C = st.text_input("Which table")

    st.code(f"""
CREATE POLICY "{B}"
ON public."{C}"
FOR SELECT
TO authenticated
USING (auth.uid() = '{A}');
""")
