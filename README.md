# ATM Management System – Python & MySQL Project

##  Project Overview
This project is a **console-based ATM Management System** developed using **Python and MySQL**.  
It simulates basic banking operations such as account creation, deposit, withdrawal, and transaction history using a relational database.

The project demonstrates how **Python interacts with SQL databases** to perform real-world CRUD operations.

## Project Objectives
- Create and manage bank accounts using MySQL
- Implement deposit and withdrawal operations
- Store and display transaction history
- Separate **Admin** and **User** functionalities
- Practice Python–SQL database connectivity

## Technologies Used
- **Python**
- **MySQL**
- **MySQL Connector for Python**
- **SQL (CRUD Operations)**

---

## Database Design

### Database Name

### Table: `account_detail`
| Column Name | Description |
|------------|------------|
| account_no | Account Number |
| name | Account Holder Name |
| branch_name | Branch Name |
| opening_balance | Current Balance |
| date | Account Creation Date |
| status | Account Status |

### Table: `transaction_detail`
| Column Name | Description |
|------------|------------|
| account_no | Account Number |
| amount | Transaction Amount |
| transaction_type | Deposit / Withdraw |
| date | Transaction Date |


## System Roles

### Admin
- Insert new account records
- Delete existing accounts
- Admin authentication using password

### User
- View account details
- Deposit money
- Withdraw money
- View transaction history


##  Project Workflow
1. User selects **Admin** or **User**
2. Admin logs in using password
3. Admin can insert or delete accounts
4. User logs in using account number
5. User performs banking operations
6. All transactions are stored in MySQL database


## Key Concepts Demonstrated
- Python–MySQL database connectivity
- SQL queries using Python
- CRUD operations (Insert, Select, Update, Delete)
- Conditional logic and loops
- Menu-driven console application


##  How to Run the Project
1. Install MySQL and create the database and tables
2. Install MySQL connector:


## Author
**Prityush Kumar Choubey**  
Aspiring Data Analyst 
Skills: Python, SQL, MySQL

---
