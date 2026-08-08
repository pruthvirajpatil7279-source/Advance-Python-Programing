#Write a program to implement a Configurable Payment Processing System Using Strategy Pattern.


class CreditCardPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class UpiPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class PayPalPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using PayPal")


# Step 2: Payment Processor (Context)
class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def make_payment(self, amount):
        self.payment_method.pay(amount)


# Step 3: Take payment method from user
print("Choose Payment Method:")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: ₹"))

# Step 4: Configure the payment strategy
if choice == 1:
    payment = CreditCardPayment()
elif choice == 2:
    payment = UpiPayment()
elif choice == 3:
    payment = PayPalPayment()
else:
    print("Invalid choice")
    exit()

# Step 5: Process payment
processor = PaymentProcessor(payment)
processor.make_payment(amount)