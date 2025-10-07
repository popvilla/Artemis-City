import unittest
from unittest.mock import patch
import io
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from artemis_city.simulation import simulate_mail_delivery

class TestSimulation(unittest.TestCase):

    @patch('random.random', return_value=0.5)  # Ensure random check passes
    @patch('time.sleep', return_value=None)     # Disable sleep to speed up test
    def test_simulate_mail_delivery_success(self, mock_sleep, mock_random):
        """Tests the mail delivery simulation for a successful scenario."""
        sender = "TestSender"
        recipient = "TestRecipient"
        message = "Test message"

        # Capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        result = simulate_mail_delivery(sender, recipient, message)

        # Restore stdout
        sys.stdout = sys.__stdout__

        self.assertTrue(result)
        output = captured_output.getvalue()
        self.assertIn("Transfer successful", output)
        self.assertIn(sender, output)
        self.assertIn(recipient, output)

    @patch('random.random', return_value=0.05) # Ensure random check fails (less than 0.1)
    @patch('time.sleep', return_value=None)    # Disable sleep
    def test_simulate_mail_delivery_failure(self, mock_sleep, mock_random):
        """Tests the mail delivery simulation for a failure scenario."""
        sender = "TestSender"
        recipient = "TestRecipient"
        message = "Test message"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        result = simulate_mail_delivery(sender, recipient, message)

        sys.stdout = sys.__stdout__

        self.assertFalse(result)
        output = captured_output.getvalue()
        self.assertIn("Transfer failed", output)

if __name__ == "__main__":
    unittest.main()