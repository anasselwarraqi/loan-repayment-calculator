"""
Project: Loan Calculator
Author: Anass El Warraqi
Description: This project helps you understand loans and mortgages with a handy calculator.
Just provide a few details like loan amount, interest rate, and payment terms.
The program will calculate key financial parameters, making informed decisions easier.
You can determine your monthly payment, the total interest paid, or the loan amount you can afford.
"""

import argparse
import math

def calculate_annuity_payment(principal: float, periods: int, interest_rate: float):
    """Calculates the monthly annuity payment."""
    i = interest_rate
    payment = principal * (i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)
    return math.ceil(payment)


def calculate_principal(payment: float, periods: int, interest_rate: float):
    """Calculates the loan principal."""
    i = interest_rate
    # Formula: P = A / ((i * (1+i)^n) / ((1+i)^n - 1))
    principal = payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
    return math.floor(principal)


def calculate_periods(principal: float, payment: float, interest_rate: float):
    """Calculates the number of months needed to repay."""
    i = interest_rate
    # Formula: n = log(A / (A - i*P)) / log(1+i)
    try:
        n_months = math.log(payment / (payment - i * principal), 1 + i)
        return math.ceil(n_months)
    except ValueError:
        # Handles cases where payment is too low to cover interest
        return float('inf')


def calculate_diff_payments(principal: float, periods: int, interest_rate: float):
    """Calculates and prints differentiated payments."""
    total_paid = 0
    i = interest_rate

    for month in range(1, periods + 1):
        # Differentiated formula: D = P/n + i * (P - P*(m-1)/n)
        payment = (principal / periods) + i * (principal - (principal * (month - 1) / periods))
        rounded_payment = math.ceil(payment)
        total_paid += rounded_payment
        print(f"Month {month}: payment is {rounded_payment}")

    overpayment = total_paid - principal
    print(f"\nOverpayment = {int(overpayment)}")


def format_period_output(n_months: int):
    """Formats the output string for years and months."""
    years = n_months // 12
    months = n_months % 12

    result = []
    if years == 1:
        result.append("1 year")
    elif years > 1:
        result.append(f"{years} years")

    if months == 1:
        result.append("1 month")
    elif months > 1:
        result.append(f"{months} months")

    duration_str = " and ".join(result)
    print(f"It will take {duration_str} to repay this loan!")


def main():
    parser = argparse.ArgumentParser(description="A loan calculator supporting annuity and differentiated payments.")

    # Use None as default to easily check if an argument was missing
    parser.add_argument("--type", choices=["annuity", "differentiated"], help="Type of payment")
    parser.add_argument("--payment", type=float, default=None, help="The monthly payment amount")
    parser.add_argument("--principal", type=float, default=None, help="The loan principal")
    parser.add_argument("--periods", type=int, default=None, help="Number of months")
    parser.add_argument("--interest", type=float, default=None, help="Interest rate (without percent sign)")

    args = parser.parse_args()

    # --- Validation Logic ---
    params = [args.type, args.payment, args.principal, args.periods, args.interest]

    # Check for negative values
    if any(x is not None and x < 0 for x in [args.payment, args.principal, args.periods, args.interest]):
        print("Incorrect parameters")
        return

    # Interest is mandatory
    if args.interest is None:
        print("Incorrect parameters")
        return

    # Type is mandatory
    if args.type is None:
        print("Incorrect parameters")
        return

    # Check for valid combinations based on calculation type
    if args.type == "differentiated":
        if args.payment is not None:  # Differentiated cannot have payment as input
            print("Incorrect parameters")
            return
        if args.principal is None or args.periods is None:
            print("Incorrect parameters")
            return

        # Execute Differentiated Logic
        nominal_interest = (args.interest / 100) / 12
        calculate_diff_payments(args.principal, args.periods, nominal_interest)

    elif args.type == "annuity":
        nominal_interest = (args.interest / 100) / 12

        # Case 1: Calculate Monthly Payment
        if args.principal is not None and args.periods is not None and args.payment is None:
            monthly_payment = calculate_annuity_payment(args.principal, args.periods, nominal_interest)
            print(f"Your monthly payment = {monthly_payment}!")
            print(f"Overpayment = {int(monthly_payment * args.periods - args.principal)}")

        # Case 2: Calculate Principal
        elif args.payment is not None and args.periods is not None and args.principal is None:
            principal = calculate_principal(args.payment, args.periods, nominal_interest)
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {int(args.payment * args.periods - principal)}")

        # Case 3: Calculate Periods (Time)
        elif args.principal is not None and args.payment is not None and args.periods is None:
            months = calculate_periods(args.principal, args.payment, nominal_interest)
            format_period_output(months)
            print(f"Overpayment = {int(args.payment * months - args.principal)}")
        else:
            # If arguments don't fit the combinations (e.g., too few args)
            print("Incorrect parameters")


if __name__ == "__main__":
    main()