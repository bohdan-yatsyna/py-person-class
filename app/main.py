class Person:

    people: [dict[str]] = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return result_list
