from app import get_bonus_value, rate_system

def test_get_bonus_value_initial():
    """ Initial conditions """
    assert get_bonus_value(1200, rate_system) == 8.0

def test_get_bonus_value_10000():
    """ 5000*0.2% + 4000*0.5% + 1000*0.7% = 10 + 20 + 7 = 37 """
    assert get_bonus_value(10000, rate_system) == 37.0

def test_get_bonus_value_0():
    """ No bonus """
    assert get_bonus_value(0, rate_system) == 0

def test_get_bonus_value_negative():
    """ No bonus for negative amounts"""
    assert get_bonus_value(-1123, rate_system) == 0

def test_get_bonus_value_change_rates():
    """ Initial amount except new rates. 1000*0.7% + 200*0.6% = 8.2 """
    new_rates = rate_system.copy()
    new_rates[1000] = 0.6
    assert get_bonus_value(1200, new_rates) == 8.2

def test_get_bonus_value_new_rates_above():
    """ 
        Adding new range above 
        3500*0.1% + 1500*0.2% *  4000*0.5% + 1000*0.7% = 10 + 20 + 7 = 33.5
    """

    new_rates = rate_system.copy()
    new_rates[6500] = 0.1
    assert get_bonus_value(10000, new_rates) == 33.5

def test_get_bonus_value_new_rates_between():
    """ Adding new range between """

    new_rates = rate_system.copy()
    new_rates[2500] = 0.4
    assert get_bonus_value(4500, new_rates) == 22.5