def bounty_calculator(initial_credit, days):
    
    guaranteed_rate = 1000
    work_days = floor(given_days/number_of_days_to_get_bounty)
    payment_owed = work_days * pay_rate
    total = work_days * guaranteed_rate + initial_credit 
    
    cost = [500,300,700]
    day = [5,8,2]
    
    day_left = [0,0,0]
    for day in range(len(days)): 
        day_left[0] 