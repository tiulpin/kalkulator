import math
from dataclasses import dataclass

from kalkulators.taxes.common import get_rates


@dataclass
class CyprusTaxesResult:
    year_net_income: float
    taxable_income: float
    month_net_income: float
    hour_net_income: float
    payroll_tax: float
    social_tax: float
    nhs_tax: float


class CyprusTaxCalculator:
    """
    Tax calculator.
    Get user input data, base government tax data
    and calculate results.

    """

    __slots__ = (
        "_year",
        "_period",
        "_salary",
        "_ruling",
        "_working_hours",
        "_tax_data",
        "_working_periods",
    )

    def __init__(
        self,
        year,
        ruling,
        salary,
        period,
        working_hours,
        tax_data,
        working_periods,
    ):
        self._year = year
        self._period = period
        self._salary = salary
        self._ruling = ruling
        self._working_hours = working_hours
        self._tax_data = tax_data
        self._working_periods = working_periods

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

    def get_social_tax(self, year: str, salary: float) -> float:
        """
        Get social tax percent from base government tax data
        and calculate tax value.

        Args:
            year (str): Calculation year.
            salary (Number): Salary value.

        Returns:
            (Number): Social tax value.

        """
        return get_rates(
            brackets=self._tax_data["socialPercent"][year],
            salary=salary,
            rate_type="rate",
        )

    def get_nhs_tax(self, year: str, salary: float) -> float:
        """
        Get social tax percent from base government tax data
        and calculate tax value.

        Args:
            year (str): Calculation year.
            salary (Number): Salary value.

        Returns:
            (Number): Social tax value.

        """
        return get_rates(
            brackets=self._tax_data["nhs"][year],
            salary=salary,
            rate_type="rate",
        )

    def calculate(self) -> CyprusTaxesResult:
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

        tax_free_year = 0
        taxable_year = gross_year

        taxable_year = math.floor(taxable_year)
        social_tax = -1 * self.get_social_tax(self._year, salary=taxable_year)
        nhs_tax = -1 * self.get_nhs_tax(self._year, salary=taxable_year)
        taxable_year += social_tax + nhs_tax

        if self._ruling != "0%":
            if self._ruling == "20%":
                tax_free_year = taxable_year * 0.2
            elif self._ruling == "50%":
                tax_free_year = taxable_year * 0.5
            taxable_year -= tax_free_year

        income_tax = math.floor(
            -1 * self.get_payroll_tax(year=self._year, salary=taxable_year)
        )
        income_tax = income_tax if income_tax < 0 else 0

        year_net_income = taxable_year + income_tax + tax_free_year
        month_net_income = math.floor(year_net_income / 12)
        hour_net_income = math.floor(
            year_net_income / (self._tax_data["workingWeeks"] * self._working_hours)
        )

        return CyprusTaxesResult(
            year_net_income=year_net_income,
            taxable_income=taxable_year,
            month_net_income=month_net_income,
            payroll_tax=income_tax,
            hour_net_income=hour_net_income,
            social_tax=social_tax,
            nhs_tax=nhs_tax,
        )
