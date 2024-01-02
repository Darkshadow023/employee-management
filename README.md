# employee-management
A fun little python project on Employee Management system for my school project

This Python project is an Employee Management System that utilizes Tkinter for the graphical user interface (GUI) and Python-MySQL connectivity for the database. It also includes functionalities for handling CSV files for data storage and retrieval.

Installation
Prerequisites
Python 3.x
MySQL Server
Required Python libraries: tkinter, mysql-connector-python
Setting up the environment
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your_username/employee-management-system.git
Install the required Python libraries:

bash
Copy code
pip install mysql-connector-python
Set up the MySQL database:

Create a MySQL database named employee_db.
Execute the database_setup.sql script located in the database directory to set up the necessary tables and structure.
Usage
Run the main application file:

bash
Copy code
python main.py
The application GUI will appear, providing options to perform various operations related to employee management such as adding, editing, deleting, and viewing employee records.

The application supports both MySQL database and CSV file handling for storing employee data. Use the appropriate functionality in the GUI to switch between these modes.
