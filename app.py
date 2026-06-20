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
        A = st.text_input('Name/description')
        B = st.text_input('Name of table')
        st.code(f'''
CREATE POLICY "{A}"
ON public."{B}"
FOR SELECT
TO authenticated
USING (true);
''') 

    if C == 'One certain person':
        A = st.text_input('Policy name/role')
        B = st.text_input('Table name')
        C = St.text_input('User ID')
        st.code(f'''
CREATE POLICY "{A}"
ON public."{B}"
FOR SELECT
TO authenticated
USING (auth.uid() = "{C}");
''')







