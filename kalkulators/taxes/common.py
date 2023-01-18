import math
from typing import List


WORKING_PERIODS = ("year", "month", "day", "hour")


def get_rates(brackets: List[dict], salary: float, rate_type: str) -> float:
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
