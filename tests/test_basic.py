import sys

sys.path.insert(
    1, "D:\\MyData\\JobHunting\\portofolioProjects\\Bounty_Hunter\\bounty_code\\"
)
from hunter import Hunter
from bounty_core import bounty_calculator

print("~~~ Running Basic Test 1 ~~~")
print("")

boba = Hunter(pay=500, days=5, name="Boba Fett")
cad = Hunter(pay=300, days=8, name="Cad Bane")
aurra = Hunter(pay=700, days=2, name="Aurra Sing")

_BOUNTY_HUNTERS = [boba, cad, aurra]

result = bounty_calculator(1000, 5, _BOUNTY_HUNTERS)

print(f"Basic Test 1: Maximum profit is {result}")
print("")
