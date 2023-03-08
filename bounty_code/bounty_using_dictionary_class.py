def bounty_calculator(initial_credit: int, days: int) -> int:
    from helper import class_to_dictionary

    bounty_hunters = class_to_dictionary(_BOUNTY_HUNTERS)

    bounty_hunters.sort(key=lambda x: x["pay"])
    num_bounties = 0
    for day in range(days):
        available = [
            hunter
            for hunter in bounty_hunters
            if hunter["pay"] <= initial_credit and hunter["days"] <= days
        ]
        if not available:
            break

        best_hunter = min(available, key=lambda x: x["days"])
        best_hunter["days_on_task"] += 1
        if best_hunter["days_on_task"] == best_hunter["days"]:
            initial_credit -= best_hunter["pay"]
            num_bounties += 1
            initial_credit += 1000
            best_hunter["days_on_task"] = 0

    if num_bounties == 0:
        raise ValueError(
            "Job cannot be completed. No suitable bounty hunters for task."
        )

    return initial_credit


if __name__ == "__main__":
    import hunter

    boba = hunter.Hunter(500, 5, "Boba Fett")
    cad = hunter.Hunter(300, 3, "Cad Bane")
    aurra = hunter.Hunter(700, 2, "Aurra Sing")

    _BOUNTY_HUNTERS = [boba, cad, aurra]

    result = bounty_calculator(1000, 5)
    print(result)
