import sys
import os

# Add the src directory to the Python path to allow for package imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from artemis_city.simulation import simulate_mail_delivery

def main():
    """Runs the mail delivery simulation with predefined scenarios."""
    print("Running Mail Delivery Simulation (Sandbox City - Post Office)")
    simulate_mail_delivery("Agent_A", "Agent_B", "Urgent operational update.")
    simulate_mail_delivery("Human_User", "Artemis", "Query about recent policy change.")

if __name__ == "__main__":
    main()