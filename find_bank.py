import scipy.stats as stats

means = { 
'A': {'loan': 42417.50, 'income': 7506.99, 'housing': 1697.04, 'fico': 697.36}, 
'B': {'loan': 41790.81, 'income': 8053.57, 'housing': 1694.57, 'fico': 732.11}, 
'C': {'loan': 41135.67, 'income': 6322.16, 'housing': 1344.64, 'fico': 674.77} } 


std_devs = { 
'A': {'loan': 28226.47, 'income': 3389.70, 'housing': 670.73, 'fico': 74.11}, 
'B': {'loan': 27723.42, 'income': 3256.77, 'housing': 667.93, 'fico': 53.84}, 
'C': {'loan': 27824.07, 'income': 3137.70, 'housing': 672.80, 'fico': 81.54}
}


def calculate_z(x, mean, std_dev):
    return (x - mean) / std_dev

def calculate_probability(z):
    return stats.norm.cdf(z)

def calculate_average_probability(user_input):
    probabilities = {'A': 0, 'B': 0, 'C': 0}
    
    for bank in ['A', 'B', 'C']:
        total_probability = 0
        
        # Calculate probability for each factor and add it
        for factor in ['loan', 'income', 'housing', 'fico']:
            user_value = user_input[factor]
            z = calculate_z(user_value, means[bank][factor], std_devs[bank][factor])
            probability = calculate_probability(z)
            total_probability += probability
        
        # Average the probabilities for the current bank
        probabilities[bank] = total_probability / 4
    
    return probabilities

def find_best_bank(user_dict, job_status):
    # User input
    #user_input = {
    #    'loan': float(input("Enter Loan Amount: ")),
    #    'income': float(input("Enter Monthly Income: ")),
    #    'housing': float(input("Enter Monthly Housing Payment: ")),
    #    'fico': float(input("Enter FICO Score: ")),
        
    #}
    #job_status = int(input("Enter 1-> Full time 2-> Part Time 3-> Unemployed"))
    # Calculate probabilities for each bank
    probabilities = calculate_average_probability(user_dict)

    
    # # Find the bank with the highest probability

    print("\nBank Probabilities:")
    # for bank, prob in probabilities.items():
    #     print(f"Bank {bank}: {prob:.4f}")

# Selecting the bank with the highest probability
    best_bank = max(probabilities, key=probabilities.get)
    if job_status == 1:
        if best_bank == "C":
            print("here")
            final_pro = ((probabilities[best_bank])+(0.75142))/2
        elif best_bank == "B":
            final_pro = ((probabilities[best_bank])+(0.89643))/2
        elif best_bank == "A":
            final_pro = ((probabilities[best_bank])+(0.86851))/2
    print(best_bank)
    print(f"The best bank for you is Bank {best_bank} with a probability of {final_pro:.4f}")
    return(best_bank, final_pro)


#while True:
#   find_best_bank()