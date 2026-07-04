# Corporate Payroll & HR System (Python Capstone Project)

Welcome to my Python Capstone Project! This is a modular, structured program that simulates a corporate Human Resources (HR) and Payroll system. It follows clean code guidelines, handles user inputs, and utilizes independent python functions to calculate employee bonuses, taxes, and final salaries.

## 🚀 Features
* Dynamic Bonus Calculation: Applies performance-based rewards (up to 20%) based on employee evaluation scores.
* Progressive Tax Deductions: Implements hierarchical tax rates depending on the employee's gross income.
* Data & Input Validation: Prevents logical execution errors by verifying user ratings and financial figures before processing.

---

## 💻 Sample Project Execution (Output)

Here is a live example of the program runtime and how the formatted payroll statement looks when executed:

welcome to Corporate Payroll System
Enter employee name: samy
Enter base salary: 5000
Enter performance rating (1-5): 4

========================================
Pyroll statement for samy
========================================
.Base Salary:                   5000.00 EGP
.Performance Bonus:             500.00 EGP
.Gross Salary:                  5500.00 EGP
.Tax Deduction:                 550.00 EGP
----------------------------------------
.Net payable cash:              4950.00 EGP
========================================
---

## 🛠️ Project Architecture (Functions)
1. calculate_bonus(base_salary, performance_rating): Computes individual corporate bonuses based on standard tiers.
2. calculate_tax(gross_salary): Automatically computes progressive tax brackets.
3. main_hr_app(): The main controller that orchestrates user inputs, validation, business logic execution, and output formatting.
