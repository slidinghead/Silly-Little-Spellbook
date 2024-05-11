import pip._vendor.requests
import os

import sys

import certifi

os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(sys.argv[0]), certifi.where())

def spell_list():
    print("\nList of Spells:")
    for i in range(10):
        if i == 0:
            print("Cantrips:")
        else:
            print("level " + str(i) + " spells:")
        url = "https://www.dnd5eapi.co/api/spells?level=" + str(i)
        headers = {"Accept": "application/json"}

        response = pip._vendor.requests.get(url, headers=headers)
        if response.status_code == 200:
            spells_data = response.json()
            spells = spells_data["results"]
            for spell in spells:
                print(f"    {spell['name']}")

def spell_info(spell):
    spell = spell.replace(' ', '-').lower()
    url = "https://www.dnd5eapi.co/api/spells/" + spell
    headers = {"Accept": "application/json"}

    response = pip._vendor.requests.get(url, headers=headers)
    if response.status_code == 200:
        spell_data = response.json()
        print(f"\n\n{spell_data['name']}")
        if spell_data['level'] == 0:
            print(f"{spell_data['school']['name']} Cantrip", end="")
        else:
            print(f"Level {spell_data['level']} {spell_data['school']['name']}", end="")
        if spell_data['ritual']:
            print(f" Ritual")
        else:
            print("")
        print(f"Components: {spell_data['components']}")
        if 'material' in spell_data:
            print(f"Material Components: {spell_data['material']}")
        print(f"Range: {spell_data['range']}")
        if 'area_of_effect' in spell_data:
            print(f"AOE: {spell_data['area_of_effect']['size']} foot {spell_data['area_of_effect']['type']}")
        if spell_data['concentration']:
            print(f"Duration: {spell_data['duration']} - Concentration")
        else:
            print(f"Duration: {spell_data['duration']}")
        print(f"\nDescription: \n{spell_data['desc'][0]}\n")
        print(f"Classes: ", end="")
        first = True
        for classes in spell_data['classes']:
            if first:
                print(f"{classes['name']}", end="")
                first = False
            else:
                print(f", {classes['name']}", end="")
        print(f"\nSubclasses: ", end="")
        first = True
        for classes in spell_data['subclasses']:
            if first:
                print(f"{classes['name']}", end="")
                first = False
            else:
                print(f", {classes['name']}", end="")
        print("\n\n")
    else:
        print(f"\n\nSpell not found, Sorry! :(\n\n")

def class_list(class_name):
    class_name = class_name.replace(' ', '-').lower()
    print("\nList of " + str(class_name) + " Spells:")
    url = "https://www.dnd5eapi.co/api/classes/" + str(class_name) + "/spells"
    headers = {"Accept": "application/json"}

    response = pip._vendor.requests.get(url, headers=headers)
    if response.status_code == 200:
        spells_data = response.json()
        spells = spells_data["results"]
        for spell in spells:
            print(f"    {spell['name']}")


def main():
    while True:
        print("Commands:")
        print("1 - List all spells")
        print("2 - Get spell by name")
        print("3 - List spells by class")
        print("4 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            spell_list()
        elif choice == "2":
            spell_name = input("Enter the spell name: ").lower()
            spell_info(spell_name)
        elif choice == "3":
            class_name = input("Enter the class name: ").lower()
            class_list(class_name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
