# 1. Function to calculate Performance Bonus
def calculate_bonus(base_salary , performance_rating):
    if performance_rating == 5:
        bonus_percentage = 0.20
    elif performance_rating >= 3:
        bonus_percentage = 0.10
    else: 
        bonus_percentage = 0.0
    return base_salary * bonus_percentage

#  2. Function to calculate progressive tax deduction
def calculate_tax(gross_salary):
    if gross_salary > 7000:
        tax_percentage = 0.15
    elif gross_salary >= 3000:
        tax_percentage = 0.10
    else : 
        tax_percentage = 0.0

    return gross_salary * tax_percentage

# 3. core runtime application
def main_hr_app():
    print("welcome to Crporate Pyroll System" )

    emp_name = input (" Enter employee name:")
    base_salary = float(input("Enter base salary:"))  
    rating = int(input("Enter performance rating (1-5):"))
    if rating < 1 or rating >5 or base_salary < 0:
        print("❌ Invalide data enterd. Please check the inputs and try again. ")
        return

    # Process flow via functions
    bonus = calculate_bonus(base_salary , rating)
    gross_salary = base_salary + bonus
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax

    #  output statement geneator
    print("\n" + "="*40 )
    print(f"Pyroll statement for {emp_name}")
    print("="*40)
    print(f".Base Salary:                              {base_salary:.2f} EGP")
    print(f".Performance Bonus:                        {bonus:.2f} EGP")
    print(f".Gross Salary:                             {gross_salary:.2f} EGP")
    print(f".Tax Deduction:                            {tax:.2f} EGP")
    print("-"*40)
    print(f".Net payable cash:                         {net_salary:.2f}")
# tRIGGAER PROGRAM RUN 
main_hr_app()
