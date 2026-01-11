# Sanskar Mali
#This is my first Python project! 
# It's a program that stores and displays personal information.




print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()


name = "Sanskar Mali"
age = 21
city = "Pune"
hobby = "Sleeping"


print("Please tell me about yourself:")
print("-" * 30)

favoriteFood = input("What's your favorite food? ")
while favoriteFood == "":
    print("Please enter a valid food!")
    favoriteFood = input("What's your favorite food? ")

favorite_color = input("What's your favorite color? ")
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")


age_in_months = age * 12


print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favoriteFood}")
print(f"Favorite Color: {favorite_color}")
print()


print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)
