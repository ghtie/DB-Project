-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: eecslab-9.case.edu    Database: team_17
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

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
-- Table structure for table `guest_user`
--

DROP TABLE IF EXISTS `guest_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `guest_user` (
  `ID` int(10) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest_user`
--

LOCK TABLES `guest_user` WRITE;
/*!40000 ALTER TABLE `guest_user` DISABLE KEYS */;
INSERT INTO `guest_user` VALUES (0,'dsh108'),(1,'bgb31'),(2,'hst51'),(3,'mjl198'),(4,'dsh108'),(5,'mjl198'),(6,'bgb31');
/*!40000 ALTER TABLE `guest_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swipes`
--

DROP TABLE IF EXISTS `swipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `swipes` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `price` decimal(10,2) NOT NULL,
  `quantity` int(5) NOT NULL,
  `user_id` varchar(10) DEFAULT NULL,
  `guest_user_id` int(5) DEFAULT NULL,
  `status` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`),
  KEY `guest_user_id` (`guest_user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `swipes_ibfk_2` FOREIGN KEY (`guest_user_id`) REFERENCES `guest_user` (`ID`),
  CONSTRAINT `swipes_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swipes`
--

LOCK TABLES `swipes` WRITE;
/*!40000 ALTER TABLE `swipes` DISABLE KEYS */;
INSERT INTO `swipes` VALUES (90,20.00,4,'dsh108',0,1),(91,40.00,10,'dsh108',0,1),(92,20.00,4,'ght8',NULL,0),(93,15.00,3,'dbr211',1,1),(94,49.00,7,'dbr211',NULL,0),(95,30.00,6,'jys10',4,1),(96,12.00,12,'jys10',3,1),(97,10.00,5,'jys10',2,1),(98,20.00,4,'dsh108',NULL,0),(99,100000.00,1,'mjl198',5,1),(101,90.00,30,'jja42',NULL,0),(102,10.00,2,'jja42',NULL,0),(103,64.00,8,'jja42',NULL,0),(104,40.00,10,'ght8',6,1),(105,133.00,7,'bgb31',NULL,0);
/*!40000 ALTER TABLE `swipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `name` varchar(255) NOT NULL,
  `ID` varchar(10) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Ben','bgb31'),('Dave','dbr211'),('drew','dsh108'),('Gloria','ght8'),('James','jja42'),('Janet','jys10'),('Madison','mjl198');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-02 11:42:31
