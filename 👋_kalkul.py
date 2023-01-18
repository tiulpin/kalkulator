import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Kalkul! 👋")

st.sidebar.success("Select a calculator you need above.")

st.markdown(
    """
    Kalkul is just a simple online collection of calculators me and my friends use.
    
    **👈  Select a calculator from the sidebar** to get started.

    ### Show me what you've got!
    - Check out salaries in the different countries and regions:
        - 🇳🇱 [Netherlands](/tax_nl)
        - 🇨🇾 [Cyprus](/tax_cy)
        - 🗿 Other countries coming soon 🇦🇲🇩🇪🇷🇸
    - Calculate whether you should buy a house or rent
    - Find out what's cheaper: buying or leasing a car
        
    ### Submit a calculator request
    Just [drop me a message](https://t.me/tiulpin) and I'll add it to the list.
"""
)

snow = st.button("Make it snow!")
if snow:
    st.snow()
