# Bounty Hunter



## Prompt

You run a bounty hunting guild in the Outer Rim. It's been a busy season and you are struggling to keep up with the demand. You also noticed that your bounty hunters' performance and rewards vary widely.

It also doesn't help that they require payment upfront. We are in a hunter's market after all.
Given an initial amount of credit (₹) and a number of days as parameters, write a function that maximizes your profit based on the bounty hunter's assignment. There's a fixed ₹1,000 reward per bounty.

Bounty Reward: ₹1000
Available Bounty Hunters:

* Bounty Hunter 1
    - Pay Rate: ₹500
    - Number of days to get bounty: 5

* Bounty Hunter 2:
    - Pay Rate: ₹300
    - Number of days: 8

* Bounty Hunter 3:
    - Pay Rate: ₹700
    - Number of days: 2

 
### Scenario 1: you are staring with ₹1000 and you have 5 days to complete the task

* if you send bounty hunter 3 twice, you will have ₹1600

* if you send bounty hunter 1 once, you will have ₹1500



## Greedy Implementation
I decided to solve this problem using a Greedy approach. 
1. Initialize a list of bounty hunters with their pay rates and times required to completed the bounty (I created a Bounty Hunter class to help me organize the data)
2. Sort the bounty hunters by increasing pay
3. Find the bounty hunter who requires the least amount of time to complete a task and can be paid with the available credit
4. If a bounty hunter exists, return the total profit
5. If a bounty hunter does not exist, exit the program

 
