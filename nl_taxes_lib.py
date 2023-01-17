from dataclasses import dataclass
import math

RULING_URL = (
    "https://belastingdienst.nl/wps/wcm/connect/en/individuals/content/"
    "coming-to-work-in-the-netherlands-30-percent-facility"
)
DEFAULT_SALARY = 60000.00
DEFAULT_WORKING_HOURS = 40

DISCLAIMER = (
    "💡 **Disclaimer:** This is a demo app. The numbers may not be accurate. "
    "Consult a tax advisor for more information."
)
RULING_TIP = f"More information about the 30% ruling [🔗here]({RULING_URL})"
WORKING_PERIODS = ("year", "month", "day", "hour")
RULING_TYPES = {
    "Normal": "normal",
    "Young Employee with Master's": "young",
    "Research": "research",
    "None": "none",
}

# The data can be obtained from the official website of the Dutch tax authority
# https://www.belastingdienst.nl/wps/wcm/connect/nl/personeel-en-loon/content/hulpmiddel-loonbelastingtabellen
# Though this dictionary is imported from the wonderful https://thetax.nl/ website
# https://raw.githubusercontent.com/stevermeister/dutch-tax-income-calculator-npm/ae6bb245d8becd2cb7e584c3a6ddca22c5fbcc8e/data.json
NL_DATA = {
    "currentYear": "2023",
    "years": ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"],
    "defaultWorkingHours": 40,
    "workingWeeks": 52,
    "workingDays": 255,
    "rulingThreshold": {
        "2015": {"normal": 36705, "young": 27901, "research": 0},
        "2016": {"normal": 36889, "young": 28041, "research": 0},
        "2017": {"normal": 37000, "young": 28125, "research": 0},
        "2018": {"normal": 37296, "young": 28350, "research": 0},
        "2019": {"normal": 37743, "young": 28690, "research": 0},
        "2020": {"normal": 38347, "young": 29149, "research": 0},
        "2021": {"normal": 38961, "young": 29616, "research": 0},
        "2022": {"normal": 39467, "young": 30001, "research": 0},
        "2023": {"normal": 41954, "young": 31891, "research": 0},
    },
    "payrollTax": {
        "2015": [
            {"bracket": 1, "min": 0, "max": 19822, "rate": 0.0835},
            {"bracket": 2, "min": 19823, "max": 33589, "rate": 0.1385},
            {"bracket": 3, "min": 33590, "max": 57585, "rate": 0.42},
            {"bracket": 4, "min": 57586, "rate": 0.52},
        ],
        "2016": [
            {"bracket": 1, "min": 0, "max": 19922, "rate": 0.0840},
            {"bracket": 2, "min": 19923, "max": 33715, "rate": 0.1205},
            {"bracket": 3, "min": 33716, "max": 66421, "rate": 0.402},
            {"bracket": 4, "min": 66422, "rate": 0.52},
        ],
        "2017": [
            {"bracket": 1, "min": 0, "max": 19981, "rate": 0.089},
            {"bracket": 2, "min": 19982, "max": 33790, "rate": 0.1315},
            {"bracket": 3, "min": 33791, "max": 67071, "rate": 0.408},
            {"bracket": 4, "min": 67072, "rate": 0.52},
        ],
        "2018": [
            {"bracket": 1, "min": 0, "max": 20141, "rate": 0.089},
            {"bracket": 2, "min": 20142, "max": 33993, "rate": 0.132},
            {"bracket": 3, "min": 33994, "max": 68506, "rate": 0.4085},
            {"bracket": 4, "min": 68507, "rate": 0.5195},
        ],
        "2019": [
            {"bracket": 1, "min": 0, "max": 20383, "rate": 0.09},
            {"bracket": 2, "min": 20384, "max": 34299, "rate": 0.1045},
            {"bracket": 3, "min": 34300, "max": 68506, "rate": 0.381},
            {"bracket": 4, "min": 68507, "rate": 0.5175},
        ],
        "2020": [
            {"bracket": 1, "min": 0, "max": 34711, "rate": 0.097},
            {"bracket": 2, "min": 34712, "max": 68507, "rate": 0.3735},
            {"bracket": 3, "min": 68507, "rate": 0.495},
        ],
        "2021": [
            {"bracket": 1, "min": 0, "max": 35129, "rate": 0.0945},
            {"bracket": 2, "min": 35130, "max": 68507, "rate": 0.3710},
            {"bracket": 3, "min": 68508, "rate": 0.495},
        ],
        "2022": [
            {"bracket": 1, "min": 0, "max": 35472, "rate": 0.0942},
            {"bracket": 2, "min": 35473, "max": 69399, "rate": 0.3707},
            {"bracket": 3, "min": 69399, "rate": 0.495},
        ],
        "2023": [
            {"bracket": 1, "min": 0, "max": 37149, "rate": 0.0928},
            {"bracket": 2, "min": 37150, "max": 73031, "rate": 0.3693},
            {"bracket": 3, "min": 73032, "rate": 0.495},
        ],
    },
    "socialPercent": {
        "2015": [
            {
                "bracket": 1,
                "min": 0,
                "max": 33590,
                "rate": 0.3650,
                "social": 0.2815,
                "older": 0.1025,
            }
        ],
        "2016": [
            {
                "bracket": 1,
                "min": 0,
                "max": 33716,
                "rate": 0.3655,
                "social": 0.2815,
                "older": 0.1025,
            }
        ],
        "2017": [
            {
                "bracket": 1,
                "min": 0,
                "max": 33791,
                "rate": 0.3655,
                "social": 0.2765,
                "older": 0.0975,
            }
        ],
        "2018": [
            {
                "bracket": 1,
                "min": 0,
                "max": 33994,
                "rate": 0.3655,
                "social": 0.2765,
                "older": 0.0975,
            }
        ],
        "2019": [
            {
                "bracket": 1,
                "min": 0,
                "max": 34300,
                "rate": 0.3665,
                "social": 0.2765,
                "older": 0.0975,
            }
        ],
        "2020": [
            {
                "bracket": 1,
                "min": 0,
                "max": 34712,
                "rate": 0.3735,
                "social": 0.2765,
                "older": 0.0975,
            }
        ],
        "2021": [
            {
                "bracket": 1,
                "min": 0,
                "max": 35129,
                "rate": 0.3710,
                "social": 0.2765,
                "older": 0.0975,
            }
        ],
        "2022": [
            {
                "bracket": 1,
                "min": 0,
                "max": 35472,
                "rate": 0.3707,
                "social": 0.2765,
                "older": 0.0975,
            }
        ],
        "2023": [
            {
                "bracket": 1,
                "min": 0,
                "max": 37150,
                "rate": 0.3693,
                "social": 0.2765,
                "older": 0.0975,
            }
        ],
    },
    "generalCredit": {
        "2015": [
            {"bracket": 1, "min": 0, "max": 19822, "rate": 2203},
            {"bracket": 2, "min": 19823, "max": 56935, "rate": -0.02320},
            {"bracket": 3, "min": 56936, "rate": 1342},
        ],
        "2016": [
            {"bracket": 1, "min": 0, "max": 19922, "rate": 2242},
            {"bracket": 2, "min": 19923, "max": 66417, "rate": -0.04822},
            {"bracket": 3, "min": 66418, "rate": 0},
        ],
        "2017": [
            {"bracket": 1, "min": 0, "max": 19982, "rate": 2254},
            {"bracket": 2, "min": 19983, "max": 67068, "rate": -0.04787},
            {"bracket": 3, "min": 67069, "rate": 0},
        ],
        "2018": [
            {"bracket": 1, "min": 0, "max": 20142, "rate": 2265},
            {"bracket": 2, "min": 20143, "max": 68507, "rate": -0.04683},
            {"bracket": 3, "min": 68508, "rate": 0},
        ],
        "2019": [
            {"bracket": 1, "min": 0, "max": 20384, "rate": 2477},
            {"bracket": 2, "min": 20384, "max": 68507, "rate": -0.05147},
            {"bracket": 3, "min": 68508, "rate": 0},
        ],
        "2020": [
            {"bracket": 1, "min": 0, "max": 20711, "rate": 2711},
            {"bracket": 2, "min": 20711, "max": 68507, "rate": -0.05672},
            {"bracket": 3, "min": 68508, "rate": 0},
        ],
        "2021": [
            {"bracket": 1, "min": 0, "max": 21043, "rate": 2837},
            {"bracket": 2, "min": 21043, "max": 68507, "rate": -0.05977},
            {"bracket": 3, "min": 68508, "rate": 0},
        ],
        "2022": [
            {"bracket": 1, "min": 0, "max": 21318, "rate": 2888},
            {"bracket": 2, "min": 21318, "max": 69398, "rate": -0.06007},
            {"bracket": 3, "min": 69399, "rate": 0},
        ],
        "2023": [
            {"bracket": 1, "min": 0, "max": 22661, "rate": 3070},
            {"bracket": 2, "min": 22661, "max": 73031, "rate": -0.06095},
            {"bracket": 3, "min": 73032, "rate": 0},
        ],
    },
    "labourCredit": {
        "2015": [
            {"bracket": 1, "min": 0, "max": 9010, "rate": 0.0181},
            {"bracket": 2, "min": 9011, "max": 19463, "rate": 0.19679},
            {"bracket": 3, "min": 19464, "max": 49770, "rate": 2220},
            {"bracket": 4, "min": 49771, "max": 100670, "rate": -0.04},
            {"bracket": 5, "min": 100671, "rate": 184},
        ],
        "2016": [
            {"bracket": 1, "min": 0, "max": 9147, "rate": 0.01793},
            {"bracket": 2, "min": 9148, "max": 19758, "rate": 0.27698},
            {"bracket": 3, "min": 19759, "max": 34015, "rate": 3103},
            {"bracket": 4, "min": 34016, "max": 111590, "rate": -0.04},
            {"bracket": 5, "min": 111591, "rate": 0},
        ],
        "2017": [
            {"bracket": 1, "min": 0, "max": 9309, "rate": 0.01772},
            {"bracket": 2, "min": 9310, "max": 20108, "rate": 0.28317},
            {"bracket": 3, "min": 20109, "max": 32444, "rate": 3223},
            {"bracket": 4, "min": 32445, "max": 121972, "rate": -0.036},
            {"bracket": 5, "min": 121973, "rate": 0},
        ],
        "2018": [
            {"bracket": 1, "min": 0, "max": 9468, "rate": 0.01764},
            {"bracket": 2, "min": 9469, "max": 20450, "rate": 0.28064},
            {"bracket": 3, "min": 20451, "max": 33112, "rate": 3249},
            {"bracket": 4, "min": 33113, "max": 123362, "rate": -0.036},
            {"bracket": 5, "min": 123363, "rate": 0},
        ],
        "2019": [
            {"bracket": 1, "min": 0, "max": 9694, "rate": 0.01754},
            {"bracket": 2, "min": 9694, "max": 20940, "rate": 0.28712},
            {"bracket": 3, "min": 20941, "max": 34060, "rate": 3399},
            {"bracket": 4, "min": 34061, "max": 90710, "rate": -0.06},
            {"bracket": 5, "min": 90711, "rate": 0},
        ],
        "2020": [
            {"bracket": 1, "min": 0, "max": 9921, "rate": 0.02812},
            {"bracket": 2, "min": 9921, "max": 21430, "rate": 0.28812},
            {"bracket": 3, "min": 21430, "max": 34954, "rate": 0.01656},
            {"bracket": 4, "min": 34954, "max": 98604, "rate": -0.06},
            {"bracket": 5, "min": 98604, "rate": 0},
        ],
        "2021": [
            {"bracket": 1, "min": 0, "max": 10108, "rate": 0.04581},
            {"bracket": 2, "min": 10108, "max": 21835, "rate": 0.28771},
            {"bracket": 3, "min": 21835, "max": 35652, "rate": 0.02663},
            {"bracket": 4, "min": 35652, "max": 105736, "rate": -0.06},
            {"bracket": 5, "min": 105736, "rate": 0},
        ],
        "2022": [
            {"bracket": 1, "min": 0, "max": 10351, "rate": 0.04541},
            {"bracket": 2, "min": 10351, "max": 22357, "rate": 0.28461},
            {"bracket": 3, "min": 22357, "max": 36650, "rate": 0.02610},
            {"bracket": 4, "min": 36650, "max": 109347, "rate": -0.05860},
            {"bracket": 5, "min": 109347, "rate": 0},
        ],
        "2023": [
            {"bracket": 1, "min": 0, "max": 10741, "rate": 0.08231},
            {"bracket": 2, "min": 10741, "max": 23201, "rate": 0.29861},
            {"bracket": 3, "min": 23201, "max": 37692, "rate": 0.03085},
            {"bracket": 4, "min": 37692, "max": 115296, "rate": -0.06510},
            {"bracket": 5, "min": 115296, "rate": 0},
        ],
    },
    "lowWageThreshold": {
        "2015": 6035,
        "2016": 6134,
        "2017": 6166,
        "2018": 6196,
        "2019": 6758,
        "2020": 7258,
        "2021": 7646,
        "2022": 7790,
        "2023": 8313,
    },
    "elderCredit": {
        "2015": [
            {"bracket": 1, "min": 0, "max": 35770, "rate": 1042},
            {"bracket": 2, "min": 35770, "rate": 152},
        ],
        "2016": [
            {"bracket": 1, "min": 0, "max": 35949, "rate": 1187},
            {"bracket": 2, "min": 35949, "rate": 70},
        ],
        "2017": [
            {"bracket": 1, "min": 0, "max": 36057, "rate": 1292},
            {"bracket": 2, "min": 36057, "rate": 71},
        ],
        "2018": [
            {"bracket": 1, "min": 0, "max": 36346, "rate": 1418},
            {"bracket": 2, "min": 36346, "rate": 72},
        ],
        "2019": [
            {"bracket": 1, "min": 0, "max": 36783, "rate": 1596},
            {"bracket": 2, "min": 36783, "max": 47423, "rate": -0.15},
            {"bracket": 3, "min": 47423, "rate": 0},
        ],
        "2020": [
            {"bracket": 1, "min": 0, "max": 37372, "rate": 1622},
            {"bracket": 2, "min": 37372, "max": 48185, "rate": -0.15},
            {"bracket": 3, "min": 48185, "rate": 0},
        ],
        "2021": [
            {"bracket": 1, "min": 0, "max": 37970, "rate": 1703},
            {"bracket": 2, "min": 37970, "max": 49323, "rate": -0.15},
            {"bracket": 3, "min": 49323, "rate": 0},
        ],
        "2022": [
            {"bracket": 1, "min": 0, "max": 38465, "rate": 1726},
            {"bracket": 2, "min": 38465, "max": 49972, "rate": -0.15},
            {"bracket": 3, "min": 49972, "rate": 0},
        ],
        "2023": [
            {"bracket": 1, "min": 0, "max": 40889, "rate": 1835},
            {"bracket": 2, "min": 40889, "max": 53123, "rate": -0.15},
            {"bracket": 3, "min": 53123, "rate": 0},
        ],
    },
}


