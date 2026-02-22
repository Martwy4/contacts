class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)
    

class BusinessContact(BaseContact):
    def __init__(self, name, surname, phone, email, position, company, business_phone):
        super().__init__(name, surname, phone, email)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        print(
            f"Wybieram numer {self.business_phone} "
            f"i dzwonię do {self.name} {self.surname}"
        )

from faker import Faker
import random

fake = Faker("pl_PL")


def create_contacts(contact_type, quantity):
    contacts = []

    for _ in range(quantity):
        name = fake.first_name()
        surname = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()

        if contact_type == "base":
            contacts.append(
                BaseContact(name, surname, phone, email)
            )

        elif contact_type == "business":
            position = fake.job()
            company = fake.company()
            business_phone = fake.phone_number()

            contacts.append(
                BusinessContact(
                    name,
                    surname,
                    phone,
                    email,
                    position,
                    company,
                    business_phone
                )
            )

    return contacts

base_contacts = create_contacts("base", 2)
business_contacts = create_contacts("business", 2)
for c in base_contacts + business_contacts:
    c.contact()
    print("Długość imienia i nazwiska:", c.label_length)
