'''3.	Write a program that manages a list of countries and their capital cities. 
It should prompt the user to enter the name of a country. 
If the program already  "knows" the name of the capital city, it should display it.
 Otherwise it should ask the user to enter it. 
 This should carry on until the user terminates the program (how this happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered variously 
as, for example, "Wales", "wales", "WALES" and so on.
'''
def manage():
    data = {}

    while True:
        country = input("Enter a country (or 'exit' to quit): ").strip().lower()
        
        if country == "exit":
            break
        
        if country in data:
            print(f"The capital of {country.title()} is {data[country].title()}.")
        else:
            capital = input(f"Enter the capital of {country.title()}: ").strip()
            data[country] = capital
            print(f"Got it! The capital of {country.title()} is {capital.title()}.")

manage()
