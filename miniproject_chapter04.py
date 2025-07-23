class Spending:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def summary(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"

    def get_tax_deduction(self):
        return 0


class FoodSpending(Spending):
    def get_tax_deduction(self):
        return int(self.amount*0.1)

class TransportSpending(Spending):
    def get_tax_deduction(self):
        return int(self.amount*0.05)

class EntertainmentSpending(Spending):
    def get_tax_deduction(self):
        return 0


class SpendingManager:
    def __init__(self):
        self.spending_list = []

    def add_spending(self, spending):
        self.spending_list.append(spending)

    
    def total_by_category(self, category):
        return sum(s.amount for s in self.spending_list if s.category == category)

    def total_tax_deduction(self):
        return sum(s.get_tax_deduction() for s in self.spending_list)

    def remove_by_date(self, date):
        # 해당하는 date의 list를 모두 삭제
        self.spending_list = [s for s in self.spending_list if s.date != date]

    def print_all(self):
        for s in self.spending_list:
            print(f"{s.summary()} -> 환급가능: {s.get_tax_deduction()} 원")





manager = SpendingManager()

s1 = FoodSpending("2025-07-20", 5000, "식비", "편의점")
s2 = TransportSpending("2025-07-21", 3000, "교통", "지하철")
s3 = FoodSpending("2025-07-22", 12000, "식비", "고기집")

manager.add_spending(s1)
manager.add_spending(s2)
manager.add_spending(s3)

print("전체 지출 목록")
manager.print_all()
# 출력:
# 2025-07-20 | 식비 | 5000원 | 편의점 -> 환급가능:500원
# 2025-07-21 | 교통 | 3000원 | 지하철 -> 환급가능:150원
# 2025-07-22 | 식비 | 12000원 | 고기집 -> 환급가능:1200원

print(f"식비 총 지출: {manager.total_by_category('식비')}원")
print(f"총 환급 예상금액: {manager.total_tax_deduction()}원")
# 출력: 
# 식비 총 지출: 17000원
# 총 환급 예상 금액: 1850원

manager.remove_by_date("2025-07-21")
manager.print_all()
# 출력:
# 2025-07-20 | 식비 | 5000원 | 편의점 -> 환급가능:500원
# 2025-07-22 | 식비 | 12000원 | 고기집 -> 환급가능:1200원


print(f"식비 총 지출: {manager.total_by_category('식비')}원")
print(f"총 환급 예상금액: {manager.total_tax_deduction()}원")
