CREATE DATABASE tracknap;
USE tracknap;
CREATE TABLE login (
	id int(11) NOT NULL AUTO_INCREMENT,
	fullname varchar(200) NOT NULL,
	username varchar(100) NOT NULL,
	email varchar(100) NOT NULL,
	password varchar(100) NOT NULL,
	cpassword varchar(100) NOT NULL,
	PRIMARY KEY (id),
    PRIMARY KEY(username)
);
CREATE TABLE record (
    sno int(11) NOT NULL AUTO_INCREMENT,
    username varchar(100) NOT NULL,
    date date NOT NULL,
    bedtime time NOT NULL,
    wakeuptime time NOT NULL,
    PRIMARY KEY(sno)
);