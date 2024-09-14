
# ACESS - Inventory Management System

ACESS is a Python-based inventory management system designed for handling various operations such as adding, deleting, editing, and filtering inventory items. Data is persistently stored and retrieved using CSV files.

## Features

- **View Inventory**: Display all items in the inventory.
- **Add Items**: Add individual or multiple items.
- **Search Items**: Find items by name.
- **Edit Items**: Update item details.
- **Delete Items**: Remove items by name.
- **Filter Items**: Filter inventory based on type or time.
- **CSV Storage**: Inventory is saved in a CSV file for persistence.



## Getting Started

### Prerequisites

- Python 3.x


### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/BowLuckie/ACESS.git
    cd ACESS
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

### Running Tests

Run the test cases using `pytest`:
```bash
cd TESTS
pytest TEST_CSV.py
```

## Usage

Interact with the inventory system via the command-line interface (CLI). The following operations are supported:

- **View Full Inventory**: Display all items in the inventory.
- **Find Item by Name**: Search for an item using its name.
- **Create New Item**: Add a new item by specifying its name, time, and type.
- **Create Multiple Sets**: Add multiple items at once.
- **Filter Inventory**: Filter items by time or type.
- **Delete Items by Name**: Remove items by name.
- **Edit Item Details**: Modify an existing item's name, time, or type.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
 issues or suggestions, open an issue on the GitHub repository or contact the project maintainer.
