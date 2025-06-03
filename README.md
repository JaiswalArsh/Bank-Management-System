# Banking System

A simple console-based banking system implemented in Python using MySQL for data storage. This application allows users to sign up, log in, and perform basic banking operations such as balance inquiries, deposits, withdrawals, and fund transfers.

## Features
- **User Registration**: Create a new account with a unique username, password, and account number.
- **Login System**: Securely log in with username and password.
- **Banking Operations**:
  - Check account balance.
  - Deposit money into the account.
  - Withdraw money from the account (with balance validation).
  - Transfer funds to another account (with account number validation).
- **Transaction History**: Maintains a record of all transactions for each user.
- **Database Integration**: Uses MySQL to store customer details and transaction records.

## Prerequisites
- Python 3.x
- MySQL Server
- MySQL Connector for Python (`mysql-connector-python`)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JaiswalArsh/Bank-Management-System.git
   cd Bank-Management-System
   ```

2. **Install Dependencies**:
   Install the required Python package:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set Up MySQL Database**:
   - Ensure MySQL is installed and running.
   - Create a database named `bank`:
     ```sql
     CREATE DATABASE bank;
     ```
   - Update the database connection details in `database.py` if necessary (default: host=`localhost`, user=`root`, password=`PASSWORD`, database=`bank`).

4. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage
1. **Run the Program**:
   - Start the application by running `main.py`.
   - You will be greeted with a welcome message and prompted to choose between:
     - **Sign Up**: Create a new account.
     - **Log In**: Access an existing account.

2. **Available Services** (after logging in):
   - **Balance Enquiry**: Check the current balance.
   - **Cash Deposit**: Deposit money into your account.
   - **Cash Withdraw**: Withdraw money from your account.
   - **Funds Transfer**: Transfer money to another account using their account number.
   - **Exit**: Log out and exit the application.

## File Structure
- `main.py`: Entry point of the application, handles user interaction and menu navigation.
- `register.py`: Manages user registration (SignUp) and login (LogIn) functionality.
- `customer.py`: Defines the `Customer` class for creating and storing user details.
- `bank.py`: Defines the `Bank` class for handling banking operations and transaction records.
- `database.py`: Manages MySQL database connection and query execution.

## Database Schema
- **customers Table**:
  - `username` (VARCHAR): Unique username.
  - `password` (VARCHAR): User password.
  - `name` (VARCHAR): User's full name.
  - `age` (INTEGER): User's age.
  - `city` (VARCHAR): User's city.
  - `balance` (INTEGER): Current account balance.
  - `account_number` (INTEGER): Unique account number.
  - `status` (BOOLEAN): Account status (active/inactive).

- **{username}_transaction Table** (created per user):
  - `timedate` (VARCHAR): Timestamp of the transaction.
  - `account_number` (INTEGER): User's account number.
  - `remarks` (VARCHAR): Transaction description (e.g., "Amount Deposit").
  - `amount` (INTEGER): Transaction amount.

## Notes
- **Security Warning**: The current implementation uses plain text passwords and is vulnerable to SQL injection. For production use, consider:
  - Hashing passwords (e.g., using `bcrypt`).
  - Using parameterized queries to prevent SQL injection.
- The application generates random 8-digit account numbers and ensures uniqueness.
- Ensure the MySQL database is running before executing the program.
- The application commits changes to the database after each transaction to ensure data persistence.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
