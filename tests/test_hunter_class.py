import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(
    1, "D:\\MyData\\JobHunting\\portofolioProjects\\Bounty_Hunter\\bounty_code\\"
)
from hunter import Hunter

Boba = Hunter(pay=500, days=5, name="Boba Fett")
Cad = Hunter(pay=300, days=8, name="Cad Bane")
Aurra = Hunter(pay=700, days=2, name="Aurra Sing")

print(Boba.isAvailable)
Boba.availability(False)
print(Boba.isAvailable)
