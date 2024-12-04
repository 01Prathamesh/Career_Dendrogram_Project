# Career Dendrogram  Project
A Career Guidance Application for Students.

## Overview

Career Dendrogram is a Django web application that visualizes career paths and roles, helping users explore various career options. The application allows users to manage their profiles, add and edit career paths, and visualize these paths in a dendrogram format.


## Features

- User account management (registration, login, profile editing)
- CRUD operations for career paths and roles
- Visualization of career paths using a dendrogram
- Responsive design for a seamless user experience


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/01Prathamesh/Career_Dendrogram_Project.git
   cd Career_Dendrogram_Project

2. **Create a virtual environment:**

   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**

   ```bash
    pip install -r requirements.txt

4. **Run migrations:**

   ```bash
   python manage.py migrate

5. **Run the development server:**

   ```bash
   python manage.py runserver

6. **Access the application:**

    Open your web browser and navigate to http://127.0.0.1:8000/.


## Usage

- User Registration: Go to the registration page to create a new account.
- Profile Management: Users can edit their profiles after logging in.
- Manage Career Paths: Add, edit, or delete career paths and roles.
- Dendrogram Visualization: View the career paths in a visual format.


## Technologies Used

- Django
- SQLite (for development)
- HTML/CSS
- JavaScript (for dendrogram visualization)


## Contributing

- Contributions are welcome! Please fork the repository and submit a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.


## Acknowledgments

- Thank you to the Django community for the fantastic framework.
- Inspiration from various career exploration tools.
