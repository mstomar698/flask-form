-- CREATE DATABASE IF NOT EXISTS `form_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
-- USE `form_db`;

-- CREATE TABLE IF NOT EXISTS `form` (
--     `id` int(11) NOT NULL AUTO_INCREMENT,
--     `username` varchar(50) NOT NULL,
--     `password` varchar(255) NOT NULL,
--     `email` varchar(100) NOT NULL,
--     PRIMARY KEY (`id`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- INSERT INTO `form` (`id`, `username`, `password`, `email`) VALUES (1, 'test', '1234', 'test@test.com');

-- show databases;
-- show tables;
-- select *  from form ;  
use form_db;
select * from form;