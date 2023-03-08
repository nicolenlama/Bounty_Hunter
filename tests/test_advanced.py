import sys

sys.path.insert(
    1, "D:\\MyData\\JobHunting\\portofolioProjects\\Bounty_Hunter\\bounty_code\\"
)
from hunter import Hunter
from bounty_core import bounty_calculator

# Test 1
print("~~~~ Running Test 1 ~~~~")
print("")

asajj = Hunter(pay=200, days=5, name="Asajj Ventress")
embo = Hunter(pay=300, days=4, name="Embo")
ig = Hunter(pay=100, days=8, name="IG-88")
bossk = Hunter(pay=500, days=9, name="Bossk")
zam = Hunter(pay=250, days=10, name="Zam Wesell")

_BOUNTY_HUNTERS = [asajj, embo, ig, bossk, zam]

result = bounty_calculator(1000, 8, _BOUNTY_HUNTERS)

print(f"Test 1: Maximum profit is {result}")
print("")

# Test 2 - Should return error
print("~~~ Running Test 2 ~~~~~~")
print("")

asajj = Hunter(pay=1200, days=5, name="Asajj Ventress")
embo = Hunter(pay=2300, days=4, name="Embo")
ig = Hunter(pay=3100, days=8, name="IG-88")
bossk = Hunter(pay=500, days=9, name="Bossk")
zam = Hunter(pay=1250, days=10, name="Zam Wesell")

_BOUNTY_HUNTERS = [asajj, embo, ig, bossk, zam]

result = bounty_calculator(200, 10, _BOUNTY_HUNTERS)

print(f"Test 2: Maximum profit is {result}")
