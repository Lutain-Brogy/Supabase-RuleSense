import streamlit as st

st.title('Supabase Rulesense')

choice = st.selectbox(
    "Choose the rule type you want",
    ["Read", "Edit/Delete"]
)


if choice == "Read":
    A = st.text_input("Rule name")
    B = st.text_input("Which table is affected") 
    C = st.selectbox(
    'For',
    ["Anyone logged in", "One certain person"]
)
    if C == 'Anyone logged in':
       C = "(true);"
    if C == 'One certain person':
        C = "(auth.uid() = '{D}');"
        D = st.text_input('Person id') 
        st.code(f"""
CREATE POLICY "{A}"
ON public."{B}"
FOR SELECT
TO authenticated
USING {C}

""")







