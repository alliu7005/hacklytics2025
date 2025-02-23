import scipy.stats as stats

means = { 
    'A': {'loan': 42417.50, 'income': 7506.99, 'housing': 1697.04, 'fico': 697.36}, 
    'B': {'loan': 41790.81, 'income': 8053.57, 'housing': 1694.57, 'fico': 732.11}, 
    'C': {'loan': 41135.67, 'income': 6322.16, 'housing': 1344.64, 'fico': 674.77} 
} 

std_devs = { 
    'A': {'loan': 28226.47, 'income': 3389.70, 'housing': 670.73, 'fico': 74.11}, 
    'B': {'loan': 27723.42, 'income': 3256.77, 'housing': 667.93, 'fico': 53.84}, 
    'C': {'loan': 27824.07, 'income': 3137.70, 'housing': 672.80, 'fico': 81.54}
}

commissions = {'A': 250, 'B': 350, 'C': 150}

job_status_adjustment = {
    1: {'A': 0.86851, 'B': 0.89643, 'C': 0.75142},
    2: {'A': 0.1167, 'B': 0.0898, 'C': 0.1695},
    3: {'A': 0.0148, 'B': 0.0138, 'C': 0.0138}
}

employment_sector_adjustment = {
    1: {'A': 0.229481, 'B': 0.2367347, 'C': 0.1882747},
    2: {'A': 0.058193, 'B': 0.0505102, 'C': 0.0626466},
    3: {'A': 0.025864, 'B': 0.0173469, 'C': 0.0251256},
    4: {'A': 0.077433, 'B': 0.0826531, 'C': 0.080402},
    5: {'A': 0.0487481, 'B': 0.0489796, 'C': 0.0562814},
    6: {'A': 0.1155696, 'B': 0.122449, 'C': 0.0968174},
    7: {'A': 0.1331454, 'B': 0.1403061, 'C': 0.1363484},
    8: {'A': 0.0807495, 'B': 0.0872449, 'C': 0.0770519},
    9: {'A': 0.0684795, 'B': 0.0673469, 'C': 0.0623116},
    10: {'A': 0.0984911, 'B': 0.0923469, 'C': 0.0923469},
    11: {'A': 0.0490798, 'B': 0.0403061, 'C': 0.0371859}
}

bankruptcy_adjustment = {
    1: {'A': 0.995, 'B': 1.0, 'C': 0.984},
    0: {'A': 0.0, 'B': 0.0, 'C': 0.0}
}

sectors = [
    "IT",
    "Communication Services",
    "Consumer Discretionary",
    "Consumer Staples",
    "Energy",
    "Financials",
    "Health Care",
    "Industrials",
    "Materials",
    "Real Estate",
    "Utilities"
]

def calculate_z(x, mean, std_dev):
    return (x - mean) / std_dev

def calculate_probability(z):
    return stats.norm.cdf(z)

def calculate_average_probability(user_input):
    probabilities = {'A': 0, 'B': 0, 'C': 0}
    
    for bank in ['A', 'B', 'C']:
        total_probability = 0
        count = 0
        for factor in ['loan', 'income', 'housing', 'fico']:
            user_value = user_input[factor]
            z = calculate_z(user_value, means[bank][factor], std_devs[bank][factor])
            probability = calculate_probability(z)

            if factor == 'housing' or factor == 'loan':
                probability = 1-probability
            
            total_probability += probability
            count += 1
            
        probabilities[bank] = total_probability  # No averaging here
    
    return probabilities

def find_best_bank(user_dict, job_status, never_bankrupt, employment_sector = 0):
    #user_input = {
    #    'loan': float(input("Enter Loan Amount: ")),
    #    'income': float(input("Enter Monthly Income: ")),
    #    'housing': float(input("Enter Monthly Housing Payment: ")),
    #    'fico': float(input("Enter FICO Score: "))
    #}
    
    #job_status = int(input("Enter Job Status (1 -> Full Time, 2 -> Part Time, 3 -> Unemployed): "))

    #if job_status not in job_status_adjustment:
        #print("Invalid Job Status")
    #    return

    if job_status != 3:
        #print("\nSelect Your Employment Sector:")
        #for idx, sector in enumerate(sectors, 1):
        #    print(f"{idx} -> {sector}")
        
        #employment_sector = int(input("Enter the number corresponding to your employment sector: "))

        if employment_sector not in employment_sector_adjustment:
            employment_sector = 0
    else:
        employment_sector = 0

    #never_bankrupt = int(input("Have you ever been bankrupt or foreclosed? (1 -> No, 0 -> Yes): "))
    #if never_bankrupt not in bankruptcy_adjustment:
    #    print("Invalid input for bankruptcy status")
    #    return

    probabilities = calculate_average_probability(user_dict)

    final_probabilities = {}
    for bank in probabilities:
        total = probabilities[bank] + job_status_adjustment[job_status][bank]
        count = 5  # 4 continuous + 1 job_status
        
        if employment_sector != 0:
            total += employment_sector_adjustment[employment_sector][bank]
            count += 1
        
        total += bankruptcy_adjustment[never_bankrupt][bank]
        count += 1

        final_probabilities[bank] = total / count

    #print("\nBank Probabilities After Adjustments:")
    #s = []
    #for bank, prob in final_probabilities.items():
    #    print(f"Bank {bank}: {prob:.4f}")


    # Sort banks by probability in descending order
    sorted_banks = sorted(final_probabilities, key=final_probabilities.get, reverse=True)
    highest_bank, second_highest_bank, third_highest_bank = sorted_banks[:3]
    
    highest_prob = final_probabilities[highest_bank]
    second_prob = final_probabilities[second_highest_bank]
    third_prob = final_probabilities[third_highest_bank]
    # Apply conditions to select the best bank
    p = 0
    if second_prob*1.15 >= highest_prob:
        best_bank = second_highest_bank
        p = 1 
    elif third_prob*1.03 >= highest_prob * 1.03:
        best_bank = third_highest_bank
        p = 1

    else:
        best_bank = highest_bank
        p = 0



#    best_bank = max(final_probabilities, key=final_probabilities.get)
    #print(f"\nThe best bank for you (based on approval probability) is **Bank {best_bank}** with a probability of **{final_probabilities[best_bank]:.4f}**")

    expected_commissions = {bank: final_probabilities[bank] * commissions[bank] for bank in final_probabilities}

    best_commission_bank = max(expected_commissions, key=expected_commissions.get)

    #print("\nExpected Commission for Each Bank:")
    #for bank, commission in expected_commissions.items():
    #    print(f"Bank {bank}: ${commission:.2f}")
    if p == 1:
    #    print(f"\nThe best bank to recommend (based on commission) is **Bank {best_bank}** with an expected commission of **${expected_commissions[best_bank]:.2f}**")
        return(best_bank, final_probabilities[best_bank])
    else:
    #    print(f"\nThe best bank to recommend (based on commission) is **Bank {best_commission_bank}** with an expected commission of **${expected_commissions[best_commission_bank]:.2f}**")
        return(best_commission_bank, final_probabilities[best_commission_bank])

#while True:
#    find_best_bank()



