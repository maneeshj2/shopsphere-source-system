import random
from datetime import date, timedelta

import requests

API_URL = "http://127.0.0.1:8000/customers"

first_names = [
    "Rahul", "Priya", "Amit", "Neha", "Arjun",
    "Sneha", "Vikram", "Ananya", "Rohit", "Pooja", "Divya",
    "Kushagra", "Arushi", "Deepa", "Priyanka", "Ashutosh",
    "Narendra", "Abhishek", "Aditya", "Anshul", "Ankit"

]

last_names = [
    "Sharma", "Verma", "Singh", "Gupta", "Joshi",
    "Kapoor", "Jain", "Mehta", "Agarwal", "Bansal",
    "Khanna", "Oberoi", "Deshmukh", "Kumar", "Jaiswal"
]


def random_dob():
    start = date(1985, 1, 1)
    end = date(2005, 12, 31)

    days = (end - start).days

    return start + timedelta(days=random.randint(0, days))


for i in range(1, 100):

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    email = f"{first_name.lower()}.{last_name.lower()}{i}@gmail.com"

    customer = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": f"98{random.randint(10000000, 99999999)}",
        "password": "Password@123",
        "date_of_birth": random_dob().isoformat()
    }

    print(f"Creating customer {i}...")

    response = requests.post(
    API_URL,
    json=customer,
)

print("=" * 50)
print(f"Customer #{i}")
print(f"Email       : {customer['email']}")
print(f"Status Code : {response.status_code}")
print(f"Response    : {response.text}")