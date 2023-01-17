import pandas as pd  # need this only because of the table shown
import streamlit as st

from nl_taxes_lib import (
    WORKING_PERIODS,
    DEFAULT_SALARY,
    RULING_TIP,
    NL_DATA,
    DISCLAIMER,
    TaxesResult,
    RULING_TYPES,
    TaxCalculator,
)


def show_metrics(t: TaxesResult):
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
                t.year_net_income,
                t.month_net_income,
                t.payroll_tax,
                t.social_security_tax,
                t.general_tax_credit,
                t.labour_tax_credit,
            ],
        },
        index=[
            "Taxable Income",
            "Year Net Income",
            "Month Net Income",
            "Payroll Tax",
            "Social Security Tax",
            "General Tax Credit",
            "Labour Tax Credit",
        ],
    )
    st.table(data.style.format("{:.2f}"))


st.set_page_config(page_title="Netherlands Salary", page_icon="🇳🇱")
st.title("🇳🇱 Netherlands Salary")
st.caption("Calculate how much money you get after the taxes")

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
    holiday_allowance_included = st.checkbox("Holiday allowance included", value=True)
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
)
tax_results = calc.calculate()
show_metrics(tax_results)
if tax_results.year_net_income > 0:
    show_table(tax_results)
else:
    st.success("🎉 You are not paying any taxes because you are not earning any money")
    st.balloons()
st.caption(DISCLAIMER)
