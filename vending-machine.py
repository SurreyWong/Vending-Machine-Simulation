import time
import os

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class ListItems:
    items = {
        "Water": 2.00,
        "Soda": 3.50,
        "Chips": 4.50,
        "Chocolate": 6.00,
        "Coffee": 7.50,
        "Juice": 8.50,
        "Sandwich": 9.00,
        "Energy Drink": 10.00,
    }

# Programmer 1: Amgad Elrashid
class VendingMachineNFA:
    """
    Implementation of a vending machine using Nondeterministic Finite Automaton (NFA) concepts.
    
    This class simulates a vending machine that:
    - Sells items with different prices
    - Accepts RM0.5 and RM1 coins
    - Dispenses items and returns change when needed
    - Tracks states based on accumulated money
    - Handles invalid inputs by simply prompting for valid input (NFA behavior)
    """
    
    def __init__(self):
        #Call the ListItems to show items and prices
        self.items = ListItems.items
        
        # Initialize menu items list 
        self.menu_items = []
        
        # Initialize the machine
        self.reset_machine()
    
    def reset_machine(self):
        """Reset the machine to its initial state."""
        self.selected_item = None
        self.selected_price = 0.0
        self.current_amount = 0.0
        self.current_state = "q0"  # Initial state
        
        clear_console()
        print("\nMachine reset to initial state.")
    
    def select_item(self, item_number):
        """Select an item from the vending machine by number."""
        try:
            # Convert to integer and adjust for 0-based indexing
            index = int(item_number) - 1
            
            # Check if the index is valid
            if 0 <= index < len(self.menu_items):
                item_name = self.menu_items[index]
                self.selected_item = item_name
                self.selected_price = self.items[item_name]
                
                print(f"\nSelected: {item_name} (RM{self.selected_price:.2f})")
                print(f"Current State: {self.current_state}")
                print(f"Insert RM0.5 or RM1 to continue")
                
                return True
            else:
                print(f"Error: Invalid selection. Please enter a number between 1 and {len(self.menu_items)}.")
                return False
                
        except ValueError:
            print("Error: Please enter a valid number.")
            return False
    
    def insert_money(self, value):
        """
        Insert money into the vending machine.
        
        The state transitions based on the input value (0.5 or 1) and the current
        accumulated amount. The state names represent the money accumulated.
        
        In NFA implementation, invalid inputs are handled by prompting for valid input.
        """
        if self.selected_item is None:
            print("Please select an item first.")
            return False
        
        # Check if the inserted value is valid (RM0.5 or RM1)
        # NFA behavior: Just prompt for valid input if invalid
        if value not in [0.5, 1]:
            print(f"Invalid value RM{value:.2f}. Only RM0.5 and RM1 are accepted.")
            print("Please insert either RM0.5 or RM1.")
            return False
        
        # Update current amount
        self.current_amount += value
        
        # Determine new state based on current state and input
        current_value = 0
        if self.current_state != "q0":
            # Extract the accumulated value from the state name
            # For example, q0.5 -> 0.5, q1 -> 1, q2.5 -> 2.5
            current_value = float(self.current_state[1:])
        
        # Calculate new state based on accumulated value
        new_value = current_value + value
        self.current_state = f"q{new_value}"
        
        print(f"Inserted: RM{value:.2f}")
        print(f"Total amount: RM{self.current_amount:.2f}")
        print(f"Required: RM{self.selected_price:.2f}")
        print(f"Current State: {self.current_state}")
        
        # Check if we've reached a final state (exact amount or over)
        if self.current_amount >= self.selected_price:
            self.dispense_item()
            return True
        
        return True
    
    def dispense_item(self):
        """
        Dispense the selected item and return change if needed.
        
        This occurs when reaching an accepting state (when the amount equals or exceeds the item price).
        """
        change = self.current_amount - self.selected_price
        
        print("\nAccepting state reached!")
        print(f"Dispensing: {self.selected_item}")
        
        # Simulate the dispensing process
        print("Processing...")
        time.sleep(1)
        print(f"{self.selected_item} has been dispensed!")
        time.sleep(1)

        
        # Return change if any
        if change > 0:
            print(f"Returning change: RM{change:.2f}")

        
        # Return to initial state
        self.reset_machine()
        
        # Prompt for a new item
        print("\nPlease select a new item.")
        return True
    
    def calculate_change(self, amount):
        """Calculate the change in terms of RM0.5 and RM1 denominations."""
        change_coins = {1.0: 0, 0.5: 0}
        
        # Calculate RM1 coins
        change_coins[1.0] = int(amount)
        remaining = amount - change_coins[1.0]
        
        # Calculate RM0.5 coins
        if remaining >= 0.5:
            change_coins[0.5] = 1
        
        return change_coins
    
    def display_menu(self):
        """Display the menu of available items with numbers for selection."""
        print("\n===== Vending Machine Menu =====")
        print("Available Items:")
        
        # Create a list of items for indexed access
        self.menu_items = list(self.items.keys())
        
        # Display items with numbers
        for i, item in enumerate(self.menu_items, 1):
            price = self.items[item]
            print(f"{i}. {item}: RM{price:.2f}")
            
        print("================================")