@dataclass
class TaxesResult:
    year_net_income: float
    taxable_income: float
    month_net_income: float
    payroll_tax: float
    social_security_tax: float
    general_tax_credit: float
    labour_tax_credit: float
    hour_net_income: float


class TaxCalculator:
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
    ):

        self._old_age = old_age
        self._year = year
        self._period = period
        self._salary = salary
        self._ruling = ruling
        self._working_hours = working_hours
        self._social_security = social_security
        self._holiday_allowance = holiday_allowance

    @staticmethod
    def get_ruling_income(tax_data, year, ruling):
        """
        Get ruling threshold from base government tax data
        by year and ruling type.

        Args:
            tax_data (dict): Government tax data.
            year (str): Calculation year.
            ruling (str): Ruling type: "normal". "young", "research".

        Returns:
            (Number): Ruling threshold.

        """
        return tax_data["rulingThreshold"][year][ruling]

    @classmethod
    def get_payroll_tax(cls, tax_data, year, salary):
        """
        Get payroll tax min, max and rate from base government tax data
        and calculate tax value.

        Args:
            tax_data (dict): Government tax data.
            year (str): Calculation year.
            salary (Number): Salary value.

        Returns:
            (Number): Payroll tax value.

        """
        return cls.get_rates(
            brackets=tax_data["payrollTax"][year], salary=salary, rate_type="rate"
        )

    @classmethod
    def get_social_tax(cls, tax_data, year, salary, age):
        """
        Get social tax percent from base government tax data
        and calculate tax value.

        Args:
            tax_data (dict): Government tax data.
            year (str): Calculation year.
            salary (Number): Salary value.
            age (bool): True if user is older 65 years, False otherwise.

        Returns:
            (Number): Social tax value.

        """
        return cls.get_rates(
            brackets=tax_data["socialPercent"][year],
            salary=salary,
            rate_type="older" if age else "social",
        )

    @classmethod
    def get_general_credit(cls, tax_data, year, salary):
        """
        Get general credit min, max and rate from base government tax data
        and calculate credit value.

        Args:
            tax_data (dict): Government tax data.
            year (str): Calculation year.
            salary (Number): Salary value.

        Returns:
            (Number): General credit value.

        """
        return cls.get_rates(
            brackets=tax_data["generalCredit"][year], salary=salary, rate_type="rate"
        )

    @classmethod
    def get_labour_credit(cls, tax_data, year, salary):
        """
        Get labour credit min, max and rate from base government tax data
        and calculate credit value.

        Args:
            tax_data (dict): Government tax data.
            year (str): Calculation year.
            salary (Number): Salary value.

        Returns:
            (Number): Labour credit value.

        """
        return cls.get_rates(
            brackets=tax_data["labourCredit"][year], salary=salary, rate_type="rate"
        )

    @staticmethod
    def get_social_credit(tax_data, year, age, social_security):
        """
        Get social credit percentage from base government tax data
        and calculate credit value.

        Args:
            tax_data (dict): Government tax data.
            year (str): Calculation year.
            age (bool): True is user is older 65 years, False otherwise.
            social_security (bool): True if social security is applied, False otherwise.

        Returns:
            (Number): Social credit percentage.

        """
        percentage = 1
        bracket = tax_data["socialPercent"][year][0]

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

    @staticmethod
    def get_rates(brackets, salary, rate_type):
        """
        Helper method to calculate rates
        for Payroll Tax, Social Tax, General Credit, Labour Credit.

        Args:
            brackets (list[dict]): Data brackets by year with min, max and rate values.
            salary (Number): Salary value.
            rate_type (str): Rate type: "rate", "older", "social".

        Returns:
            (Number): Calculated amount.

        """
        amount = 0

        for bracket in brackets:
            delta = bracket["max"] - bracket["min"] if "max" in bracket else math.inf
            tax = bracket.get(rate_type, "rate")
            is_percent_valid = -1 < tax < 1 and tax != 0

            if salary <= delta:
                amount = (
                    amount + round((salary * 100 * tax) / 100, 2)
                    if is_percent_valid
                    else tax
                )
                break
            else:
                amount = amount + (delta * tax) if is_percent_valid else tax
                salary -= delta

        return amount

    def calculate(self) -> TaxesResult:
        """
        Main calculation method.

        Returns:
            (TaxesResult): Calculation results.

        """

        # Calculation part
        salary_by_period = dict.fromkeys(WORKING_PERIODS, 0)
        salary_by_period[self._period] = self._salary

        gross_year = salary_by_period["year"]
        gross_year += salary_by_period["month"] * 12
        gross_year += salary_by_period["day"] * NL_DATA["workingDays"]
        gross_year += (
            salary_by_period["hour"] * NL_DATA["workingWeeks"] * self._working_hours
        )
        gross_year = max(gross_year, 0)

        gross_allowance = (
            math.floor(gross_year * (0.08 / 1.08)) if self._holiday_allowance else 0
        )

        tax_free_year = 0
        taxable_year = gross_year - gross_allowance

        if self._ruling != "None":
            ruling_income = self.get_ruling_income(
                tax_data=NL_DATA, year=self._year, ruling=RULING_TYPES[self._ruling]
            )

            if taxable_year > ruling_income:
                tax_free_year = taxable_year * 0.3
                taxable_year -= tax_free_year

        taxable_year = math.floor(taxable_year)

        payroll_tax = -1 * self.get_payroll_tax(
            tax_data=NL_DATA, year=self._year, salary=taxable_year
        )

        social_tax = (
            -1
            * self.get_social_tax(
                tax_data=NL_DATA,
                year=self._year,
                salary=taxable_year,
                age=self._old_age,
            )
            if self._social_security
            else 0
        )

        social_credit = self.get_social_credit(
            tax_data=NL_DATA,
            year=self._year,
            age=self._old_age,
            social_security=self._social_security,
        )

        general_credit = social_credit * self.get_general_credit(
            tax_data=NL_DATA, year=self._year, salary=taxable_year
        )

        labour_credit = social_credit * self.get_labour_credit(
            tax_data=NL_DATA, year=self._year, salary=taxable_year
        )

        income_tax = math.floor(
            payroll_tax + social_tax + general_credit + labour_credit
        )
        income_tax = income_tax if income_tax < 0 else 0

        net_year = taxable_year + income_tax + tax_free_year

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

        month_net_income = math.floor(net_year / 12)
        hour_net_income = math.floor(
            net_year / (NL_DATA["workingWeeks"] * self._working_hours)
        )

        return TaxesResult(
            year_net_income=net_year,
            taxable_income=taxable_year,
            month_net_income=month_net_income,
            payroll_tax=payroll_tax,
            social_security_tax=social_tax,
            general_tax_credit=general_credit,
            labour_tax_credit=labour_credit,
            hour_net_income=hour_net_income,
        )
