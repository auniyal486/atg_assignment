CREATE DATABASE db;-- create database 
USE db;-- select db database for executing all below queries. 
CREATE TABLE JobType1(
	id INT AUTO_INCREMENT PRIMARY KEY,
    Category VARCHAR(256) UNIQUE
);-- create jobtype1 table
CREATE TABLE JobType2(
	id INT AUTO_INCREMENT PRIMARY KEY,
    Category VARCHAR(256),
    Subcategory VARCHAR(256) UNIQUE,
    FOREIGN KEY (Category) REFERENCES JobType1(Category)
);-- create jobtype2 table
CREATE TABLE States(
	id INT AUTO_INCREMENT PRIMARY KEY,
    State VARCHAR(256) UNIQUE
);-- create states table
CREATE TABLE CompanyDetails(
	id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(256) UNIQUE,
    Field VARCHAR(256),
    Headquarters VARCHAR(256),
    Description VARCHAR(2000),
    UNIQUE(Name,Field)
);-- create companydetails table
CREATE TABLE Jobs(
	id INT AUTO_INCREMENT PRIMARY KEY,
    Company VARCHAR(256),
    JobPosition VARCHAR(256),
    Location VARCHAR(256),
    WorkType VARCHAR(256),
    State VARCHAR(256),
    Subcategory VARCHAR(256),
    UNIQUE(Company,JobPosition),
    FOREIGN KEY (State) REFERENCES States(State),
    FOREIGN KEY (Company) REFERENCES CompanyDetails(Name),
    FOREIGN KEY (Subcategory) REFERENCES JobType2(Subcategory)
);-- create jobs table 
 