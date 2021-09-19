CREATE TABLE `Work_Types` (
  `work_type_id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`work_type_id`)
) 

INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (1,'Duo');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (2,'Duet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (3,'Trio');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (4,'Quartet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (5,'Quintet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (6,'Sexet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (7,'Septet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (8,'Octet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (9,'Nonet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (10,'Decet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (11,'String Trio');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (12,'String Quartet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (13,'String Quintet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (14,'String Sextet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (15,'Piano Trio');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (16,'Piano Quartet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (17,'Piano Quintet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (18,'Blank');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (19,'Clarinet Trio');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (20,'Clarinet Quartet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (21,'Clarinet Quintet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (22,'Duo Sonata');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (23,'Trio Sonata');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (24,'Violin Sonata');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (25,'Cello Sonata');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (26,'Viola Sonata');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (27,'Horn Sonata');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (28,'Bassoon Sonata');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (29,'Clarinet Sonata');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (30,'Flute Sonata');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (31,'Horn Quintet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (32,'Flute Quartet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (33,'Oboe Quartet');
INSERT INTO `Work_Types` (`work_type_id`,`description`) VALUES (34,'String Duo');

--ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
