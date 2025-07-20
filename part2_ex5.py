class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("서브클래스에서 구현해야 합니다.")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"{amount}원을 신용카드로 결제합니다.")

class KakaoPay(PaymentMethod):
    def pay(self, amount):
        print(f"{amount}원을 카카오페이로 결제합니다.")

class BankTransfer(PaymentMethod):
    def pay(self, amount):
        print(f"{amount}원을 계좌이체로 결제합니다.")

def process_payment(methods, amount):
    for method in methods:
        method.pay(amount)

methods = [CreditCard(), KakaoPay(), BankTransfer()]
process_payment(methods, 10000)