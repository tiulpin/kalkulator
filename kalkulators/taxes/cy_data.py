CY_DATA = {
    "currentYear": "2023",
    "years": ["2022", "2023"],
    "defaultWorkingHours": 40,
    "workingWeeks": 52,
    "workingDays": 255,
    "rulingThreshold": {
        "2022": {"normal": 55000},
        "2023": {"normal": 55000},
    },
    "payrollTax": {
        "2022": [
            {"bracket": 1, "min": 0, "max": 19500, "rate": 0.0},
            {"bracket": 2, "min": 19501, "max": 28000, "rate": 0.2},
            {"bracket": 3, "min": 28001, "max": 36300, "rate": 0.25},
            {"bracket": 4, "min": 36301, "max": 60000, "rate": 0.3},
            {"bracket": 5, "min": 60001, "rate": 0.35},
        ],
        "2023": [
            {"bracket": 1, "min": 0, "max": 19500, "rate": 0.0},
            {"bracket": 2, "min": 19501, "max": 28000, "rate": 0.2},
            {"bracket": 3, "min": 28001, "max": 36300, "rate": 0.25},
            {"bracket": 4, "min": 36301, "max": 60000, "rate": 0.3},
            {"bracket": 5, "min": 60001, "rate": 0.35},
        ],
    },
    "socialPercent": {
        "2022": [{"bracket": 1, "min": 0, "max": 58080, "rate": 0.083}],
        "2023": [{"bracket": 1, "min": 0, "max": 58080, "rate": 0.083}],
    },
    "nhs": {
        "2022": [{"bracket": 1, "min": 0, "rate": 0.0265}],
        "2023": [{"bracket": 1, "min": 0, "rate": 0.0265}],
    },
}
