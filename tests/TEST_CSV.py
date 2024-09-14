import unittest
import tempfile
import os
from main import CreateItem, find_item_by_name, save_inventory_to_csv, load_inventory_from_csv

class InventoryTestCase(unittest.TestCase):

    def setUp(self):
        # This method runs before every test
        self.inventory = []
        self.item1 = CreateItem("book", "2023", "media")
        self.item2 = CreateItem("album", "2021", "music")
        self.inventory.append(self.item1)
        self.inventory.append(self.item2)

        # Create a temporary file for testing CSV storage
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        self.csv_file_path = self.temp_file.name
        self.temp_file.close()  # Close the file to use it in our functions

    def tearDown(self):
        # Clean up the temporary file after each test
        if os.path.exists(self.csv_file_path):
            os.remove(self.csv_file_path)

    def test_create_item(self):
        # Test if the item is created with the correct attributes
        item = CreateItem("movie", "2022", "media")
        self.assertEqual(item.name, "movie")
        self.assertEqual(item.time, "2022")
        self.assertEqual(item.type, "media")

    def test_find_item_by_name(self):
        # Test if we can find an item by its name
        found_item = find_item_by_name("book", self.inventory)
        self.assertIsNotNone(found_item)
        self.assertEqual(found_item.name, "book")

    def test_find_item_by_name_case_insensitive(self):
        # Test if the search is case-insensitive
        found_item = find_item_by_name("ALBUM", self.inventory)
        self.assertIsNotNone(found_item)
        self.assertEqual(found_item.name, "album")

    def test_save_inventory_to_csv(self):
        # Test saving inventory to the temporary CSV file
        save_inventory_to_csv(self.inventory)

        # Save the inventory to the temporary file
        save_inventory_to_csv(self.inventory)

        # Load the inventory from the temporary file
        saved_inventory = load_inventory_from_csv()

        # Check if the inventory saved correctly
        self.assertEqual(len(saved_inventory), 2)
        self.assertEqual(saved_inventory[0].name, "book")
        self.assertEqual(saved_inventory[1].name, "album")

    def test_load_inventory_from_csv(self):
        # Test loading inventory from the temporary CSV file
        save_inventory_to_csv(self.inventory)  # Save first to create the file
        loaded_inventory = load_inventory_from_csv()

        # Check if inventory is loaded correctly
        self.assertEqual(len(loaded_inventory), 2)
        self.assertEqual(loaded_inventory[0].name, "book")
        self.assertEqual(loaded_inventory[1].name, "album")

if __name__ == '__main__':
    unittest.main()
