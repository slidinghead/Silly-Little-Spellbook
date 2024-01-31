import pip._vendor.requests


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


def main():
    while True:
        print("Commands:")
        print("1 - List all spells")
        print("2 - Get spell by name")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
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
        elif choice == "2":
            spell_name = input("Enter the spell name: ").lower()
            spell_info(spell_name)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
