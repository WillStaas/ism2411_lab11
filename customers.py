#SA Questions
#1 # 1. I would use .get() when I am not sure if a key exists in a dictionary because it allows me to provide a default value instead of getting an error.
#2 Building a summary dictionary with a loop reminds me of using SUMIF or Pivot Tables in Excel to organize and total data based on categories. Python can be more useful for large datasets because it can process and organize large amounts of information automatically without  having to manually create formulas or update tables
# EXERCISE 1 - Create and access a dictionary

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1250
}


print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print(customer)



# EXERCISE 2 - Update and add


# Add a phone field
customer["phone"] = "555-123-4567"
print(customer)

# Update the tier to platinum
customer["tier"] = "platinum"
print(customer)

# Delete the email field
del customer["email"]
print(customer)



# EXERCISE 3 - Safe lookup

# Use get() to look up the deleted email
email = customer.get("email", "no email on file")
print(email)


try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")



# EXERCISE 4 - Iterate


# Use .items() to print each key and value
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only returns the keys
for key in customer:
    print(key)



# EXERCISE 5 - Lookup table


tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}


tier = customer["tier"]
discount = tier_discounts.get(tier, 0)


purchase_price = 200
final_price = purchase_price * (1 - discount)

print("Tier:", tier)
print("Discount rate:", discount * 100, "%")
print("Final price: $", round(final_price, 2))



# EXERCISE 6 - List of dictionaries


dict1 = {
    "name": "Alice",
    "tier": "platinum"
}

dict2 = {
    "name": "Bob",
    "tier": "gold"
}

dict3 = {
    "name": "Charlie",
    "tier": "silver"
}

customers = [dict1, dict2, dict3]


for customer_info in customers:
    name = customer_info["name"]
    tier = customer_info["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{name}: {tier} - "
        f"Discount: ${discount_amount:.2f}"
    )



# EXERCISE 7 - Nested catalog


catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}


for product, details in catalog.items():
    if details["stock"] < 20:
        print(
            f"LOW STOCK: {product} - "
            f"Only {details['stock']} remaining"
        )



# EXERCISE 8 - Sales by region


transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]


sales_summary = {}


for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = (
        sales_summary.get(region, 0) + amount
    )


for region in sorted(sales_summary):
    print(f"{region}: {sales_summary[region]}")
