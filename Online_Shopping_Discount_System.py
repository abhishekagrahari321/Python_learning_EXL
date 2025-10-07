# Expanded & Interactive Case Study: Online Shopping Discount System

print("Welcome to the Online Shopping Discount System!\n")

# Step 1: Add multiple items
items = []
add_more = "yes"
while add_more.lower() == "yes":
    name = input("Enter item name: ")
    price = float(input(f"Enter price for {name} (₹): "))
    quantity = int(input(f"Enter quantity of {name}: "))
    items.append({"name": name, "price": price, "quantity": quantity})
    add_more = input("Add another item? (yes/no): ")

# Step 2: Calculate total cart value
cart_value = sum(item["price"] * item["quantity"] for item in items)
print(f"\nTotal cart value: ₹{cart_value:.2f}")

# Step 3: Membership status
membership = input("Enter your membership status (Premium/Regular): ").strip().lower()

# Step 4: Promo code
promo_code = input("Enter promo code (if any, or press Enter to skip): ").strip().lower()

# Step 5: Discount calculation based on rules
discount = 0.0
discount_desc = ""

if cart_value > 5000:
    if membership == "premium":
        discount = 0.20
        discount_desc = "20% Premium Member Discount"
    elif membership == "regular":
        discount = 0.10
        discount_desc = "10% Regular Member Discount"
    else:
        discount_desc = "No membership discount"
elif 2000 < cart_value <= 5000:
    discount = 0.05
    discount_desc = "5% Standard Discount"
else:
    discount_desc = "No discount"

# Step 6: Promo code logic (example codes)
promo_discount = 0.0
promo_desc = ""
if promo_code:
    if promo_code == "save50" and cart_value >= 1000:
        promo_discount = 50
        promo_desc = "₹50 off with SAVE50"
    elif promo_code == "festive10":
        promo_discount = 0.10 * cart_value
        promo_desc = "Extra 10% off with FESTIVE10"
    else:
        promo_desc = "Invalid or inapplicable promo code"

# Step 7: Apply discounts
discount_amount = cart_value * discount
subtotal = cart_value - discount_amount

if promo_discount < 1:  # percent-based promo
    promo_amount = promo_discount
else:  # flat promo
    promo_amount = promo_discount

final_total = subtotal - promo_amount

# Step 8: Print bill summary
print("\n----- BILL SUMMARY -----")
for item in items:
    line_total = item["price"] * item["quantity"]
    print(f"{item['name']}: ₹{item['price']} x {item['quantity']} = ₹{line_total:.2f}")
print(f"Cart Value: ₹{cart_value:.2f}")
print(f"{discount_desc}: -₹{discount_amount:.2f}")

if promo_code and promo_desc:
    if "Invalid" in promo_desc:
        print(f"Promo Code: {promo_desc}")
    else:
        print(f"Promo Code ({promo_code.upper()}): -₹{promo_amount:.2f} ({promo_desc})")

print(f"Final Amount to Pay: ₹{final_total:.2f}")
print("------------------------")
