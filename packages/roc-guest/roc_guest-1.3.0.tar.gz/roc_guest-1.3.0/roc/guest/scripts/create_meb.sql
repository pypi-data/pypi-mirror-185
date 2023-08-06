-- MySQL dump 10.15  Distrib 10.0.21-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: das_validation_db
-- ------------------------------------------------------
-- Server version	5.6.25-log

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
-- Table structure for table `databaseinformation`
--

DROP TABLE IF EXISTS `databaseinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `databaseinformation` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DatabaseName` varchar(256) DEFAULT NULL,
  `CreationDate` datetime DEFAULT NULL,
  `TerminatedDate` datetime DEFAULT NULL,
  `description` text,
  `Name` varchar(256) DEFAULT NULL,
  `Current` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `DatabaseName_UNIQUE` (`DatabaseName`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `UUID` varchar(32) NOT NULL,
  `ProjectName` varchar(256) NOT NULL,
  `Author` varchar(45) DEFAULT NULL,
  `CreationDate` datetime NOT NULL,
  `ModificationDate` datetime NOT NULL,
  `Description` varchar(1024) DEFAULT NULL,
  `Locked` tinyint(1) DEFAULT NULL,
  `XML` longtext,
  `Masked` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `UUID_UNIQUE` (`UUID`),
  UNIQUE KEY `ProjectName_UNIQUE` (`ProjectName`),
  KEY `Author_Index` (`Author`),
  KEY `CreationDate_Index` (`CreationDate`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `projectlocked`
--

DROP TABLE IF EXISTS `projectlocked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projectlocked` (
  `project_ID` int(10) unsigned NOT NULL,
  `User_ID` int(11) NOT NULL,
  PRIMARY KEY (`project_ID`,`User_ID`),
  KEY `fk_ProjectLocked_User1_idx` (`User_ID`),
  CONSTRAINT `fk_ProjectLocked_User1` FOREIGN KEY (`User_ID`) REFERENCES `user` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_ProjectLocked_project1` FOREIGN KEY (`project_ID`) REFERENCES `project` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `projecttcscriptlistentry`
--

DROP TABLE IF EXISTS `projecttcscriptlistentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projecttcscriptlistentry` (
  `Project_id` int(10) unsigned NOT NULL,
  `ScriptID` int(10) unsigned NOT NULL,
  PRIMARY KEY (`Project_id`,`ScriptID`),
  KEY `fk_TCScripttProjectEntry` (`Project_id`),
  KEY `fk_projecttcscriptlistentry` (`ScriptID`),
  CONSTRAINT `fk_TCScriptProjectEntry_TCScriptProject1` FOREIGN KEY (`Project_id`) REFERENCES `project` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_projecttcscriptlistentry_tcscript1` FOREIGN KEY (`ScriptID`) REFERENCES `tcscript` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `projecttestlistentry`
--

DROP TABLE IF EXISTS `projecttestlistentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projecttestlistentry` (
  `Project_id` int(10) unsigned NOT NULL,
  `TestDescriptor_ID` int(11) NOT NULL,
  `database_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`Project_id`,`TestDescriptor_ID`),
  KEY `fk_projecttestlistentry_databaseinformation1_idx` (`database_ID`),
  KEY `fk_projectTestlistentry_project1_idx` (`Project_id`),
  CONSTRAINT `fk_projecttestlistentry_databaseinformation1` FOREIGN KEY (`database_ID`) REFERENCES `databaseinformation` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_projecttestlistentry_project1` FOREIGN KEY (`Project_id`) REFERENCES `project` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `scriptlocked`
--

DROP TABLE IF EXISTS `scriptlocked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scriptlocked` (
  `User_ID` int(11) NOT NULL,
  `TCScript_ID` int(10) unsigned NOT NULL,
  PRIMARY KEY (`TCScript_ID`,`User_ID`),
  KEY `fk_ScriptLocked_User1_idx` (`User_ID`),
  KEY `fk_ScriptLocked_TCScript1_idx` (`TCScript_ID`),
  CONSTRAINT `fk_ScriptLocked_TCScript1` FOREIGN KEY (`TCScript_ID`) REFERENCES `tcscript` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_ScriptLocked_User1` FOREIGN KEY (`User_ID`) REFERENCES `user` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `scriptrelation`
--

DROP TABLE IF EXISTS `scriptrelation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scriptrelation` (
  `ParentId` int(11) NOT NULL,
  `ChildId` int(11) NOT NULL,
  PRIMARY KEY (`ParentId`,`ChildId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tcscript`
--

DROP TABLE IF EXISTS `tcscript`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcscript` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `UUID` varchar(32) NOT NULL,
  `ScriptName` varchar(256) NOT NULL,
  `author` varchar(256) DEFAULT NULL,
  `CreationDate` datetime NOT NULL,
  `ModificationDate` datetime NOT NULL,
  `Description` varchar(1024) DEFAULT NULL,
  `Locked` tinyint(1) DEFAULT NULL COMMENT 'Indicate if a script is user locked or not',
  `XML` longtext NOT NULL,
  `Executed` tinyint(1) NOT NULL DEFAULT '0',
  `masked` tinyint(1) DEFAULT '0',
  `majorVersion` int(11) DEFAULT NULL,
  `minorversion` int(11) DEFAULT NULL,
  `last` tinyint(1) NOT NULL DEFAULT '1',
  `isVersionnedId` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `UUID_UNIQUE` (`UUID`),
  UNIQUE KEY `ScriptName_UNIQUE` (`ScriptName`),
  KEY `Author_Index` (`author`),
  KEY `CreationDate_Index` (`CreationDate`),
  KEY `ModificationDate_Index` (`ModificationDate`)
) ENGINE=InnoDB AUTO_INCREMENT=7002 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `testlocked`
--

DROP TABLE IF EXISTS `testlocked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testlocked` (
  `Test_ID` int(11) NOT NULL,
  `User_ID` int(11) NOT NULL,
  PRIMARY KEY (`Test_ID`,`User_ID`),
  KEY `fk_TestLocked_TestDescriptor1_idx` (`Test_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Automatic unique ID for index and research efficiency',
  `Login` varchar(256) NOT NULL,
  `Password` varchar(45) DEFAULT NULL,
  `Admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-15 10:03:56
