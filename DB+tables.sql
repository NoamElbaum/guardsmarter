CREATE SCHEMA `guardsmarter` ;

CREATE TABLE `residents` (
  `ID` int NOT NULL,
  `car_num` int DEFAULT NULL,
  `pic` longblob NOT NULL,
  `f_name` varchar(45) NOT NULL,
  `l_name` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
);

  
 CREATE TABLE `entries_log` (
  `time` datetime NOT NULL,
  `car_num` int NOT NULL,
  `driver_name` varchar(80) NOT NULL,
  `driver_id` int NOT NULL,
  PRIMARY KEY (`time`)
);
