import pip._vendor.requests


def spell_info(spell):
    url = "https://www.dnd5eapi.co/api/spells/" + spell
    headers = {"Accept": "application/json"}

    response = pip._vendor.requests.get(url, headers=headers)
    if response.status_code == 200:
        spell_data = response.json()
        print(f"Range: {spell_data['range']}")


def main():
    while True:
        print("Commands:")
        print("1 - List all spells")
        print("2 - Get spell description by name")
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
