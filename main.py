import csv
import os

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


class CreateItem:
    def __init__(self, name, time, type):
        self.name = name.lower()  # Ensure the name is stored in lowercase
        self.time = time
        self.type = type
        self.attributes = [time, type]

    def NewPart(self, name, time, type):
        self.name = name.lower()  # Ensure the name is stored in lowercase
        self.attributes = [time, type]

    def FindByName(self, name):
        return self.name == name.lower()  # Case-insensitive comparison


def display_inventory(inventory):
    console = Console()
    table = Table(title="Inventory")

    table.add_column("Name", justify="left", style="bold")
    table.add_column("Type", justify="left")
    table.add_column("Time", justify="left")

    for item in inventory:
        table.add_row(item.name, item.type, item.time)

    console.print(table)


def find_item_by_name(name, inventory):
    for item in inventory:
        if item.FindByName(name):
            return item
    return None


def delete_items_by_names(names, inventory):
    names = [name.lower() for name in names]
    items_to_delete = [item for item in inventory if item.name in names]

    for item in items_to_delete:
        inventory.remove(item)

    return items_to_delete  # Return the list of deleted items


def save_inventory_to_csv(inventory, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Time", "Type"])
        for item in inventory:
            writer.writerow([item.name, item.time, item.type])


def load_inventory_from_csv(filename):
    inventory = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) == 3:
                    name, time, type = row
                    inventory.append(CreateItem(name, time, type))
    return inventory


def validate_name(name):

    return ',' not in name

