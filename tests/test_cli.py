import unittest
from unittest.mock import patch
import io
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from artemis_city.cli import handle_command

class TestCli(unittest.TestCase):

    def setUp(self):
        """Set up a mock agent router for testing."""
        self.agent_router = {
            'agents': {
                'artemis': {
                    'role': 'Mayor protocol, governance',
                    'keywords': ['artemis', 'governance'],
                    'action_description': 'Initiating governance review.'
                },
                'pack_rat': {
                    'role': 'Courier role, safe transfer',
                    'keywords': ['transfer', 'send'],
                    'action_description': 'Preparing secure data transfer.'
                }
            }
        }

    def test_handle_command_routed_to_artemis(self):
        """Tests that a command with a keyword is routed to the correct agent."""
        command = "ask artemis about policy"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        handle_command(command, self.agent_router)

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Routing command to artemis", output)
        self.assertIn("Initiating governance review", output)

    def test_handle_command_default_routing(self):
        """Tests that a command with no keyword uses default routing."""
        command = "what is the weather?"

        captured_output = io.StringIO()
        sys.stdout = captured_output

        handle_command(command, self.agent_router)

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("No specific agent found", output)
        self.assertIn("Defaulting to general system processing", output)

if __name__ == "__main__":
    unittest.main()