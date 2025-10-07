import yaml
import os

def load_agent_router_config(config_path: str) -> dict:
    """Loads the agent router configuration from a YAML file.

    Args:
        config_path: The path to the agent router YAML configuration file.

    Returns:
        A dictionary containing the agent router configuration, or an empty
        dictionary if the file is not found.
    """
    if not os.path.exists(config_path):
        print(f"Error: Agent router config not found at {config_path}")
        return {}
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def handle_command(command: str, agent_router: dict):
    """Simulates handling a command by routing it to the appropriate agent.

    This function checks the command against a list of keywords defined for each
    agent in the router configuration. If a match is found, it prints routing
    information. Otherwise, it defaults to general system processing.

    Args:
        command: The command string to be processed.
        agent_router: A dictionary containing agent configurations, where
                             each agent has keywords and a role description.
    """
    print(f"CLI received command: '{command}'")
    routed = False
    for agent_name, config in agent_router.get('agents', {}).items():
        if any(keyword in command.lower() for keyword in config.get('keywords', [])):
            print(f"Routing command to {agent_name} ({config.get('role', 'unknown role')}):")
            print(f"  - Input: '{command}'")
            print(f"  - Expected action: {config.get('action_description', 'processing...')}")
            routed = True
            break
    if not routed:
        print("No specific agent found for this command. Defaulting to general system processing.")