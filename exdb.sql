/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.1.32-community : Database - exam
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`exam` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `exam`;

/*Table structure for table `courses` */

DROP TABLE IF EXISTS `courses`;

CREATE TABLE `courses` (
  `Course_id` int(11) NOT NULL AUTO_INCREMENT,
  `Course_name` varchar(25) DEFAULT NULL,
  `Duration` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `courses` */

insert  into `courses`(`Course_id`,`Course_name`,`Duration`) values (1,'B.A. (English Literature)','3 Year'),(2,'M.A. (English Literature)','2 Year'),(7,'M.S.W','2 Year'),(8,'bcom','3 year'),(9,'mca','3 yrs'),(10,'msc','3 year'),(11,'Physics','3');

/*Table structure for table `dept` */

DROP TABLE IF EXISTS `dept`;

CREATE TABLE `dept` (
  `Dept_no` int(11) NOT NULL AUTO_INCREMENT,
  `Dept_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Dept_no`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `dept` */

insert  into `dept`(`Dept_no`,`Dept_name`) values (8,'hffffddseereree');

/*Table structure for table `ec_reg` */

DROP TABLE IF EXISTS `ec_reg`;

CREATE TABLE `ec_reg` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `First_name` varchar(25) DEFAULT NULL,
  `Last_name` varchar(25) DEFAULT NULL,
  `Address` varchar(150) DEFAULT NULL,
  `Dob` date DEFAULT NULL,
  `Qualification` varchar(50) DEFAULT NULL,
  `Phone` int(11) DEFAULT NULL,
  `Email` varchar(25) DEFAULT NULL,
  `Post` varchar(30) DEFAULT NULL,
  `Doj` date DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ec_reg` */

/*Table structure for table `exam_add` */

DROP TABLE IF EXISTS `exam_add`;

CREATE TABLE `exam_add` (
  `Exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `Exam_Name` varchar(50) NOT NULL,
  `Course` varchar(50) NOT NULL,
  `Subject` varchar(50) NOT NULL,
  `Date` date NOT NULL,
  `publish` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `exam_add` */

insert  into `exam_add`(`Exam_id`,`Exam_Name`,`Course`,`Subject`,`Date`,`publish`) values (1,'first semester exam','2','6','2019-02-23','published'),(2,'third internal exam','2','7','2019-04-28','pending'),(3,'3rd Semster Exam','2','8','2019-08-09','pending'),(4,'second sem','1','1','2019-04-17','pending'),(5,'bdef','1','1','2019-04-29','pending'),(6,'abcd','9','2','2019-04-17','pending');

/*Table structure for table `examc_reg` */

DROP TABLE IF EXISTS `examc_reg`;

CREATE TABLE `examc_reg` (
  `id` int(11) NOT NULL,
  `first_name` varchar(25) DEFAULT NULL,
  `last_name` varchar(25) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(25) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `phone` bigint(15) DEFAULT NULL,
  `Email` varchar(25) DEFAULT NULL,
  `post` varchar(25) DEFAULT NULL,
  `doj` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `examc_reg` */

insert  into `examc_reg`(`id`,`first_name`,`last_name`,`address`,`dob`,`gender`,`qualification`,`phone`,`Email`,`post`,`doj`) values (13,'Abhilash','Mehra','abi villa,trissur','2019-04-09','Male','PhD',9878986543,'abi@gmail.com','trissur','2019-04-10');

/*Table structure for table `hall_ticket` */

DROP TABLE IF EXISTS `hall_ticket`;

CREATE TABLE `hall_ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `month_year` varchar(50) NOT NULL,
  `hall_ticket` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `hall_ticket` */

insert  into `hall_ticket`(`id`,`student_id`,`month_year`,`hall_ticket`,`status`) values (1,1,'april 2018','hall1.jpg','pending'),(2,2,'april 2019','hall2.jpg','pending'),(3,3,'march 2018','hall1.jpg','pending'),(4,17,'march 2018','hall2.jpg','approved'),(5,1,'January 2015','hall2.jpg','pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `User_name` varchar(25) DEFAULT NULL,
  `Password` varchar(25) DEFAULT NULL,
  `Type` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Id`,`User_name`,`Password`,`Type`) values (2,'anju','123456','student'),(3,'arun','arun@gmail.com','reject'),(4,'devagiri','devagiri','devagiri'),(6,'athira','athi@gmail.com','pending'),(13,'Abhilash','9878986543','controller'),(14,'anu','9567890987','staff'),(17,'mridu@gmail.com','9870987654','student'),(18,NULL,NULL,NULL);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Date` date DEFAULT NULL,
  `Notification` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`Id`,`Date`,`Notification`) values (1,'2018-05-12','university exam'),(2,'2019-04-07','second semester exam'),(3,'2018-09-09','aaassdsdfggggg'),(4,'2019-04-10','jkkkkkkkkkkkkkkk'),(5,'2019-04-30','Exam scheduled on 30 april 2019');

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `Qid` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(25) NOT NULL,
  `Question` varchar(1000) NOT NULL,
  `Answer` varchar(1000) NOT NULL,
  `Mark` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`Qid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `question` */

insert  into `question`(`Qid`,`exam_id`,`Question`,`Answer`,`Mark`,`status`) values (1,1,'What is java?','Programming language',10,'approved'),(2,1,'Exception handing?','Error handling',5,'approved'),(3,2,'Platform Independent','Yes',5,'pending'),(4,2,'JIT','Yes',23,'approved'),(5,1,'Founder of java?','James Gosling',5,'approved'),(6,2,'Explain Java','Platform independent',4,'pending');

/*Table structure for table `staff_reg` */

DROP TABLE IF EXISTS `staff_reg`;

CREATE TABLE `staff_reg` (
  `Staff_id` int(11) NOT NULL,
  `First_name` varchar(25) DEFAULT NULL,
  `Last_name` varchar(25) DEFAULT NULL,
  `Father_name` varchar(25) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Gender` varchar(25) DEFAULT NULL,
  `Dob` date DEFAULT NULL,
  `Qualificartion` varchar(25) DEFAULT NULL,
  `Doj` date DEFAULT NULL,
  `Phone` bigint(25) DEFAULT NULL,
  `Email` varchar(25) DEFAULT NULL,
  `Post` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `staff_reg` */

insert  into `staff_reg`(`Staff_id`,`First_name`,`Last_name`,`Father_name`,`Address`,`Gender`,`Dob`,`Qualificartion`,`Doj`,`Phone`,`Email`,`Post`) values (14,'anu','ravi','Ravi pillai','anu villa, Kozhikode','Female','2019-04-10','PG','2019-04-04',9567890987,'anu@gmail.com','Tutor');

/*Table structure for table `std_reg` */

DROP TABLE IF EXISTS `std_reg`;

CREATE TABLE `std_reg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Reg_no` int(11) DEFAULT NULL,
  `First_Name` varchar(25) DEFAULT NULL,
  `Last_Name` varchar(25) DEFAULT NULL,
  `Father_Name` varchar(25) DEFAULT NULL,
  `Dob` date DEFAULT NULL,
  `Gender` varchar(25) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `District` varchar(25) DEFAULT NULL,
  `Pincode` int(25) DEFAULT NULL,
  `State` varchar(25) DEFAULT NULL,
  `Nationality` varchar(25) DEFAULT NULL,
  `Qualification` varchar(50) DEFAULT NULL,
  `Phone_number` bigint(11) DEFAULT NULL,
  `Email` varchar(25) DEFAULT NULL,
  `Course` varchar(25) DEFAULT NULL,
  `sem` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `std_reg` */

insert  into `std_reg`(`id`,`Reg_no`,`First_Name`,`Last_Name`,`Father_Name`,`Dob`,`Gender`,`Address`,`District`,`Pincode`,`State`,`Nationality`,`Qualification`,`Phone_number`,`Email`,`Course`,`sem`) values (2,123,'anju','raju','raju','1994-06-23','radio2','calicut','kannur',1233454,'kerala','indian','on',123545666,'anju@gmail.com','2','2'),(3,1289,'arun','kumar','kumar','1994-06-23','Male','calicut','calicut',134566,'kerala','indian','on',2354566,'arun@gmail.com','2','3'),(6,1899,'Athira','v','vinod','1995-05-16','Female','palakkad','wayanad',134455,'kerala','indian','Degree',1234676,'athira@gmail.com','1','5'),(17,6787654,'Mridhula','Ravi','Raveendran','2019-04-11','Male','Mridula villa,Kotooli','Kozhikode',786576,'Kerala','Indian','Plus Two,Degree',9870987654,'mridu@gmail.com','2','2');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Course_id` int(11) DEFAULT NULL,
  `sem` varchar(25) DEFAULT NULL,
  `Subject` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`id`,`Course_id`,`sem`,`Subject`) values (1,2,'1','Communication Skills in E'),(2,2,'1','Critical Reasoning, Writi'),(3,2,'1','Communication Skill in th'),(4,2,'1','Methodology of Humanities'),(5,2,'2','Reading Literature in Eng'),(6,7,'2','Readings on Indian Consti'),(7,7,'2','Translation and communica'),(8,7,'2','Methodology of Literature'),(9,8,'3','Literature and Contempora'),(10,8,'3','Literature in the additio'),(11,8,'3','Informatics'),(12,8,'3','Reading Prose'),(13,9,'4','History and Philosophy of'),(14,9,'4','Culture and Civilization'),(15,9,'4','Reading Poetry'),(16,9,'4','Reading Fiction'),(17,9,'5','Reading Drama'),(18,10,'5','Language and Linguistics'),(19,10,'5','Literary Criticism and Th'),(20,10,'5','Literature in English:Ame'),(21,10,'6','Womens Writing'),(22,11,'6','Modern English Literature'),(23,11,'6','Indian Writing in English'),(24,11,'6','Writing for the Media'),(25,11,'1','Communication Skills in E'),(26,1,'2','Communication Skills in E'),(27,1,'2','maths'),(28,1,'4','mm'),(29,1,'1','Thermodynamics');

/*Table structure for table `timetable` */

DROP TABLE IF EXISTS `timetable`;

CREATE TABLE `timetable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) NOT NULL,
  `sem` int(11) NOT NULL,
  `time_table` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `timetable` */

insert  into `timetable`(`id`,`course_id`,`sem`,`time_table`) values (1,1,1,'result_ACE.pdf'),(2,6,4,'result_ASI.pdf'),(3,6,3,'result_AAP.pdf');

/*Table structure for table `write_exam` */

DROP TABLE IF EXISTS `write_exam`;

CREATE TABLE `write_exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stud_id` int(11) NOT NULL,
  `examid` int(11) DEFAULT NULL,
  `ques_id` int(11) NOT NULL,
  `Answer` varchar(500) NOT NULL,
  `Mark` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `write_exam` */

insert  into `write_exam`(`id`,`stud_id`,`examid`,`ques_id`,`Answer`,`Mark`) values (1,2,1,1,'Programming language','10'),(2,2,1,2,'error','7'),(3,2,1,5,'James','10'),(4,2,2,3,'No','7'),(5,2,2,4,'Yes','10'),(6,2,2,6,'platform independent','7'),(7,17,1,1,'language','10'),(8,17,1,2,'Yes','7'),(9,17,1,5,'James Gosling','10');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
