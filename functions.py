def load_facts(filename="animaldata.txt"):
    facts = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                if ":" in line:
                    animal, fact = line.strip().split(":", 1)
                    facts[animal.lower()] = fact
    except FileNotFoundError:
        pass  # return empty dict if file doesn't exist yet
    return facts

def save_facts(facts, filename="animaldata.txt"):
    with open(filename, "w") as file:
        for animal, fact in facts.items():
            file.write(f"{animal}:{fact}\n")

def search_animal(facts, animal):
    return facts.get(animal.lower())

def add_fact(facts, animal, fact):
    facts[animal.lower()] = fact

def list_animals(facts):
    return [animal.title() for animal in facts.keys()]

