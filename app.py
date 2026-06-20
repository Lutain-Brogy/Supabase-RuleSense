import streamlit as st

st.title('Supabase Rulesense')
user_input = st.text_input


mode = st.selectbox('What would you like to do today'
                    ["Write policy", "Ask questiond"]
                   )

if mode == 'What would you like to do today':

  Rule_type = st.selectbox('Choose the required type of policy'
                           [ "SELECT",  "INSERT", "UPDATE", "DELETE","ALL", "REFERENCES" , "TRIGGER" ]
                          )
  
        
       
