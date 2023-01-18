import pandas as pd  # need this only because of the table shown
import streamlit as st

from kalkulators.nl_taxes.calc import (
    TaxesResult,
    TaxCalculator,
    RULING_TYPES,
    WORKING_PERIODS,
)
from kalkulators.nl_taxes.data import NL_DATA

RULING_URL = (
    "https://belastingdienst.nl/wps/wcm/connect/en/individuals/content/"
    "coming-to-work-in-the-netherlands-30-percent-facility"
)
DEFAULT_SALARY = 60000.00
DEFAULT_WORKING_HOURS = 40
NO_TAXES_MESSAGE = (
    "🎉 You are not paying any taxes because you are not earning any money"
)
EXPLANATIONS_TITLE = "The calculations are incorrect, what should I do?"
EXPLANATIONS = """#### 🤔 What are the formulas and how the calculator works?
The calculations are perfectly explained in 
[iamexpat.nl article](https://www.iamexpat.nl/expat-info/taxation/dutch-tax-system).


#### 🤑 Your employee pays you some benefits or charges for something else
It could be a parking space you must pay for yourself. It could be the lunch allowance, insurance coverage, or travel 
allowance you get additionally. Just look inside your payslips. 
Given that the situation is different for every company, this calculator does only one job: 
approximate your annual income.

#### 👮 You might be eligible for a tax refund if you didn't work the entire year
When you get your salary, you pay taxes based on your annual income (from the contract), but when you work only for 
part of the year, your actual payment might be lower than your expected yearly income. 
That is why you could get a refund from the tax services; you will have to fill in the tax declaration. 
More information about filling out the declaration can be found in 
[iamexpat.nl article](https://www.iamexpat.nl/expat-info/taxation/annual-dutch-tax-form).

#### 🤷 The stupid developer made a mistake
If you think that the calculator is wrong, please [drop me a message](https://t.me/tiulpin), and I will fix it as soon as possible.
"""
DISCLAIMER = (
    "💡 **Disclaimer:** This is a demo app. The numbers may not be accurate. "
    "Consult a tax advisor for more information."
)
RULING_TIP = f"More information about the 30% ruling 🔗[here]({RULING_URL})"


def show_metrics(t: TaxesResult) -> None:
    def display_metric(block, title, value, key):
        delta = (value - st.session_state[key]) if key in st.session_state else 0
        display_value = f"{value:,.2f} €"
        if delta != 0:
            display_delta = (
                f"{delta:.2f} € more" if delta > 0 else f"{delta:.2f} € less"
            )
            block.metric(title, display_value, display_delta)
        else:
            block.metric(title, display_value)
        st.session_state[key] = value

    st.markdown("#### Total Net Income")
    main_col1, main_col2, main_col3 = st.columns(3)
    display_metric(main_col1, "Per Year", t.year_net_income, "year_prev_net")
    display_metric(main_col2, "Per Month", t.month_net_income, "month_prev_net")
    display_metric(main_col3, "Per Hour", t.hour_net_income, "hour_prev_net")


def show_table(t: TaxesResult) -> None:
    data = pd.DataFrame(
        {
            "EUR": [
                t.taxable_income,
                t.payroll_tax,
                t.social_security_tax,
                t.general_tax_credit,
                t.labour_tax_credit,
            ],
        },
        index=[
            "Taxable Income",
            "Payroll Tax",
            "Social Security Tax",
            "General Tax Credit",
            "Labour Tax Credit",
        ],
    )
    st.table(data.style.format("{:,.2f}"))


st.set_page_config(page_title="Netherlands: Salary", page_icon="🇳🇱")
st.title("🇳🇱 Netherlands: Salary")
st.caption("Calculate how much money you get after the taxes")

tab_employed, tab_semployed = st.tabs(["Employed", "Self-employed"])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with tab_employed:
    income_col, period_col = st.columns(2)
    income = income_col.number_input(
        "Income in EUR", value=DEFAULT_SALARY, min_value=0.0, step=1000.0
    )
    period = period_col.selectbox("Period", WORKING_PERIODS)
    ruling = st.checkbox("30% facility", help=RULING_TIP, value=True)
    ruling_type = "Normal"

    with st.expander("Advanced options"):
        first_col, second_col = st.columns(2)
        year = first_col.selectbox("Year", list(reversed(NL_DATA["years"])))
        hours = second_col.number_input(
            "Weekly working hours", value=NL_DATA["defaultWorkingHours"], min_value=1
        )
        holiday_allowance_included = st.checkbox(
            "Holiday allowance included", value=True
        )
        social_security = st.checkbox("Social security", value=True)
        old_age = st.checkbox("66 years or older", value=False)
        if ruling:
            ruling_type = st.selectbox("Ruling Type", RULING_TYPES.keys())
        else:
            ruling_type = "None"

    calc = TaxCalculator(
        salary=income,
        old_age=old_age,
        year=year,
        ruling=ruling_type,
        period=period,
        working_hours=hours,
        social_security=social_security,
        holiday_allowance=holiday_allowance_included,
        tax_data=NL_DATA,
        working_periods=WORKING_PERIODS,
    )
    tax_results = calc.calculate()
    show_metrics(tax_results)
    if tax_results.year_net_income > 0:
        show_table(tax_results)
    else:
        st.success(NO_TAXES_MESSAGE)
        st.balloons()

with tab_semployed:
    st.markdown(
        """
    ### Coming soon...
    
    Meanwhile, you can watch the following relaxing video:"""
    )
    st.video("https://www.youtube.com/watch?v=3FMyeGw6Tn0")

with st.expander(EXPLANATIONS_TITLE):
    st.markdown(EXPLANATIONS)

st.caption(DISCLAIMER)
