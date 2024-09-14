Here's a structured and formatted `README.md` for your project:

```md
# ACESS - Inventory Management System

ACESS is a Python-based inventory management system designed to handle various inventory operations such as adding, deleting, editing, and filtering items. The system stores and loads data from a CSV file to maintain persistent inventory records.

## Features

- **View Inventory**: Display all items in the inventory with their respective attributes.
- **Add Items**: Add new items, either individually or in sets.
- **Search Items**: Find items by their name.
- **Edit Items**: Modify existing item details.
- **Delete Items**: Remove items from the inventory by name.
- **Filter Items**: Filter items based on attributes like type or time.
- **CSV Storage**: Persistent inventory storage using CSV files.

## Project Structure

```
ACESS/
    TESTS/
        .pytest_cache/
        inventory.csv (test data)
        inventroyTest.csv (test data)
        TEST_CSV.py (test cases)
    venv/ (virtual environment)
    inventory.csv (actual inventory data)
    main.py (main application)
    requirements.txt (dependencies)
```

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment setup (optional but recommended)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/BowLuckie/ACESS.git
    cd ACESS
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

### Running Tests

To run the tests for your project:
```bash
cd TESTS
pytest TEST_CSV.py
```

## Usage

Once the application is running, you can interact with the inventory system through a command-line interface (CLI). Follow the prompts to perform various inventory operations.

### Options
- **View Full Inventory**: Displays the entire inventory with names, types, and time attributes.
- **Find Item by Name**: Search for an item using its name.
- **Create New Item**: Add a new item to the inventory by specifying its name, time, and type.
- **Create Multiple Sets**: Add multiple items at once.
- **Filter Inventory**: Filter items by specific attributes like time or type.
- **Delete Items by Name**: Remove items from the inventory by providing their names.
- **Edit Item Details**: Modify the name, time, or type of an existing item.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