def home_terminal():
    console = Console()
    inventory = []

    # Load existing inventory from CSV file
    csv_filename = "inventory.csv"
    inventory = load_inventory_from_csv(csv_filename)
    console.print("[bold red]Welcome to the Inventory System![/bold red]")

    while True:
        save_inventory_to_csv(inventory, csv_filename)
        console.print("[bold]type [/bold][?][bold] to get help[/bold]")
        console.print("[bold cyan]Please select an option:[/bold cyan]")
        console.print("[1] [cyan]View Full Inventory[/cyan]")
        console.print("[2] [cyan]Find Item by Name[/cyan]")
        console.print("[3] [cyan]Create New Item[/cyan]")
        console.print("[4] [cyan]Create Multiple Sets[/cyan]")
        console.print("[5] [cyan]Filter Inventory[/cyan]")
        console.print("[6] [cyan]Delete Items by Name[/cyan]")
        console.print("[7] [cyan]Edit Item Details[/cyan]")
        console.print("[8] [red]Exit[/red]")
        choice = Prompt.ask("[bold green]Enter your choice[/bold green]")

        if choice == "1":
            console.print("[bold green]Displaying full inventory:[/bold green]")
            display_inventory(inventory)
        elif choice == "2":
            search_name = Prompt.ask("[bold green]Enter the name of the item to find[/bold green]")
            search_result = find_item_by_name(search_name, inventory)

            if search_result:
                console.print(
                    f"[bold blue]Item found:[/bold blue] {search_result.name}, Type: {search_result.type}, Time: {search_result.time}")
            else:
                console.print(f"[bold red]Item not found:[/bold red] {search_name}")
        elif choice == "3":
            while True:
                name = Prompt.ask("[bold green]Enter the name of the new item[/bold green]").lower()
                if not validate_name(name):
                    console.print("[bold red]Invalid name. Names cannot contain commas. Please try again.[/bold red]")
                    continue
                # Check for existing item with the same name
                if find_item_by_name(name, inventory):
                    console.print(f"[bold red]An item with the name '{name}' already exists.[/bold red]")
                    continue
                time = Prompt.ask("[bold green]Enter the time of the new item[/bold green]")
                type = Prompt.ask("[bold green]Enter the type of the new item[/bold green]")

                new_item = CreateItem(name, time, type)
                inventory.append(new_item)
                console.print(
                    f"[bold green]Item created:[/bold green] {new_item.name}, Type: {new_item.type}, Time: {new_item.time}")
                break
        elif choice == "4":
            sets = int(Prompt.ask("[bold green]How many sets of items do you want to add[/bold green]"))
            for i in range(sets):
                while True:
                    item_input = Prompt.ask(f"[bold green]Set {i + 1}: Name, Date, Type[/bold green]")
                    items = [item.strip() for item in item_input.split(',')]
                    if len(items) == 3:
                        name, time, type = items
                        if not validate_name(name):
                            console.print("[bold red]Invalid name. Names cannot contain commas. Please try again.[/bold red]")
                            continue
                        # Check for existing item with the same name
                        if find_item_by_name(name.lower(), inventory):
                            console.print(f"[bold red]An item with the name '{name}' already exists.[/bold red]")
                            continue
                        new_item = CreateItem(name, time, type)
                        inventory.append(new_item)
                        console.print(
                            f"[bold green]Item added:[/bold green] {new_item.name}, Type: {new_item.type}, Time: {new_item.time}")
                        break
                    else:
                        console.print(
                            "[bold red]Invalid input. Please enter exactly three values separated by commas.[/bold red]")

        elif choice == "5":
            filtertype = Prompt.ask("[bold green]Filter category (time/type)[/bold green]")
            if filtertype.lower() == "time":
                filtervalue_date = Prompt.ask("[bold green]Filter to which year?[/bold green]")
                filtered_inventory = [item for item in inventory if item.time == filtervalue_date]
                display_inventory(filtered_inventory)
            elif filtertype.lower() == "type":
                filtervalue_type = Prompt.ask("[bold green]Filter to which type?[/bold green]")
                filtered_inventory = [item for item in inventory if item.type == filtervalue_type]
                display_inventory(filtered_inventory)
            else:
                console.print("[bold red]Invalid filter category.[/bold red]")

        elif choice == "6":
            names_input = Prompt.ask(
                "[bold red]Please enter the names of the items you wish to delete, separated by commas[/bold red]")
            names = [name.strip() for name in names_input.split(',')]

            # Display items to be deleted
            items_to_delete = [item for item in inventory if item.name in [name.lower() for name in names]]
            if items_to_delete:
                console.print(f"[bold red]The following items will be deleted:[/bold red]")
                for item in items_to_delete:
                    console.print(f"- Name: {item.name}, Type: {item.type}, Time: {item.time}")

                proceed = Prompt.ask(
                    "[bold red]Do you wish to proceed with deletion? (yes/no)[/bold red]").strip().lower()

                if proceed in ["yes", "y"]:
                    delete_count = delete_items_by_names(names, inventory)
                    console.print(f"[bold green]Deleted item(s)[/bold green]")
                else:
                    console.print("[bold yellow]Deletion cancelled.[/bold yellow]")
            else:
                console.print(f"[bold red]No items found with the provided names[/bold red]")

        elif choice == "7":
            edit_target = Prompt.ask(
                "[bold green]Please enter the name of the item you wish to edit[/bold green]").lower()
            item_to_edit = find_item_by_name(edit_target, inventory)

            if item_to_edit:
                console.print(
                    f"[bold green]Item found:[/bold green] Name: {item_to_edit.name}, Type: {item_to_edit.type}, Time: {item_to_edit.time}")

                while True:
                    new_name = Prompt.ask("[bold green]Enter the new name for the item[/bold green]").lower()
                    if not validate_name(new_name):
                        console.print("[bold red]Invalid name. Names cannot contain commas. Please try again.[/bold red]")
                        continue
                    # Check for duplicate names
                    if find_item_by_name(new_name, inventory):
                        console.print(f"[bold red]An item with the name '{new_name}' already exists.[/bold red]")
                        continue

                    new_time = Prompt.ask("[bold green]Enter the new time for the item[/bold green]")
                    new_type = Prompt.ask("[bold green]Enter the new type for the item[/bold green]")

                    # Update the item using NewPart
                    item_to_edit.NewPart(new_name, new_time, new_type)
                    console.print(
                        f"[bold green]Item updated:[/bold green] Name: {item_to_edit.name}, Type: {item_to_edit.type}, Time: {item_to_edit.time}")
                    break
            else:
                console.print(f"[bold red]Item not found:[/bold red] {edit_target}")
        elif choice == "?":
            console.print(
                "[bold blue]Within the inventory there are items with unique names, dates and types attached which are all stored in a csv file.[/bold blue]\n"
                "type a number 1 through to 8 to select that option\n"
                "1 - display all current items with inventory\n"
                "2 - Enter a name for a item and it will tell you its attributes\n"
                "3 - Enter Name, time and type to add an item to the inventory and consequentially the csv file\n"
                "4 - Enter a integer and you will be prompted to chose a name, time and type for that many items "
                "which will be appended to the inventory\n"
                "5 - you will be prompted to enter a column name and label and it will display all items fitting that "
                "description\n"
                "6 - Enter a list of names seperated by commas and it will delete those items from all inventory "
                "locations \n"
                "7 - you will be prompted to enter the name of an existing item within the inventory and then you can "
                "change its attributes. Press enter to retain original value\n"
                "8 - exits the program and loads any changes to csv to inventory and vice versa\n"
            )

        elif choice == "8":
            # Save the inventory to a CSV file before exiting
            save_inventory_to_csv(inventory, csv_filename)
            console.print("[bold red]Exiting...[/bold red]")
            break
        else:
            console.print("[bold red]Invalid choice, type [?] to see help.[/bold red]")

if __name__ == "__main__":
    home_terminal()

