CREATE SCHEMA `guardsmarter` ;

CREATE TABLE `residents` (
  `ID` int NOT NULL,
  `car_num` int DEFAULT NULL,
  `pic` longblob NOT NULL,
  `f_name` varchar(45) NOT NULL,
  `l_name` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
);

  
  CREATE TABLE `guardsmarter`.`entries_log` (
  `time` DATETIME NOT NULL,
  `car_num` INT NULL,
  `driver_name` VARCHAR(45) NULL,
  `driver_id` INT NULL,
  PRIMARY KEY (`time`));