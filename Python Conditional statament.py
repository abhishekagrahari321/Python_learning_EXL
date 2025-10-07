# E-commerce discount calculator

print("Welcome! Please enter your cart value:")
cart_value = float(input("Cart Value (₹): "))

membership = input("Enter your membership status (Premium/Regular): ").strip().lower()

if cart_value > 5000:
    if membership == "premium":
        discount = 0.20
    elif membership == "regular":
        discount = 0.10
    else:
        print("Invalid membership status. No discount applied.")
        discount = 0.0
elif 2000 < cart_value <= 5000:
    discount = 0.05
else:
    discount = 0.0

final_price = cart_value * (1 - discount)

print(f"Discount applied: {discount*100:.0f}%")
print(f"Final price to pay: ₹{final_price:.2f}")
