import streamlit as st

st.title('Supabase Rulesense')


start1, start2, start3 = st.tabs(["Write policy", "Ask questions" , "Smart policy generating"])
with start2:
   user_input = st.text_input
   
with start1:
   write_type = st.selectbox(["Explanatory", "Straightforward"])
   if write_type == 'Explanatory':
     user_input = st.text_input

   if write_type == 'Straightforward':
      Rule_type = st.selectbox("Choose the required type of policy",
                           ["SELECT", "INSERT", "UPDATE", "DELETE", "ALL", "REFERENCES", "TRIGGER"])
  
  if Rule_type == 'SELECT':
     st.write('Which type of read policy sir/madam?')
     tab1, tab2, = st.tabs(["Anyone can read", "One certain person"])

     with tab1:
       A = st.text_input('Policy name')
       B = st.selectbox('table schema', 
         ["private", "public"])
  
       C = st.text_input('Table name')
       st.code(f'''
CREATE POLICY "{A}"
ON {B}."{C}"
FOR SELECT
TO authenticated
USING (true);
''')
  with tab2:
    A = st.text_input("policy name")
    B = st.selectbox(
        "Table schema",
        ["private", "public"]
    )
    C = st.text_input("table name")
    D = st.text_input("User ID")

    st.code(f'''
CREATE POLICY "{A}"
ON {B}."{C}"
FOR SELECT
TO authenticated
USING (auth.uid() = '{D}');
''')

 






                               
        
       
