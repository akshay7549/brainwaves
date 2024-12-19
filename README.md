# ATM Interface Project

## Overview
The ATM Interface Project is a Python-based application that simulates the functionality of an Automated Teller Machine (ATM). It provides essential banking operations such as balance inquiry, cash withdrawal, deposits, fund transfers, and transaction history. This project demonstrates Python programming skills, modular design, and user interaction.

## Features
- **User Authentication**: Secure login with account number and PIN.
- **Balance Inquiry**: Check account balance.
- **Cash Withdrawal**: Withdraw specified amounts if funds are available.
- **Cash Deposit**: Add funds to the account.
- **Fund Transfer**: Transfer money between accounts.
- **Transaction History**: View a log of all transactions.
- **Exit Option**: Gracefully exit the interface.

## Project Structure
The project follows a modular structure, with the main functionalities encapsulated in methods for ease of use and clarity. Data is stored in a simulated database using Python dictionaries.

### Flow of Execution
1. **Authentication**: User logs in with account credentials.
2. **Menu Display**: User selects an operation from the menu.
3. **Operation Execution**: The system performs the chosen operation and updates account data.
4. **Exit**: The user logs out and exits the system.

## Requirements
- **Python Version**: 3.6 or above.
- **Libraries**: No additional libraries are required. This project uses core Python modules such as `time`.

## How to Run
1. Clone or download the project files to your local system.
2. Open a terminal and navigate to the project directory.
3. Run the Python script using the command:
   ```bash
   python atm_interface.py
   ```
4. Follow the on-screen instructions to log in and perform various operations.

## File Structure
- `atm_interface.py`: Main script that implements the ATM functionalities.
- `accounts` (Dictionary in code): Simulated database for storing account details and transaction history.

## Sample Accounts
- **Account Number**: `12345`
  - **PIN**: `1234`
  - **Initial Balance**: ₹10,000

- **Account Number**: `67890`
  - **PIN**: `5678`
  - **Initial Balance**: ₹5,000

## Testing
The application includes test cases to verify:
- Successful login with valid credentials.
- Error handling for invalid credentials.
- Correct balance updates after deposits, withdrawals, and transfers.
- Proper logging of transactions.

## Future Enhancements
- **Persistent Storage**: Integrate with SQLite or a similar database to store data permanently.
- **Encryption**: Encrypt sensitive data such as PINs.
- **GUI**: Develop a graphical interface using libraries like Tkinter or PyQt.

## License
This project is for educational purposes and is licensed under the MIT License.

For any issues or suggestions, feel free to contact me.
## MR.Akshay Kumar Email: akshaykumarstm2020@gmail.com
---