# Programmer 2: 
class VendingMachineDFA:
    """
    Implementation of a vending machine using Deterministic Finite Automaton (DFA) concepts.
    
    This class simulates a vending machine that:
    - Sells items with different prices
    - Accepts RM0.5 and RM1 coins
    - Dispenses items and returns change when needed
    - Tracks states based on accumulated money
    - Handles invalid inputs by resetting the machine (DFA behavior)
    """
    
    def __init__(self):
        #Call the ListItems to show items and prices
        self.items = ListItems.items
        
        # Initialize menu items list 
        self.menu_items = []
        
        # Initialize the machine
        self.reset_machine()
    
    def reset_machine(self):
        """Reset the machine to its initial state."""
        self.selected_item = None
        self.selected_price = 0.0
        self.current_amount = 0.0
        self.current_state = "q0"  # Initial state
        
        clear_console()
        print("\nMachine reset to initial state.")
    
    def select_item(self, item_number):
        """Select an item from the vending machine by number."""
        try:
            # Convert to integer and adjust for 0-based indexing
            idx = int(item_number) - 1
            
            # Check if the index is valid
            if 0 <= idx < len(self.menu_items):
                item_name = self.menu_items[idx]
                self.selected_item = item_name
                self.selected_price = self.items[item_name]
                
                print(f"\nSelected: {item_name} (RM{self.selected_price:.2f})")
                print(f"Current State: {self.current_state}")
                print(f"Insert RM0.5 or RM1 to continue")
                
                return True
            else:
                print(f"Error: Invalid selection. Please enter a number between 1 and {len(self.menu_items)}.")
                return False
                
        except ValueError:
            print("Error: Please enter a valid number.")
            return False
    
    def insert_money(self, value):
        """
        Insert money into the vending machine.
        
        The state transitions based on the input value (0.5 or 1) and the current
        accumulated amount. The state names represent the money accumulated.
        """
        if self.selected_item is None:
            print("Please select an item first.")
            return False
        
        # Update current amount
        self.current_amount += value
        
        # Determine new state based on current state and input
        current_value = 0
        if self.current_state != "q0":
            # Extract the accumulated value from the state name
            current_value = float(self.current_state[1:])
        
        # Calculate new state based on accumulated value
        new_value = current_value + value
        self.current_state = f"q{new_value}"
        
        print(f"Inserted: RM{value:.2f}")
        print(f"Total amount: RM{self.current_amount:.2f}")
        print(f"Required: RM{self.selected_price:.2f}")
        print(f"Current State: {self.current_state}")
        
        # Check if we've reached a final state (exact amount or over)
        if self.current_amount >= self.selected_price:
            self.dispense_item()
            return True
        
        return False  # Continue with money insertion
    
    def dispense_item(self):
        """
        Dispense the selected item and return change if needed.
        
        This occurs when reaching an accepting state (when the amount equals or exceeds the item price).
        """
        change = self.current_amount - self.selected_price
        
        print("\nAccepting state reached!")
        print(f"Dispensing: {self.selected_item}")
        
        # Simulate the dispensing process
        print("Processing...")
        time.sleep(1)
        print(f"{self.selected_item} has been dispensed!")
        time.sleep(1)
        
        # Return change if any
        if change > 0:
            print(f"Returning change: RM{change:.2f}")
        
        # Return to initial state
        self.reset_machine()
        
        # Prompt for a new item
        print("\nPlease select a new item.")
        return True
    
    def calculate_change(self, amount):
        """Calculate the change in terms of RM0.5 and RM1 denominations."""
        change_coins = {1.0: 0, 0.5: 0}
        
        # Calculate RM1 coins
        change_coins[1.0] = int(amount)
        remaining = amount - change_coins[1.0]
        
        # Calculate RM0.5 coins
        if remaining >= 0.5:
            change_coins[0.5] = 1
        
        return change_coins
    
    def display_menu(self):
        """Display the menu of available items with numbers for selection."""
        print("\n===== Vending Machine Menu =====")
        print("Available Items:")
        
        # Create a list of items for indexed access
        self.menu_items = list(self.items.keys())
        
        # Display items with numbers
        for i, item in enumerate(self.menu_items, 1):
            price = self.items[item]
            print(f"{i}. {item}: RM{price:.2f}")
            
        print("================================")

