from vending_machine import VendingMachine
from drink import OrangeJuice, ZeroCoke, Water
from user import User

vm = VendingMachine({
    OrangeJuice():10,
    ZeroCoke():10,
    Water():10,
})

vm.show_menu()

user1 = User("방문자1", 10000)
user1.buy(vm, OrangeJuice())

user2 = User('방문자2', 5000)
user2.buy(vm, Water())

vm.show_menu()
vm.add_drink(OrangeJuice(), 3)
vm.show_menu()
