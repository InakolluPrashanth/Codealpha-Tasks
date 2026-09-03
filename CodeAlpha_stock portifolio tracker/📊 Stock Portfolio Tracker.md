# 📊 Stock Portfolio Tracker

A simple Python-based **Stock Portfolio Tracker** developed as part of the **CodeAlpha Python Programming Internship – Task 2**.

The program allows users to enter stock symbols and quantities, calculates the investment value of each stock, and displays the total portfolio investment. The final portfolio report is also saved to a text file.

## 🎯 Project Objective

The objective of this project is to build a simple stock portfolio tracker using Python while practicing:

- Dictionaries
- User input and output
- Conditional statements
- Loops
- Basic arithmetic operations
- Exception handling
- File handling

## 🚀 Features

- 📈 Hardcoded stock price dictionary
- 🔎 Stock symbol validation
- 🔢 User-defined stock quantities
- 💰 Automatic investment calculation
- 📊 Portfolio summary
- 💾 Saves the portfolio report to a `.txt` file
- ❌ Handles invalid stock names and quantities

## 🛠️ Technologies Used

- **Python 3**
- Python Dictionaries
- File Handling
- Exception Handling

## 💡 How It Works

The program contains a dictionary with predefined stock prices:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180,
    "META": 500,
    "NVDA": 120
}
```

The user enters a stock symbol and the number of shares they own.

The program then calculates:

```text
Investment Value = Stock Price × Quantity
```

Finally, the values of all stocks are added together to calculate the total portfolio investment.

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Stock-Portfolio-Tracker.git
```

### 2. Open the Project Folder

```bash
cd Stock-Portfolio-Tracker
```

### 3. Run the Python Program

```bash
python stock_portfolio_tracker.py
```

## 🖥️ Example

```text
=============================================
       STOCK PORTFOLIO TRACKER
=============================================

Available Stocks:
AAPL: $180
TSLA: $250
GOOGL: $140
MSFT: $420
AMZN: $180
META: $500
NVDA: $120

Enter 'done' when you have finished adding stocks.

Enter stock symbol: AAPL
Enter quantity of AAPL: 5

Enter stock symbol: TSLA
Enter quantity of TSLA: 2

Enter stock symbol: MSFT
Enter quantity of MSFT: 3

Enter stock symbol: done

=============================================
          PORTFOLIO SUMMARY
=============================================
AAPL | Quantity: 5 | Price: $180 | Value: $900
TSLA | Quantity: 2 | Price: $250 | Value: $500
MSFT | Quantity: 3 | Price: $420 | Value: $1260
---------------------------------------------
TOTAL INVESTMENT: $2660
=============================================

✅ Portfolio report saved as 'portfolio_report.txt'
```

## 📁 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio_tracker.py
├── portfolio_report.txt
└── README.md
```

## 📚 Key Concepts Learned

Through this project, I practiced:

1. **Dictionary** – storing stock symbols and prices.
2. **Input/Output** – collecting information from the user.
3. **Loops** – allowing multiple stocks to be entered.
4. **Conditional Statements** – validating stock symbols and quantities.
5. **Arithmetic Operations** – calculating investment values.
6. **Exception Handling** – handling invalid user input.
7. **File Handling** – saving the portfolio report to a text file.

## 🔮 Future Improvements

The project can be extended by adding:

- Live stock prices using an API
- CSV export functionality
- Graphical user interface (GUI)
- Portfolio performance tracking
- Profit and loss calculation
- Database storage
- Multiple user portfolios

## 👨‍💻 Author

**Inakollu Prashanth**

B.Tech – Artificial Intelligence & Machine Learning

## 🏆 Internship

**CodeAlpha Python Programming Internship**

**Task 2 – Stock Portfolio Tracker**

---

⭐ If you found this project useful, consider giving the repository a star!