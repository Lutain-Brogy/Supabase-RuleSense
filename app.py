import streamlit as st

st.title('Supabase Rulesense')


mode = st.selectbox("What would you like to do today", ["Write policy", "Ask questions"])

if mode == 'Write policy':
  Rule_type = st.selectbox(
    "Choose the required type of policy",
    ["SELECT", "INSERT", "UPDATE", "DELETE", "ALL", "REFERENCES", "TRIGGER"]
  )  
  
  if Rule_type == 'SELECT':
     st.write('Which type of read policy sir/madam?')
     tab1, tab2, = st.tabs(["Anyone can read", "One certain person"])

     with tab1:
       A = st.text_input('Policy name')
       B = st.selectbox('Table schema', 
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
      A = st.text_input('Policy name')
      B = st.selectbox('Table schema', 
         ["private", "public"])
      C = st.text_intpu('Table name')
      D = st.text_imput('User ID')
      st.code(f'''
CREATE POLICY "{A}"
ON {B}.{C}
FOR SELECT
TO authenticated
USING (auth.uid() = "{D}");
''')
    






                               
        
       
