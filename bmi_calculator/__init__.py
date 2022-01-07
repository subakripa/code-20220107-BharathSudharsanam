from pandas import DataFrame, Series, cut
from typing import List, Tuple, Any
from include import input_data
from logging import getLogger

logger = getLogger(__name__)


def read_input() -> DataFrame:

    return DataFrame.from_dict(input_data)


def get_reference_data() -> Tuple[List[Any], List[Any], List[Any]]:
    """
    This we can replace with file load or DB load to get the reference data.
    :return:
    """
    cat_labels = ['Underweight', 'Normal Weight', 'Overweight', 'Moderately Obese', 'Severely Obese',
                  'Very Severely Obese']
    risk_labels = ['Malnutrition Risk', 'Low Risk', 'Enhanced Risk', 'Medium Risk', 'High Risk',
                   'Very High Risk']
    buckets = [0, 18.4, 24.9, 29.9, 34.9, 39.9, 40]

    return cat_labels, risk_labels, buckets


def calculate_bmi(series: Series) -> float:
    """

    :param series: Numpy series on which new fields are calculated
    :return: Value of the new column
    """

    height_in_metre = series['HeightCm']/100
    metre_squared = round(height_in_metre * height_in_metre, 2)
    return round(series['WeightKg'] / metre_squared, 2)


def main() -> None:
    df = read_input()
    cat_labels, risk_labels, buckets = get_reference_data()
    df['BMI'] = df.apply(calculate_bmi, axis=1)
    df['BMI_Category'] = cut(x=df['BMI'], bins=buckets, labels=cat_labels)
    df['Health_Risk'] = cut(x=df['BMI'], bins=buckets, labels=risk_labels)
    overweight_count = len(df[df['BMI_Category'] == 'Overweight'])
    print(f"Number of persons in category - overweight: {overweight_count}")


if __name__ == "__main__":
    main()
