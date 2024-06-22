age = int(input("What is your current age? "))

optimal_year= 90

age_in_days = age*364
age_in_weeks = age*52
age_in_year = age*12

optimal_year_in_days = optimal_year * 364
optimal_year_in_weeks = optimal_year * 52
optimal_year_in_months = optimal_year * 12


your_age_in_days = optimal_year_in_days - age_in_days
your_age_in_weeks = optimal_year_in_weeks - age_in_weeks
your_age_in_months = optimal_year_in_months - age_in_year


print(f"You have {your_age_in_days} days, {your_age_in_weeks} weeks, and {your_age_in_months} months left.")
