import pytest
from pandas import DataFrame, Series
from bmi_calculator import read_input, get_reference_data, calculate_bmi, main


def test_read_input():
    test_df = read_input()
    assert isinstance(test_df, DataFrame)
    test_cols = test_df.columns
    assert len(test_cols) == 3


def test_get_reference_data():
    test_cat_labels, test_risk_labels, test_bins = get_reference_data()
    assert 'Underweight' in test_cat_labels
    assert 'Enhanced Risk' in test_risk_labels
    assert 40 in test_bins


def test_calculate_bmi():

    test_series = Series([171, 96], index=['HeightCm', 'WeightKg'])
    actual_value = calculate_bmi(test_series)
    expected_value = 32.88
    assert expected_value == actual_value
