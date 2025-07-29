from functions import load_facts, save_facts, search_animal, add_fact, list_animals

def main():
    facts = load_facts()
    while True:
        print("\n🐾 Animal Fun Facts Encyclopedia 🦁")
        print("1. Search for an animal fact")
        print("2. Add a new animal and fact")
        print("3. List all animals")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            animal = input("Enter animal name: ").strip()
            fact = search_animal(facts, animal)
            if fact:
                print(f"{animal.title()}: {fact}")
            else:
                print("Animal not found.")
        elif choice == "2":
            animal = input("Enter new animal name: ").strip()
            fact = input("Enter a fun fact: ").strip()
            add_fact(facts, animal, fact)
            save_facts(facts)
            print(f"Added: {animal.title()} - {fact}")
        elif choice == "3":
            animals = list_animals(facts)
            if animals:
                print("Animals in Encyclopedia:")
                for animal in animals:
                    print(f"- {animal}")
            else:
                print("No animals found.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()