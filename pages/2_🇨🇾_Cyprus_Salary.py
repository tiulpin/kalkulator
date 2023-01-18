import pandas as pd  # need this only because of the table shown
import streamlit as st

from kalkulators.taxes.common import WORKING_PERIODS
from kalkulators.taxes.cy_calc import (
    CyprusTaxesResult,
    CyprusTaxCalculator,
)
from kalkulators.taxes.cy_data import CY_DATA

RULING_URL = "https://www.pwc.com.cy/en/publications/assets/dtu-n8-2022.pdf"
DEFAULT_SALARY = 36000.00
DEFAULT_WORKING_HOURS = 40
NO_TAXES_MESSAGE = (
    "🎉 You are not paying any taxes because you are not earning any money"
)
EXPLANATIONS_TITLE = "The calculations are incorrect, what should I do?"
EXPLANATIONS = """#### 🤔 What are the formulas and how the calculator works?
1. You have to pay 2.65% to National Health Service and 8.3% for the Social insurance.
2. Then your salary is taxed by the payroll tax (progressive): depending on how big is your salary the different tax rate applies to you.

Also, it's possible to get a tax benefit (an exemption) on Cyprus if you are working there for the first time in your life.
It means that 20% (or 50%) if your income won't be taxed at all.

So the total tax is calculated the following way:
```
taxable_year = salary - social_tax - nhs_tax
payroll_tax(taxable_year)
```

Here are the bands for the payroll tax the last year:

| Taxable income band EUR	  | National income tax rates     |
|-----------------------------|------------------------------:|
| 0 to 19,500                 | 0%                            |
| 19,501 to 28,000            | 20%                           |
| 28,001 to 36,300            | 25%                           |
| 36,301 to 60,000            | 30%                           |
| 60,000 and more             | 35%                           |


#### 🤑 Your employee pays you some benefits or charges for something else
It could be a parking space you must pay for yourself. It could be the lunch allowance, insurance coverage, or travel 
allowance you get additionally. Just look inside your payslips. 
Given that the situation is different for every company, this calculator does only one job: 
approximate your annual income.


#### 🤷 The stupid developer made a mistake
If you think that the calculator is wrong, please [drop me a message](https://t.me/tiulpin), and I will fix it as soon as possible.
"""
DISCLAIMER = (
    "💡 **Disclaimer:** This is a demo app. The numbers may not be accurate. "
    "Consult a tax advisor for more information."
)
RULING_TIP = f"Cyprus tax benefit when 20% (or 50%) of your salary is not taxed. [More info about the exemption]({RULING_URL})"


def show_metrics(t: CyprusTaxesResult) -> None:
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


def show_table(t: CyprusTaxesResult) -> None:
    data = pd.DataFrame(
        {
            "EUR / YEAR": [t.social_tax, t.nhs_tax, t.taxable_income, t.payroll_tax],
        },
        index=[
            "Social Insurance Tax",
            "National Health Services Tax",
            "Taxable Income",
            "Payroll Tax",
        ],
    )
    st.table(data.style.format("{:,.2f}"))


st.set_page_config(page_title="Cyprus: Salary", page_icon="🇨🇾")
st.title("🇨🇾 Cyprus: Salary")
st.caption("Approximate how much money you get after the taxes")

tab_employed, tab_semployed = st.tabs(["Employed", "Self-employed"])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with tab_employed:
    left_col, right_col = st.columns(2)
    salary = left_col.number_input(
        "Salary in EUR",
        value=DEFAULT_SALARY
        if "salary" not in st.session_state
        else st.session_state["salary"],
        min_value=0.0,
        step=1000.0,
    )
    st.session_state["salary"] = salary
    ruling = left_col.checkbox("Payroll Tax exemption", help=RULING_TIP, value=True)
    period = right_col.radio("Working period", WORKING_PERIODS)

    with st.expander("Advanced options"):
        first_col, second_col, third_col = st.columns(3)
        year = first_col.selectbox("Year", list(reversed(CY_DATA["years"])))
        hours = second_col.number_input(
            "Weekly working hours",
            value=CY_DATA["defaultWorkingHours"],
            min_value=1,
            max_value=168,
        )

    calc = CyprusTaxCalculator(
        salary=salary,
        year=year,
        ruling=ruling,
        period=period,
        working_hours=hours,
        tax_data=CY_DATA,
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
