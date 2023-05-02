import requests
import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Endpoint URLs
base_url = "http://localhost:8080"
welcome_url = f"{base_url}/"
contact_url = f"{base_url}/contact"
submit_url = f"{base_url}/submit"
users_url = f"{base_url}/users"

# Define the database connection
engine = create_engine("sqlite:///users.db", echo=True)

# Define the User model
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)


# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Connect to the database and create a session
Session = sessionmaker(bind=engine)
session = Session()

# Read the users from the JSON file and add them to the database
with open("users.json") as f:
    users = json.load(f)["users"]
    for user in users:
        session.add(User(name=user["name"], email=user["email"], phone=user["phone"]))
    session.commit()

# Command-line interface
while True:
    query = input(
        "Enter a user's name to display their information, or type 'quit' to exit: "
    )
    if query == "quit":
        break
    user = session.query(User).filter_by(name=query).first()
    if user:
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print(f"Phone: {user.phone}")
    else:
        print(f"No user found with name '{query}'.")

# Disconnect from the database
session.close()
