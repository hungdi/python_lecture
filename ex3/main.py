from delivery_system import DeliverySystem
from delivery_person import DeliveryPerson
from delivery_method import DeliveryMethod, Drone, Motorbike, Bicycle
from user import User
from order import Order


ds = DeliverySystem()
user1 = User("고객1")
user1.order_deliver(ds, "짜장면", Drone())
user1.order_deliver(ds, "비빔국수", Drone())
user1.order_deliver(ds, "콩국수", Drone())

delivery_person1 = DeliveryPerson(Drone())
delivery_person2 = DeliveryPerson(Drone())
delivery_person3 = DeliveryPerson(Drone())
ds.process_order(delivery_person1)
ds.process_order(delivery_person2)
ds.process_order(delivery_person3)