def class_to_dictionary(hunters):
    """
    This function will return a dictionary version of the 
    Hunter class
    """

    hunters_res = []
    for hunter in hunters:
        hunter_dict = {
            "pay": hunter._pay,
            "pay_rate": hunter._pay_rate,
            "days": hunter._days,
            "available": hunter.available,
            "days_on_task": 0,
        }
        hunters_res.append(hunter_dict)

    return hunters_res
