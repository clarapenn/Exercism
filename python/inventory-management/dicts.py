"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    dictionary = {}
    for item in items:
        if item in dictionary:
            continue
        amount = items.count(item)
        dictionary[item] = amount
    return dictionary


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        # if item in inventory and inventory[item] == 0:
        #     continue
        # elif inventory[item] >= 1:
        #     inventory[item] = inventory[item] - 1
        if inventory[item] >= 1:
            inventory[item] = inventory[item] - 1

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)

    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    # new_list = []
    new_inventory = list(inventory.items())

    # for entry in new_inventory:
    #     if entry[1] == 0:
    #         continue
    #     else:
    #         new_list.append(entry)

    # return new_list

    new_list = [entry for entry in new_inventory if entry[1] != 0]

    return new_list
