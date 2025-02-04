
class Payment:

    def process_payment(self):
        print("Payment is Processing!!!\n")

class CreditCardPayment(Payment):

    def process_payment(self):
        print("Credit Card Payment is Processing!!!\n")

class PayPalPayment:

    def process_payment(self):
        print("PayPal Payment is Processing!!!\n")

class BitcoinPayment:

    def process_payment(self):
        print("Bitcoin Payment is Processing!!!\n")

print("Payment :")
P=Payment()
P.process_payment()

print("Credit Card Payment :")
C=CreditCardPayment()
C.process_payment()

print("PayPal Payment :")
PP=PayPalPayment()
PP.process_payment()

print("Bitcoin Payment :")
B=BitcoinPayment()
B.process_payment()
