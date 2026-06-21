import streamlit as st

st.title('Supabase Rulesense')

 #start2, start3
start1, = st.tabs(["Write policy"])  # "Ask questions", "Smart policy generating"

with start1:
 tab1, tab2 = st.tabs(
        ["Explanatory", "Straightforward"]
    )
    
with tab1:
 user_input = st.text_input("Describe what you want the policy to do")


with tab2:
 Rule_type = st.selectbox("Choose the required type of policy",
                         ["SELECT", "INSERT", "UPDATE", "DELETE", "ALL", "REFERENCES", "TRIGGER"]
        )
   
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

 






                               
        
       
