
# Database Creation Guide for Thermal Imaging Drone Project

This guide provides step-by-step instructions for setting up the database to store GPS coordinates and timestamps of drone detections.

---

## Prerequisites

- **Operating System**: Ubuntu 22.04 or similar
- **Database Software**: MySQL Server
- **Python**: Installed with required libraries (if using scripts)

---

## Steps for MySQL Installation

1. **Update the System:**
    ```bash
    sudo apt update
    sudo apt upgrade
    ```

2. **Install MySQL Server:**
    ```bash
    sudo apt install mysql-server
    ```

3. **Start MySQL Service:**
    ```bash
    sudo systemctl start mysql.service
    ```

4. **Check MySQL Service Status:**
    ```bash
    sudo service mysql status
    ```

---

## Configure MySQL

1. **Log into MySQL:**
    ```bash
    sudo mysql
    ```

2. **Reset MySQL Root Password:**
    ```sql
    ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'your_password';
    ```

3. **Log Back In with New Password:**
    ```bash
    mysql -u root -p
    ```

---

## Create the Database

1. **Create Database:**
    ```sql
    CREATE DATABASE GPS;
    ```

2. **Use the Database:**
    ```sql
    USE GPS;
    ```

---

## Create the Table

1. **Define the Table Structure:**
    ```sql
    CREATE TABLE Coordinates (
        id INT AUTO_INCREMENT PRIMARY KEY,
        latitude DECIMAL(10, 8),
        longitude DECIMAL(11, 8),
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    ```

2. **Verify the Table:**
    ```sql
    SHOW TABLES;
    ```

3. **Describe Table to Confirm Structure:**
    ```sql
    DESCRIBE Coordinates;
    ```

---

## Insert Sample Data

1. **Insert Data:**
    ```sql
    INSERT INTO Coordinates (latitude, longitude) VALUES (8.5931, 76.8938);
    ```

2. **View Data:**
    ```sql
    SELECT * FROM Coordinates;
    ```

---

## Connecting to Database via Python

1. **Install MySQL Connector:**
    ```bash
    pip install mysql-connector-python
    ```

2. **Sample Python Script to Insert Data:**
    ```python
    import mysql.connector

    # Establish Connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="GPS"
    )

    cursor = conn.cursor()

    # Insert Data
    query = "INSERT INTO Coordinates (latitude, longitude) VALUES (%s, %s)"
    data = (8.5613, 76.8767)
    cursor.execute(query, data)
    conn.commit()

    print("Data Inserted Successfully")

    # Close Connection
    conn.close()
    ```

---

## Export and Backup the Database

1. **Export Database to a File:**
    ```bash
    mysqldump -u root -p GPS > gps_backup.sql
    ```

2. **Restore Database from a File:**
    ```bash
    mysql -u root -p GPS < gps_backup.sql
    ```

---

## Additional Notes

- Ensure proper privileges are set for remote connections if required.
- Use secure passwords and follow best practices for database security.

