CREATE DATABASE IF NOT EXISTS inventory;

use inventory;

CREATE TABLE items (
item_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE stock (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items(item_id) ON DELETE CASCADE
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    price_per_item DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES items(item_id) ON DELETE CASCADE
);


create table stock_shipment( 
    stock_shipment_id int AUTO_INCREMENT PRIMARY KEY, 
    stock_id int NOT NULL, 
    shipment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    item_id int NOT NULL, 
    quantity int NOT NULL, 
    FOREIGN KEY (stock_id) REFERENCES stock(stock_id) ON DELETE CASCADE, 
    FOREIGN KEY (item_id) REFERENCES items(item_id) ON DELETE CASCADE  
);

