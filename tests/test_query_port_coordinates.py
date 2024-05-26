# test_query_port_coordinates.py
from typing import Dict, Optional
import unittest
from unittest.mock import patch, MagicMock
from scripts.query_port_coordinates import get_port_coordinates

class TestQueryPortCoordinates(unittest.TestCase):
    @patch('scripts.query_port_coordinates.get_db_connection')
    def test_get_port_coordinates_success(self, mock_get_db_connection: MagicMock) -> None:
        """
        Test the get_port_coordinates function when a valid result is returned from the database.

        Args:
            mock_get_db_connection (MagicMock): Mock of the get_db_connection function.
        """
        # Mock database connection and cursor
        mock_connection: MagicMock = MagicMock()  # Mock database connection
        mock_cursor: MagicMock = MagicMock()  # Mock cursor object

        # Setup the mock connection to return the mock cursor
        mock_get_db_connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Define the expected row and column names
        expected_row: List[str] = ['Long Beach', 'USLGB', '33.75', '-118.2']  # Expected result row
        expected_column_names: List[str] = ['Main Port Name', 'UN/LOCODE', 'Latitude', 'Longitude']  # Expected column names

        # Set the cursor's fetchone and description mocks
        mock_cursor.fetchone.return_value = expected_row
        mock_cursor.description = [(col,) for col in expected_column_names]

        # Call the function
        result: Optional[Dict[str, str]] = get_port_coordinates('Long Beach')

        # Verify the result
        self.assertIsNotNone(result)  # Result should not be None
        self.assertEqual(result['Main Port Name'], 'Long Beach')  # Main Port Name should be 'Long Beach'
        self.assertEqual(result['UN/LOCODE'], 'USLGB')  # UN/LOCODE should be 'USLGB'
        self.assertEqual(result['Latitude'], '33.75')  # Latitude should be '33.75'
        self.assertEqual(result['Longitude'], '-118.2')  # Longitude should be '-118.2'

        # Verify the query execution
        expected_query: str = """
            SELECT "Main Port Name", "UN/LOCODE", "Latitude", "Longitude"
            FROM port_coordinates
            WHERE "Main Port Name" = %s;
            """  # Expected query
        expected_params: Tuple[str] = ('Long Beach',)  # Expected query parameters
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)  # Assert that the query was executed with the expected query and parameters.

    @patch('scripts.query_port_coordinates.get_db_connection')
    def test_get_port_coordinates_no_result(
            self,
            mock_get_db_connection: MagicMock) -> None:
        """
        Test the get_port_coordinates function when no result is returned from the database.

        Args:
            mock_get_db_connection (MagicMock): Mock of the get_db_connection function.

        Returns:
            None
        """
        # Mock database connection and cursor
        mock_connection: MagicMock = MagicMock()  # Mock database connection
        mock_cursor: MagicMock = MagicMock()  # Mock cursor object

        # Setup the mock connection to return the mock cursor
        mock_get_db_connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Define the expected column names but no row
        expected_column_names: List[str] = ['Main Port Name', 'UN/LOCODE', 'Latitude', 'Longitude']

        # Set the cursor's fetchone and description mocks
        mock_cursor.fetchone.return_value = None
        mock_cursor.description = [(col,) for col in expected_column_names]

        # Call the function
        result: Optional[Dict[str, str]] = get_port_coordinates('Unknown Port')

        # Verify the result
        self.assertIsNone(result)  # Result should be None

        # Verify the query execution
        expected_query: str = """
            SELECT "Main Port Name", "UN/LOCODE", "Latitude", "Longitude"
            FROM port_coordinates
            WHERE "Main Port Name" = %s;
        """
        expected_params: Tuple[str] = ('Unknown Port',)
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)

    @patch('scripts.query_port_coordinates.get_db_connection', return_value=None)
    def test_get_port_coordinates_connection_error(self, mock_get_db_connection: MagicMock) -> None:
        """
        Test the get_port_coordinates function when the database connection fails.

        This test checks if the function returns None when the database connection fails.

        Args:
            mock_get_db_connection (MagicMock): Mock of the get_db_connection function.

        Returns:
            None
        """
        # Call the function when the connection fails
        result: Optional[Dict[str, str]] = get_port_coordinates('Long Beach')

        # Verify the result
        self.assertIsNone(result)  # Result should be None when connection fails

if __name__ == '__main__':
    unittest.main()
