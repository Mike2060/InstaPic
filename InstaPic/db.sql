CREATE DATABASE IF NOT EXISTS `heroku_5a73ef4f1809026` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `heroku_5a73ef4f1809026`;

CREATE TABLE IF NOT EXISTS `accounts` (
	id int(11) NOT NULL AUTO_INCREMENT,
  	password varchar(255) NOT NULL,
  	username varchar(50) NOT NULL UNIQUE,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `images` (
	id int(11) NOT NULL AUTO_INCREMENT,
		imageID int(11) NOT NULL,
		content TEXT,
		time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	username varchar(50) NOT NULL,
		extention varchar(50) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO accounts (id, password, username) VALUES (1, 'test', 'test');