# Programmer 3:
def main():
    # Ask which implementation to use
    print("Which implementation would you like to use?")
    print("1. Deterministic Finite Automaton (DFA)")
    print("2. Nondeterministic Finite Automaton (NFA)")
    
    choice = input("Enter your choice (1 or 2): ")
    clear_console()

    # Create the appropriate machine based on user choice
    if choice == "1":
        machine = VendingMachineDFA()
        print("Using DFA implementation")
        print("Note: In DFA mode, invalid inputs will reset the machine.")
    elif choice == "2":
        machine = VendingMachineNFA()
        print("Using NFA implementation")
        print("Note: In NFA mode, invalid inputs will just prompt for valid input.")

    else:
        print("Invalid choice. Exiting.")
        return
    
    # Main interaction loop
    while True:
        machine.display_menu()
        
        # First, user must select an item
        print("\nCommands:")
        print("1. Select item")
        print("2. Exit")
        
        command = input("Enter command (1-2): ")

        if command == "1":
            item_number = input("Enter item number: ")
            clear_console()
            if not machine.select_item(item_number):
                continue
            
            # After selecting an item, user can insert money
            if isinstance(machine, VendingMachineDFA):
                # DFA money insertion (one chance only)
                try:
                    # Get the input value
                    value = float(input("\nInsert value (0.5 or 1): "))
                    
                    # Check if it's valid (DFA is strict)
                    if value not in [0.5, 1]:
                        print(f"Invalid value RM{value:.2f}. Only RM0.5 and RM1 are accepted.")
                        print("Resetting machine due to invalid input.")
                        time.sleep(1)
                        machine.reset_machine()
                        # No need for a loop here, just continue to the main menu
                    else:
                        # Process valid input
                        machine.insert_money(value)
                        # Continue inserting money if needed
                        while machine.selected_item is not None:  # Item not dispensed yet
                            value = float(input("\nInsert value (0.5 or 1): "))
                            if value not in [0.5, 1]:  # Invalid input
                                print(f"Invalid value RM{value:.2f}. Only RM0.5 and RM1 are accepted.")
                                print("Resetting machine due to invalid input.")
                                time.sleep(1)
                                machine.reset_machine()
                                break  # Exit to main menu
                            else:
                                result = machine.insert_money(value)
                                # If item is dispensed, machine.selected_item will be None
                
                except ValueError:
                    # For DFA, any non-numeric input is invalid
                    print("Invalid input. Resetting machine.")
                    time.sleep(1)
                    machine.reset_machine()
                    # Continue to main menu
            
            else:  # NFA implementation
                # More detailed menu for NFA
                while True:
                    print("\nCommands:")
                    print("1. Insert money")
                    print("2. Cancel and return to main menu")
                    
                    money_command = input("Enter command (1-2): ")
                    
                    if money_command == "1":
                        try:
                            value = float(input("Insert value (0.5 or 1): "))
                            clear_console()

                            result = machine.insert_money(value)
                            # If item is dispensed, break out of the money insertion loop
                            if result and machine.selected_item is None:
                                break
                        except ValueError:
                            clear_console()
                            print("Invalid input. Please enter a valid number.")
                    
                    elif money_command == "2":
                        print("Transaction cancelled.")
                        time.sleep(1)
                        machine.reset_machine()
                        break
                    
                    else:
                        clear_console()
                        print("Invalid command. Please try again.")
        
        elif command == "2":
            clear_console()
            print("Exiting. Thank you for using the vending machine!")
            break
        
        else:
            clear_console()
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
