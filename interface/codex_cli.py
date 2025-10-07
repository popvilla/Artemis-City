import argparse
import os
import sys

# Add the src directory to the Python path to allow for package imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from artemis_city.cli import handle_command, load_agent_router_config

def main():
    """The main entry point for the Agentic Codex CLI.

    This function initializes the command-line interface, parses arguments, and
    enters a loop to accept user commands. It loads the agent router
    configuration and uses it to handle commands either from an initial
    argument or from interactive input.
    """
    parser = argparse.ArgumentParser(description="Agentic Codex CLI Interface")
    parser.add_argument(
        "command",
        nargs="?",
        help="The command to send to the Codex (e.g., 'status', 'ask artemis')"
    )
    # Add an argument for custom config path
    parser.add_argument(
        "--config",
        default=os.path.join(os.path.dirname(__file__), 'agent_router.yaml'),
        help="Path to the agent router YAML configuration file."
    )
    args = parser.parse_args()

    print("--- Agentic Codex CLI ---")
    print("Type 'exit' or 'quit' to close.")

    # Load agent router configuration
    agent_router_config = load_agent_router_config(args.config)
    if not agent_router_config:
        print("Could not load agent configuration. Exiting.")
        return

    if args.command:
        handle_command(args.command, agent_router_config)
    else:
        # Interactive mode
        while True:
            try:
                user_input = input("codex> ").strip()
                if user_input.lower() in ["exit", "quit"]:
                    print("Exiting Codex CLI. Goodbye!")
                    break
                if not user_input:
                    continue
                handle_command(user_input, agent_router_config)
            except KeyboardInterrupt:
                print("\nExiting Codex CLI. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()