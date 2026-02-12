# 🏦 Loan & Mortgage Calculator
### University of Göttingen | Python Programming Project

This project provides a comprehensive command-line tool for calculating key financial parameters of loans and mortgages. By inputting variables such as loan principal, interest rates, and payment terms, users can make informed financial decisions regarding monthly obligations and total interest costs.

---

## 🚀 Overview
This project helps you understand loans and mortgages with a handy calculator. Just provide a few details like loan amount, interest rate, and payment terms. The program will calculate key financial parameters, making informed decisions easier. You can determine your monthly payment, the total interest paid, or the loan amount you can afford.

## 🛠️ Key Features
* **Annuity Payments:** Calculate fixed monthly payments where the interest and principal components change over time.
* **Differentiated Payments:** Calculate decreasing monthly payments where the principal component remains constant.
* **Duration Estimation:** Determine exactly how many years and months it will take to repay a loan based on your monthly budget.
* **Overpayment Analysis:** Automatically calculates the total interest paid over the life of the loan.

---

## 📐 Mathematical Logic

The calculator implements standard financial formulas for accuracy:

### 1. Annuity Payment Formula
$$A = P \cdot \frac{i \cdot (1+i)^n}{(1+i)^n - 1}$$
Where $A$ is the monthly payment, $P$ is the principal, $i$ is the nominal interest rate, and $n$ is the number of periods.

### 2. Differentiated Payment Formula
$$D_m = \frac{P}{n} + i \cdot \left(P - \frac{P \cdot (m-1)}{n}\right)$$
Where $D_m$ is the payment for the $m$-th month.

---

## 📂 Project Structure
The repository is organized as a standalone Python application for clear accessibility and distribution:

```text
.
├── .gitignore              # Prevents tracking of .idea/, __pycache__, and .DS_Store
├── LICENSE                 # MIT License
├── README.md               # Project documentation and usage guide
├── loan_calculator.py      # Main application script
└── requirements.txt        # Project dependency list
