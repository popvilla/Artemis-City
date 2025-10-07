# Artemis City

## Overview

Artemis City is an architectural framework designed to align agentic reasoning with transparent, accountable action across distributed intelligence systems—both human and machine. This project provides a foundational structure for defining agents, managing memory, establishing interfaces, and simulating environments.

The repository contains a command-line interface (CLI) to interact with the system's agent router and a standalone simulation for mail delivery within the "Sandbox City" environment. The core logic is housed in the `src/artemis_city` package, with executable scripts in the `interface` and `sandbox_city` directories.

## Prerequisites

Before you begin, ensure you have the following software installed on your system:
- **Python 3.8 or higher**
- **pip** (Python's package installer)
- **Make** (for using the Makefile)

## Setup and Installation

1.  **Clone the Repository**:
    If this were a Git repository, you would clone it. For now, ensure all project files are located in a single directory.

2.  **Navigate to the Project Directory**:
    Open your terminal and change to the directory containing the project files.

3.  **Create and Activate a Virtual Environment** (Recommended):
    ```bash
    # Create the virtual environment
    python3 -m venv venv

    # Activate on macOS and Linux
    source venv/bin/activate

    # Activate on Windows
    .\venv\Scripts\activate
    ```

4.  **Install Dependencies**:
    Use the `Makefile` to install the required Python packages.
    ```bash
    make install
    ```

## Usage

Artemis City can be operated through its command-line interface or by running individual simulations using `make` commands.

### Running the Agentic Codex CLI

The main entry point is the Agentic Codex CLI, which simulates routing commands to different agents based on keywords.

1.  **Launch the CLI in Interactive Mode**:
    ```bash
    make run-cli
    ```
    You will be greeted with a `codex>` prompt. Type commands and press Enter. To exit, type `exit` or `quit`.

2.  **Run the CLI with a Command**:
    Pass a command directly.
    ```bash
    python interface/codex_cli.py "check mail for delivery"
    ```

3.  **Using a Custom Configuration File**:
    The CLI uses `interface/agent_router.yaml` by default, but you can specify a different configuration file using the `--config` flag.
    ```bash
    python interface/codex_cli.py --config /path/to/your/custom_router.yaml
    ```

### Running the Mail Delivery Simulation

The `mail_delivery_sim.py` script simulates a secure mail delivery process.

-   **Execute the script using the Makefile**:
    ```bash
    make run-simulation
    ```
    The script will run two predefined simulations and print the results.