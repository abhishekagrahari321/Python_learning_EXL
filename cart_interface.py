# Create an interface where user will add their following details
print("Welcome to this site. Please enter your cart value:")
cart_value = int(input("Value: "))

customer = input("Enter your customer type (premium/regular): ").strip().lower()

if cart_value > 5000:
    if customer == "premium":
        price = cart_value - (20 * cart_value) / 100
    elif customer == "regular":
        price = cart_value - (10 * cart_value) / 100
    else:
        print("Invalid customer type!")
        price = None
elif 2000 < cart_value <= 5000:
    price = cart_value - (5 * cart_value) / 100
else:
    price = cart_value

if price is not None:
    print(f"Final price to pay: {price}")