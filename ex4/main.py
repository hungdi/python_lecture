from user import User
from food import Food
from kitchen import Kitchen

u1 = User("민지")
foods = [Food("짜장면", 7), Food("탕수육", 5)]
order = u1.make_orders(foods)

k = Kitchen()
k.receive_order(order)
k.cook_order()