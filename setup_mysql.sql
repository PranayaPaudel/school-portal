-- MySQL Initialization Script for Gurukul Bidhya Sadan Secondary School Portal
-- Run as root: sudo mysql < setup_mysql.sql

CREATE DATABASE IF NOT EXISTS gurukul_school CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'gurukul_user'@'localhost' IDENTIFIED BY 'gurukul123';
ALTER USER 'gurukul_user'@'localhost' IDENTIFIED BY 'gurukul123';
GRANT ALL PRIVILEGES ON gurukul_school.* TO 'gurukul_user'@'localhost';
FLUSH PRIVILEGES;
