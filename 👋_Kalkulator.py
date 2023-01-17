import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Kalkulator! 👋")

st.sidebar.success("Select a calculator you need above.")

st.markdown(
    """
    Kalkulator is just a simple online collection of calculators me and my friends use.
    
    **👈  Select a calculator from the sidebar** to get started.

    ### Show me what you've got!
    - Check out salaries in the different countries and regions:
        - 🇳🇱 [Netherlands](/Netherlands_Salary)
        - 🗿 Other counties coming soon 🇦🇲🇩🇪🇷🇸🇨🇾
    - Calculate whether you should buy a house or rent
    - Find out what's cheaper: buying or leasing a car
        
    ### Submit a calculator request
    Go to our GitHub and create a new [GitHub issue](https://github.com/tiulpin/kalkulator/issues/new?assignees=&labels=calculator&template=calculator-request.md&title=)
"""
)

snow = st.button("Make it snow!")
if snow:
    st.snow()
