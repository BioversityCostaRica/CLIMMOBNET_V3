-- MySQL dump 10.15  Distrib 10.0.21-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: climmobv3
-- ------------------------------------------------------
-- Server version	10.0.21-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activitylog`
--

DROP TABLE IF EXISTS `activitylog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `activitylog` (
  `log_id` int(9) NOT NULL AUTO_INCREMENT,
  `log_user` varchar(80) NOT NULL,
  `log_datetime` datetime DEFAULT NULL,
  `log_type` varchar(3) DEFAULT NULL,
  `log_message` text,
  PRIMARY KEY (`log_id`),
  KEY `fk_activitylog_user1_idx` (`log_user`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activitylog`
--

LOCK TABLES `activitylog` WRITE;
/*!40000 ALTER TABLE `activitylog` DISABLE KEYS */;
INSERT INTO `activitylog` VALUES (1,'qlands','2016-02-16 23:12:29','PRF','Welcome to Climmob'),(2,'qlands','2016-02-16 23:14:02','PRF','Updated profile');
/*!40000 ALTER TABLE `activitylog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apilog`
--

DROP TABLE IF EXISTS `apilog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apilog` (
  `log_id` int(9) NOT NULL AUTO_INCREMENT,
  `log_datetime` datetime DEFAULT NULL,
  `log_ip` varchar(45) DEFAULT NULL,
  `log_user` varchar(80) NOT NULL,
  `log_uuid` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `fk_apilog_user1_idx` (`log_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apilog`
--

LOCK TABLES `apilog` WRITE;
/*!40000 ALTER TABLE `apilog` DISABLE KEYS */;
/*!40000 ALTER TABLE `apilog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `country` (
  `cnty_cod` varchar(3) NOT NULL,
  `cnty_name` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`cnty_cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES ('CRC','Costa Rica'),('KE','Kenya'),('USA','United States of America');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crop`
--

DROP TABLE IF EXISTS `crop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `crop` (
  `crop_id` int(11) NOT NULL AUTO_INCREMENT,
  `crop_name` varchar(45) DEFAULT NULL,
  `user_name` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`crop_id`),
  KEY `fk_crop_user1_idx` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crop`
--

LOCK TABLES `crop` WRITE;
/*!40000 ALTER TABLE `crop` DISABLE KEYS */;
/*!40000 ALTER TABLE `crop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enumerator`
--

DROP TABLE IF EXISTS `enumerator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enumerator` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `enum_id` varchar(80) NOT NULL,
  `enum_name` varchar(120) DEFAULT NULL,
  `enum_password` varchar(80) DEFAULT NULL,
  `enum_active` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`user_name`,`project_cod`,`enum_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enumerator`
--

LOCK TABLES `enumerator` WRITE;
/*!40000 ALTER TABLE `enumerator` DISABLE KEYS */;
/*!40000 ALTER TABLE `enumerator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `i18n`
--

DROP TABLE IF EXISTS `i18n`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `i18n` (
  `lang_code` varchar(5) NOT NULL,
  `lang_name` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`lang_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `i18n`
--

LOCK TABLES `i18n` WRITE;
/*!40000 ALTER TABLE `i18n` DISABLE KEYS */;
/*!40000 ALTER TABLE `i18n` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `package`
--

DROP TABLE IF EXISTS `package`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `package` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `package_id` int(11) NOT NULL,
  `varietya_user` varchar(80) NOT NULL,
  `varietya_project` varchar(80) NOT NULL,
  `varietya_variety` int(11) NOT NULL,
  `varietyb_user` varchar(80) NOT NULL,
  `varietyb_project` varchar(80) NOT NULL,
  `varietyb_variety` int(11) NOT NULL,
  `varietyc_user` varchar(80) NOT NULL,
  `varietyc_project` varchar(80) NOT NULL,
  `varietyc_variety` int(11) NOT NULL,
  PRIMARY KEY (`user_name`,`project_cod`,`package_id`),
  KEY `fk_package_prjvariety1_idx` (`varietya_user`,`varietya_project`,`varietya_variety`),
  KEY `fk_package_prjvariety2_idx` (`varietyb_user`,`varietyb_project`,`varietyb_variety`),
  KEY `fk_package_prjvariety3_idx` (`varietyc_user`,`varietyc_project`,`varietyc_variety`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `package`
--

LOCK TABLES `package` WRITE;
/*!40000 ALTER TABLE `package` DISABLE KEYS */;
/*!40000 ALTER TABLE `package` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prjquestion`
--

DROP TABLE IF EXISTS `prjquestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prjquestion` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `question_id` int(11) NOT NULL,
  `added_date` datetime DEFAULT NULL,
  PRIMARY KEY (`user_name`,`project_cod`,`question_id`),
  KEY `fk_projectquestion_question1_idx` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prjquestion`
--

LOCK TABLES `prjquestion` WRITE;
/*!40000 ALTER TABLE `prjquestion` DISABLE KEYS */;
/*!40000 ALTER TABLE `prjquestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prjvariety`
--

DROP TABLE IF EXISTS `prjvariety`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prjvariety` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `variety_id` int(11) NOT NULL,
  `variety_name` varchar(120) DEFAULT NULL,
  `source_crop` int(11) DEFAULT NULL,
  `source_variety` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_name`,`project_cod`,`variety_id`),
  KEY `fk_prjvariety_variety1_idx` (`source_crop`,`source_variety`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prjvariety`
--

LOCK TABLES `prjvariety` WRITE;
/*!40000 ALTER TABLE `prjvariety` DISABLE KEYS */;
/*!40000 ALTER TABLE `prjvariety` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `user_name` varchar(80) NOT NULL,
  `project_cod` varchar(80) NOT NULL,
  `project_name` varchar(120) DEFAULT NULL,
  `project_abstract` text,
  `project_tags` text,
  `project_pi` varchar(120) DEFAULT NULL,
  `project_piemail` varchar(120) DEFAULT NULL,
  `project_cnty` varchar(3) NOT NULL,
  `project_crop` int(11) NOT NULL,
  `project_lang` varchar(5) NOT NULL,
  PRIMARY KEY (`user_name`,`project_cod`),
  KEY `fk_project_lkpcountry1_idx` (`project_cnty`),
  KEY `fk_project_user1_idx` (`user_name`),
  KEY `fk_project_crop1_idx` (`project_crop`),
  KEY `fk_project_i18n1_idx` (`project_lang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qstoption`
--

DROP TABLE IF EXISTS `qstoption`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `qstoption` (
  `question_id` int(11) NOT NULL,
  `value_code` int(11) NOT NULL,
  `value_desc` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`question_id`,`value_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qstoption`
--

LOCK TABLES `qstoption` WRITE;
/*!40000 ALTER TABLE `qstoption` DISABLE KEYS */;
/*!40000 ALTER TABLE `qstoption` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_desc` varchar(120) DEFAULT NULL,
  `question_notes` text,
  `question_unit` varchar(120) DEFAULT NULL,
  `question_type` int(11) DEFAULT NULL,
  `question_dtype` int(11) DEFAULT NULL,
  `user_name` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`question_id`),
  KEY `fk_question_user1_idx` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `response`
--

DROP TABLE IF EXISTS `response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `response` (
  `submission_uuid` varchar(80) NOT NULL,
  `resp_uuid` varchar(80) NOT NULL,
  `prjuser_name` varchar(80) NOT NULL,
  `prjproject_cod` varchar(80) NOT NULL,
  `question_id` int(11) NOT NULL,
  `resp_intvalue` int(11) DEFAULT NULL,
  `resp_decvalue` decimal(11,3) DEFAULT NULL,
  `resp_datevalue` datetime DEFAULT NULL,
  `resp_txtvalue` text,
  `resp_question` int(11) DEFAULT NULL,
  `resp_value` int(11) DEFAULT NULL,
  `resp_variety_user` varchar(80) DEFAULT NULL,
  `resp_variety_project` varchar(80) DEFAULT NULL,
  `resp_variety_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`submission_uuid`,`resp_uuid`),
  KEY `fk_response_projectquestion1_idx` (`prjuser_name`,`prjproject_cod`,`question_id`),
  KEY `fk_response_qstoption1_idx` (`resp_question`,`resp_value`),
  KEY `fk_response_prjvariety1_idx` (`resp_variety_user`,`resp_variety_project`,`resp_variety_id`),
  KEY `fk_response_submission1_idx` (`submission_uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `response`
--

LOCK TABLES `response` WRITE;
/*!40000 ALTER TABLE `response` DISABLE KEYS */;
/*!40000 ALTER TABLE `response` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sector`
--

DROP TABLE IF EXISTS `sector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sector` (
  `sector_cod` int(11) NOT NULL AUTO_INCREMENT,
  `sector_name` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`sector_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sector`
--

LOCK TABLES `sector` WRITE;
/*!40000 ALTER TABLE `sector` DISABLE KEYS */;
INSERT INTO `sector` VALUES (1,'Private'),(2,'Goverment'),(3,'Research');
/*!40000 ALTER TABLE `sector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `submission`
--

DROP TABLE IF EXISTS `submission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `submission` (
  `submission_uuid` varchar(80) NOT NULL,
  `submission_date` datetime DEFAULT NULL,
  `submission_source` varchar(45) DEFAULT NULL,
  `submission_sourceuuid` varchar(80) DEFAULT NULL,
  `enum_user` varchar(80) NOT NULL,
  `enum_project` varchar(80) NOT NULL,
  `enum_id` varchar(80) NOT NULL,
  `package_user` varchar(80) NOT NULL,
  `package_project` varchar(80) NOT NULL,
  `package_id` int(11) NOT NULL,
  PRIMARY KEY (`submission_uuid`),
  KEY `fk_submission_enumerator1_idx` (`enum_user`,`enum_project`,`enum_id`),
  KEY `fk_submission_package1_idx` (`package_user`,`package_project`,`package_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `submission`
--

LOCK TABLES `submission` WRITE;
/*!40000 ALTER TABLE `submission` DISABLE KEYS */;
/*!40000 ALTER TABLE `submission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_name` varchar(80) NOT NULL,
  `user_fullname` varchar(120) DEFAULT NULL,
  `user_password` varchar(80) DEFAULT NULL,
  `user_organization` varchar(120) DEFAULT NULL,
  `user_email` varchar(120) DEFAULT NULL,
  `user_apikey` varchar(45) DEFAULT NULL,
  `user_about` text,
  `user_cnty` varchar(3) NOT NULL,
  `user_sector` int(11) NOT NULL,
  `user_active` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`user_name`),
  KEY `fk_user_lkpcountry_idx` (`user_cnty`),
  KEY `fk_user_lkpsector1_idx` (`user_sector`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('qlands','Carlos Quiros Campos','kGfkeS+s9sDQ1W8cvpieQw==','Bioversity','cquiros@qlands.com','f18f9bee-bae5-4346-8bf1-d959d4690445','Yo soy Carlos Quiros','CRC',3,1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variety`
--

DROP TABLE IF EXISTS `variety`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `variety` (
  `crop_id` int(11) NOT NULL,
  `variety_id` int(11) NOT NULL,
  `variety_name` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`crop_id`,`variety_id`),
  KEY `fk_variety_crop1_idx` (`crop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variety`
--

LOCK TABLES `variety` WRITE;
/*!40000 ALTER TABLE `variety` DISABLE KEYS */;
/*!40000 ALTER TABLE `variety` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-02-16 23:15:23
