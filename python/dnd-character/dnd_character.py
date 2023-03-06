import random


# class Character:
#     def __init__(
#         self,
#         constitution,
#         strength,
#         dexterity,
#         intelligence,
#         wisdom,
#         charisma,
#     ):

#         self.strength = strength
#         self.charisma = charisma
#         self.dexterity = dexterity
#         self.intelligence = intelligence
#         self.constitution = constitution
#         self.wisdom = wisdom

#         self.constitution_modifier = (
#             self.constitution - 10
#         ) // 2  # integer division rounds down
#         self.hitpoints = 10 + self.constitution_modifier


# def generate_characters(num_to_make=3):

#     characters = []

#     for _ in range(num_to_make):
#         strength = roll_dice(4)
#         charisma = roll_dice(4)
#         dexterity = roll_dice(4)
#         intelligence = roll_dice(4)
#         wisdom = roll_dice(4)
#         constitution = roll_dice(4)

#         new_char = Character(
#             constitution=constitution,
#             strength=strength,
#             dexterity=dexterity,
#             intelligence=intelligence,
#             wisdom=wisdom,
#             charisma=charisma,
#         )

#         characters.append(new_char)

#     return characters


# def roll_dice(num_dice=4):

#     """Return a list of four integers. Each integer in the returned
#     list is a random number between 1 and 6, inclusive.

#     """

#     roll_results = []

#     for _ in range(num_dice):
#         roll = random.randint(1, 6)
#         roll_results.append(roll)

#     index_smallest_result = roll_results.index(min(roll_results))

#     roll_results.pop(index_smallest_result)
#     three_remaining = roll_results

#     character_feature_number = sum(three_remaining)
#     return character_feature_number


# print(roll_dice())


def modifier(constitution):

    constitution_modifier = (constitution - 10) // 2  # integer division rounds down

    return constitution_modifier


class Character:
    def __init__(self):

        self.strength = self.ability()
        self.charisma = self.ability()
        self.dexterity = self.ability()
        self.intelligence = self.ability()
        self.constitution = self.ability()
        self.wisdom = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self, num_dice=4):

        """Return a list of four integers. Each integer in the returned
        list is a random number between 1 and 6, inclusive.
        """

        roll_results = []

        for _ in range(num_dice):
            roll = random.randint(1, 6)
            roll_results.append(roll)

        index_smallest_result = roll_results.index(min(roll_results))

        roll_results.pop(index_smallest_result)
        three_remaining = roll_results

        character_feature_number = sum(three_remaining)
        return character_feature_number
