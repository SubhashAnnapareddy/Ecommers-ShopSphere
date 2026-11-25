# Django E-Commerce Website

## Project Overview

This is a web-based E-commerce application developed using **Python and Django**. It provides an online shopping platform where users can browse products, view product details, and manage orders.

The application includes product management, inventory management, and database integration to handle essential e-commerce operations.

## Features

- **Product Listing:** Display available products with relevant details.
- **Product Details:** View individual product information.
- **Inventory Management:** Manage product and stock information.
- **Order Management:** Handle customer orders and order-related information.
- **Database Integration:** Store and manage product and order data.
- **Responsive Frontend:** User interface developed using HTML, CSS, and JavaScript.

## Technologies Used

| Category | Technologies |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| Tools | VS Code, Git, GitHub |


### 2. Navigate to the Project Directory

```bash
cd ecommerce-project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Future Enhancements

- Online payment gateway integration.
- Advanced product search and filtering.
- Shopping cart improvements.
- Order tracking.
- User authentication and profile management.


---

*This project was developed to gain practical experience in Django web development, database integration, and building e-commerce applications.*
