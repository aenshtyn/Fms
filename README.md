
# Farm Management System

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [User Roles and Journeys](#user-roles-and-journeys)
    - [Farm Owner](#farm-owner)
    - [Farm Manager](#farm-manager)
    - [Shareholder](#shareholder)
5. [Features](#features)
6. [Concepts](#concepts)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction
A brief introduction to the farm management system, its purpose, and key functionalities.

## Installation
Instructions on how to set up the development environment, install dependencies, and run the application.

## Usage
Basic usage instructions, including how to log in and navigate the system.

## User Roles and Journeys

### Farm Owner
#### User Journey:
1. **Sign Up / Login**:
    - Sign up with email and password or log in if already registered.
    - Provide necessary farm details during registration, including subdomain preference.

2. **Dashboard Access**:
    - Directed to the farm-specific dashboard (e.g., kajidofarm.farmsync.co.ke).
    - Displays a comprehensive overview of all farm operations, including livestock, crops, finances, and inventory.

3. **Manage Farm Managers**:
    - Add farm managers by entering their email addresses, triggering an invitation email.
    - View the list of existing managers and remove any if necessary.

4. **Input and Manage Records**:
    - Access pages to input and manage records for livestock, crops, finances, and inventory.
    - Ability to add, edit, and delete records.

5. **View Detailed Reports and Analytics**:
    - Access detailed reports and analytics, including milk production, feed consumption, crop yield, financial statements, and inventory levels.
    - Filter and customize the reports as needed.

6. **Notifications and Alerts**:
    - Receive notifications and alerts for critical events, such as low inventory levels, upcoming maintenance, and health alerts for livestock.

### Farm Manager
#### User Journey:
1. **Invitation and Registration**:
    - Receive an email invitation from the farm owner.
    - Register on the platform using the invitation link, setting up their account with a password.

2. **Login and Dashboard Access**:
    - Log in to the platform and directed to the farm-specific dashboard.
    - Provides an overview of the farm's operations relevant to their role.

3. **Input and Manage Records**:
    - Navigate to pages for inputting and managing records.
    - Add, edit, and delete records for livestock, crops, finances, and inventory.

4. **View Reports and Analytics**:
    - Access relevant reports and analytics for their responsibilities.
    - View detailed data on milk production, feed consumption, crop yield, and more.

5. **Notifications and Alerts**:
    - Receive notifications and alerts for tasks and critical events related to their duties.

### Shareholder
#### User Journey:
1. **Invitation and Registration**:
    - Receive an email invitation from the farm owner.
    - Register on the platform using the invitation link, setting up their account with a password.

2. **Login and Dashboard Access**:
    - Log in to the platform and directed to the farm-specific dashboard.
    - Displays an overview of farm performance and key metrics.

3. **View Reports and Analytics**:
    - Access selected reports and analytics relevant to their interests.
    - View summarized data on milk production, crop yield, financial performance, and inventory levels.

4. **Notifications and Alerts**:
    - Receive notifications and alerts for important updates, such as financial reports and major changes in farm operations.

## Features
- **Multi-Tenancy**: Support for multiple farms with unique subdomains.
- **Comprehensive Dashboards**: Real-time data and analytics.
- **User Management**: Roles and permissions for farm owners, managers, and shareholders.
- **Record Management**: Input and manage records for livestock, crops, finances, and inventory.
- **Notifications and Alerts**: Automated alerts for critical events and tasks.

## Concepts
- **Multi-Tenancy**: Isolating data for different farms using unique subdomains.
- **Angular Services and Interceptors**: Managing HTTP requests and authentication.
- **Role-Based Access Control (RBAC)**: Defining permissions based on user roles.
- **Data Aggregation and Analytics**: Summarizing and analyzing farm data.

## Contributing

## License
