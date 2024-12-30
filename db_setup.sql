CREATE DATABASE online_food_ordering;

USE online_food_ordering;

-- Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    address TEXT NOT NULL
);

-- Food Items Table
CREATE TABLE food_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    availability BOOLEAN DEFAULT TRUE
);

-- Orders Table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order Items Table
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES food_items(item_id)
);

-- Sample Data for Food Items
INSERT INTO food_items (name, category, price, availability)
VALUES 
('Pizza', 'Main Course', 299.99, TRUE),
('Burger', 'Snacks', 149.99, TRUE),
('Coke', 'Beverage', 49.99, TRUE),
('Pasta', 'Main Course', 199.99, TRUE),
('Ice Cream', 'Dessert', 99.99, TRUE),
('Chicken Wings', 'Snacks', 249.99, TRUE),
('Tacos', 'Main Course', 179.99, TRUE),
('Milkshake', 'Beverage', 99.99, TRUE),
('Brownie', 'Dessert', 129.99, TRUE),
('Garlic Bread', 'Snacks', 99.99, TRUE),
('Salad', 'Appetizer', 149.99, TRUE),
('Fried Rice', 'Main Course', 199.99, TRUE),
('Spring Rolls', 'Appetizer', 149.99, TRUE),
('Orange Juice', 'Beverage', 59.99, TRUE),
('Cheesecake', 'Dessert', 159.99, TRUE),
('Maggie', 'Main Course', 129.99, TRUE),
('Cold Coffee', 'Beverage', 99.99, TRUE),
('Grill Sandwich', 'Snacks', 49.99, TRUE),
('Cup Cakes', 'Dessert', 99.99, TRUE),
('Noodles', 'Main Course', 179.99, TRUE);

SELECT * FROM food_items;
