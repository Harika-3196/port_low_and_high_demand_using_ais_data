from typing import List
import unittest
import pandas as pd

from scripts.demand_identification import get_cargo_vessels_within_bounding_box, count_unique_vessels_by_time

class TestDemandIdentification(unittest.TestCase):
    def test_get_cargo_vessels_within_bounding_box(self) -> None:
        """
        Test case for the get_cargo_vessels_within_bounding_box function.

        This function tests if the get_cargo_vessels_within_bounding_box function returns
        a pandas DataFrame. It uses the get_cargo_vessels_within_bounding_box function with
        sample input parameters and asserts that the returned object is an instance of
        pandas DataFrame.

        Args:
            self (TestDemandIdentification): The current test case instance.

        Returns:
            None: This function does not return anything.
        """

        # Define input parameters
        port_code: str = 'USLGB'
        width: float = 10.0
        height: float = 10.0
        cargo_vessel_types: List[str] = ['Cargo Vessel']

        # Call the function to be tested
        df: pd.DataFrame = get_cargo_vessels_within_bounding_box(port_code, width, height, cargo_vessel_types)

        # Assert that the returned object is a pandas DataFrame
        self.assertIsInstance(df, pd.DataFrame)

    def test_count_unique_vessels_by_time(self) -> None:
        """
        Test case for the count_unique_vessels_by_time function.

        This function tests if the count_unique_vessels_by_time function returns
        a pandas DataFrame. It uses the count_unique_vessels_by_time function with
        sample input parameters and asserts that the returned object is an instance of
        pandas DataFrame.

        Args:
            self (TestDemandIdentification): The current test case instance.

        Returns:
            None: This function does not return anything.
        """

        # Define input parameters
        port_code: str = 'USLGB'  # type: ignore
        width: float = 10.0
        height: float = 10.0
        cargo_vessel_types: List[str] = ['Cargo Vessel']
        time_interval: str = 'H'

        # Call the function to be tested
        df: pd.DataFrame = count_unique_vessels_by_time(
            port_code, width, height, cargo_vessel_types, time_interval
        )

        # Assert that the returned object is a pandas DataFrame
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
