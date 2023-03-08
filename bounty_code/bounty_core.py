def bounty_calculator(initial_credit: int, days: int, bounty_hunters=None) -> int:
    """
    A function used to calculate maximum profit based on
    bounty hunter availability

    ARGUMENTS
    ---------
    initial_credit: int
        amount of initial payment given by client

    days: int
        number of days given to complete job
 
    bounty_hunters: List<Hunter>
        provide list of available bounty hunters using the Hunter class

    """
    
    if bounty_hunters is None:
        bounty_hunters = sorted(_BOUNTY_HUNTERS, key=lambda x: x._pay)
    else:
        bounty_hunters = sorted(bounty_hunters, key=lambda x: x._pay)
    
    num_bounties = 0

    for _ in range(days):
        available = [
            hunter
            for hunter in bounty_hunters
            if hunter._pay <= initial_credit and hunter._days <= days
        ]
        if not available:
            raise Exception(
                "Job cannot be completed. \
                 No suitable bounty hunters for task."
            )

        best_hunter = min(available, key=lambda x: x._days)
        best_hunter.daysOnTaskSetter(best_hunter.days_on_task + 1)
        if best_hunter.days_on_task == best_hunter._days:
            # print(best_hunter)
            initial_credit -= best_hunter._pay
            num_bounties += 1
            initial_credit += 1000
            best_hunter.daysOnTaskSetter(0)

    if num_bounties == 0:
        raise Exception(
            "Job cannot be completed. \
                        No suitable bounty hunters for task."
        )

    return initial_credit


if __name__ == "__main__":
    import hunter

    boba = hunter.Hunter(500, 5, "Boba Fett")
    cad = hunter.Hunter(300, 8, "Cad Bane")
    aurra = hunter.Hunter(700, 2, "Aurra Sing")

    _BOUNTY_HUNTERS = [boba, cad, aurra]

    result = bounty_calculator(1000, 5)

    print("")
    print(f"Maximum Profit is {result}")
    print("")
