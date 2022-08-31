import typing

rate_system = {0 : 0.7,
               1000 : 0.5,
               5000 : 0.2}

def get_bonus_value(amount: float, rate_system: typing.Dict[float, float]) -> float:
    sorted_lower_boundaries = sorted(rate_system, reverse = True)
    result = 0
    for lower_boundary in sorted_lower_boundaries:
        if amount >= lower_boundary:
            result += (amount - lower_boundary) * rate_system[lower_boundary] / 100
            amount = lower_boundary

    return result

print(get_bonus_value(1200, rate_system))