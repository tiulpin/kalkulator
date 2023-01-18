import math
from dataclasses import dataclass

from kalkulators.taxes.common import get_rates

RULING_TYPES = {
    "Normal": "normal",
    "Young & Master's": "young",
    "Research": "research",
    "None": "none",
}


@dataclass
class DutchTaxesResult:
    year_net_income: float
    taxable_income: float
    month_net_income: float
    payroll_tax: float
    social_security_tax: float
    general_tax_credit: float
    labour_tax_credit: float
    hour_net_income: float


class DutchTaxCalculator:
    """
    Tax calculator.
    Get user input data, base government tax data
    and calculate results.

    """

    __slots__ = (
        "_old_age",
        "_year",
        "_period",
        "_salary",
        "_ruling",
        "_working_hours",
        "_social_security",
        "_holiday_allowance",
        "_tax_data",
        "_working_periods",
    )

    def __init__(
        self,
        old_age,
        year,
        ruling,
        salary,
        period,
        working_hours,
        social_security,
        holiday_allowance,
        tax_data,
        working_periods,
    ):

        self._old_age = old_age
        self._year = year
        self._period = period
        self._salary = salary
        self._ruling = ruling
        self._working_hours = working_hours
        self._social_security = social_security
        self._holiday_allowance = holiday_allowance
        self._tax_data = tax_data
        self._working_periods = working_periods

    def get_ruling_income(self, year: str, ruling: str) -> int:
        """
        Get ruling threshold from base government tax data
        by year and ruling type.

        Args:
            year: Calculation year.
            ruling: Ruling type: "normal". "young", "research".

        Returns:
            Ruling threshold.

        """
        return self._tax_data["rulingThreshold"][year][ruling]

    def get_payroll_tax(self, year: str, salary: float) -> float:
        """
        Get payroll tax min, max and rate from base government tax data
        and calculate tax value.

        Args:
            year: Calculation year.
            salary: Salary value.

        Returns:
            Payroll tax value.

        """
        return get_rates(
            brackets=self._tax_data["payrollTax"][year], salary=salary, rate_type="rate"
        )

    def get_social_tax(self, year: str, salary: float, age: bool) -> float:
        """
        Get social tax percent from base government tax data
        and calculate tax value.

        Args:
            year (str): Calculation year.
            salary (Number): Salary value.
            age (bool): True if user is older 65 years, False otherwise.

        Returns:
            (Number): Social tax value.

        """
        return get_rates(
            brackets=self._tax_data["socialPercent"][year],
            salary=salary,
            rate_type="older" if age else "social",
        )

    def get_general_credit(self, year: str, salary: float) -> float:
        """
        Get general credit min, max and rate from base government tax data
        and calculate credit value.

        Args:
            year (str): Calculation year.
            salary (Number): Salary value.

        Returns:
            (Number): General credit value.

        """
        return get_rates(
            brackets=self._tax_data["generalCredit"][year],
            salary=salary,
            rate_type="rate",
        )

    def get_labour_credit(self, year: str, salary: float) -> float:
        """
        Get labour credit min, max and rate from base government tax data
        and calculate credit value.

        Args:
            year (str): Calculation year.
            salary (Number): Salary value.

        Returns:
            (Number): Labour credit value.

        """
        return get_rates(
            brackets=self._tax_data["labourCredit"][year],
            salary=salary,
            rate_type="rate",
        )

    def get_social_credit(self, year: str, age: bool, social_security: bool):
        """
        Get social credit percentage from base government tax data
        and calculate credit value.

        Args:
            year (str): Calculation year.
            age (bool): True is user is older 65 years, False otherwise.
            social_security (bool): True if social security is applied, False otherwise.

        Returns:
            (Number): Social credit percentage.

        """
        percentage = 1
        bracket = self._tax_data["socialPercent"][year][0]

        if not social_security:
            # Removing AOW + Anw + Wlz from total
            # Percentage of social contributions (AOW + Anw + Wlz)
            percentage = (bracket["rate"] - bracket["social"]) / bracket["rate"]
        elif age:
            # Removing only AOW from total
            # Percentage for retirement age (Anw + Wlz, no contribution to AOW)
            percentage = (
                bracket["rate"] + bracket["older"] - bracket["social"]
            ) / bracket["rate"]

        return percentage

    def calculate(self) -> DutchTaxesResult:
        """
        Main calculation method.

        Returns:
            (DutchTaxesResult): Calculation results.

        """
        salary_by_period = dict.fromkeys(self._working_periods, 0)
        salary_by_period[self._period] = self._salary

        gross_year = salary_by_period["year"]
        gross_year += salary_by_period["month"] * 12
        gross_year += salary_by_period["day"] * self._tax_data["workingDays"]
        gross_year += (
            salary_by_period["hour"]
            * self._tax_data["workingWeeks"]
            * self._working_hours
        )
        gross_year = max(gross_year, 0)

        gross_allowance = (
            math.floor(gross_year * (0.08 / 1.08)) if self._holiday_allowance else 0
        )

        tax_free_year = 0
        taxable_year = gross_year - gross_allowance

        if self._ruling != "None":
            ruling_income = self.get_ruling_income(
                year=self._year, ruling=RULING_TYPES[self._ruling]
            )

            if taxable_year > ruling_income:
                tax_free_year = taxable_year * 0.3
                taxable_year -= tax_free_year

        taxable_year = math.floor(taxable_year)

        payroll_tax = -1 * self.get_payroll_tax(year=self._year, salary=taxable_year)

        social_tax = (
            -1
            * self.get_social_tax(
                year=self._year,
                salary=taxable_year,
                age=self._old_age,
            )
            if self._social_security
            else 0
        )

        social_credit = self.get_social_credit(
            year=self._year,
            age=self._old_age,
            social_security=self._social_security,
        )

        general_credit = social_credit * self.get_general_credit(
            year=self._year, salary=taxable_year
        )

        labour_credit = social_credit * self.get_labour_credit(
            year=self._year, salary=taxable_year
        )

        income_tax = math.floor(
            payroll_tax + social_tax + general_credit + labour_credit
        )
        income_tax = income_tax if income_tax < 0 else 0

        year_net_income = taxable_year + income_tax + tax_free_year

        # holiday allowance: math.floor(net_year * (0.08 / 1.08)) if self._holiday_allowance else 0
        # day income: math.floor(net_year / NL_DATA["workingDays"])
        # calculated_total_income_tax income_tax
        # Add calculated data to result
        # result["calculated_year_gross_ha"] = gross_allowance
        # result["calculated_year_gross_income"] = math.floor(gross_year)
        # result["calculated_month_gross_income"] = math.floor(gross_year / 12)
        # result["calculated_day_gross_income"] = math.floor(gross_year / NL_DATA["workingDays"])
        # result["calculated_hour_gross_income"] = math.floor(gross_year / (NL_DATA["workingWeeks"] * self._working_hours))
        # result["calculated_tax_free_income"] = math.floor(tax_free_year)
        # result["calculated_ruling_percentage"] = math.floor(tax_free_year / gross_year * 100)
        # result["calculated_taxable_income"] = taxable_year

        month_net_income = math.floor(year_net_income / 12)
        hour_net_income = math.floor(
            year_net_income / (self._tax_data["workingWeeks"] * self._working_hours)
        )

        return DutchTaxesResult(
            year_net_income=year_net_income,
            taxable_income=taxable_year,
            month_net_income=month_net_income,
            payroll_tax=payroll_tax,
            social_security_tax=social_tax,
            general_tax_credit=general_credit,
            labour_tax_credit=labour_credit,
            hour_net_income=hour_net_income,
        )
