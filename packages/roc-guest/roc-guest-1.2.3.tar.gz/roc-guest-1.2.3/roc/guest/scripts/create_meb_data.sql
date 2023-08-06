-- MySQL dump 10.15  Distrib 10.0.21-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: das_validation_db_data_3
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

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `device` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Automatic unique ID for index and research efficiency',
  `DeviceName` varchar(20) NOT NULL COMMENT 'Name of the device',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `DeviceName_UNIQUE` (`DeviceName`(10))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COMMENT='Liste des device (TNR-HFR, DPU, ...)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `errorcode`
--

DROP TABLE IF EXISTS `errorcode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `errorcode` (
  `eventID` int(11) NOT NULL COMMENT 'Unique Id of an event saved in the eventdescr table',
  `ErrorMessage_ErrorCode` int(11) NOT NULL COMMENT 'Id of an error message',
  UNIQUE KEY `eventID_UNIQUE` (`eventID`),
  KEY `fk_ErrorCode_eventdescr1_idx` (`eventID`),
  KEY `fk_ErrorCode_ErrorMessage1_idx` (`ErrorMessage_ErrorCode`),
  CONSTRAINT `fk_ErrorCode_ErrorMessage1` FOREIGN KEY (`ErrorMessage_ErrorCode`) REFERENCES `errormessage` (`ErrorCode`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_ErrorCode_eventdescr1` FOREIGN KEY (`eventID`) REFERENCES `eventdescr` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `errormessage`
--

DROP TABLE IF EXISTS `errormessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `errormessage` (
  `ErrorCode` int(11) NOT NULL COMMENT 'Unique Id of an error code saved in the table ErrorCode',
  `ErrorMessage` varchar(45) NOT NULL COMMENT 'Message of the error',
  PRIMARY KEY (`ErrorCode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `eventdescr`
--

DROP TABLE IF EXISTS `eventdescr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eventdescr` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Automatic unique ID for index and research efficiency',
  `DateProduction` datetime NOT NULL COMMENT 'Production date/time of the event ',
  `XML` longtext COMMENT 'The XML document that fully describe the event.',
  `Device` int(10) unsigned NOT NULL COMMENT 'Id of the device from the event is sent.',
  `PacketType` int(10) unsigned NOT NULL COMMENT 'Id of the type of the packet',
  `AssociatedTest` int(11) DEFAULT NULL COMMENT 'ID of the test (from ï¿½TestDescriptorï¿½ table) running when the event was produced',
  `Category` text COMMENT 'Category of the packet',
  `Name` varchar(256) DEFAULT NULL COMMENT 'Name of the packet',
  `Collection` int(10) unsigned NOT NULL COMMENT 'Id of the collection of the packet',
  `Status` int(11) DEFAULT NULL COMMENT 'Status if the packet is a feedback type',
  PRIMARY KEY (`ID`),
  KEY `fk_eventdescr_device1_idx` (`Device`),
  KEY `fk_eventdescr_packettype1_idx` (`PacketType`),
  KEY `fk_eventdescr_TestDescriptor1_idx` (`AssociatedTest`),
  KEY `DateProduction_Index` (`DateProduction`),
  KEY `fk_eventdescr_parsercollection1_idx` (`Collection`),
  KEY `fk_eventdescr_feedbackstatus1_idx` (`Status`),
  KEY `Category_Index` (`Category`(256)),
  KEY `Name_index` (`Name`),
  CONSTRAINT `fk_eventdescr_TestDescriptor1` FOREIGN KEY (`AssociatedTest`) REFERENCES `testdescriptor` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_eventdescr_device1` FOREIGN KEY (`Device`) REFERENCES `device` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_eventdescr_feedbackstatus1` FOREIGN KEY (`Status`) REFERENCES `feedbackstatus` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_eventdescr_packettype1` FOREIGN KEY (`PacketType`) REFERENCES `packettype` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_eventdescr_parsercollection1` FOREIGN KEY (`Collection`) REFERENCES `parsercollection` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=47663953 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `feedbackstatus`
--

DROP TABLE IF EXISTS `feedbackstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedbackstatus` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Automatic unique ID for index and research efficiency',
  `Status` varchar(20) NOT NULL COMMENT 'Text indicating the status of the feedback',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `packettype`
--

DROP TABLE IF EXISTS `packettype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `packettype` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Automatic unique ID for index and research efficiency',
  `Type` varchar(20) NOT NULL COMMENT 'Name of the packet type',
  `IsInput` tinyint(1) NOT NULL COMMENT 'For a TC (event sent toward the device) this column is set to true. For a TM (event produced by the device) this column is set to false',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Type_UNIQUE` (`Type`),
  KEY `IsInput_Index` (`IsInput`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COMMENT='List des type de paquets (TM, TCFeedback, ...)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `parsercollection`
--

DROP TABLE IF EXISTS `parsercollection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parsercollection` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Automatic unique ID for index and research efficiency',
  `CollectionName` varchar(20) NOT NULL COMMENT 'Name of the collection',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `CollectionName_UNIQUE` (`CollectionName`(10))
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1 COMMENT='List of available parsers collection (e.g. ''IDB'')';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `testdescriptor`
--

DROP TABLE IF EXISTS `testdescriptor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testdescriptor` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Automatic unique ID for index and research efficiency',
  `UUID` varchar(45) NOT NULL COMMENT 'The UUID that uniquely identified the script in the system',
  `TestName` varchar(256) NOT NULL COMMENT 'A unique name for the test',
  `Status` enum('Running','Pending','Terminated') NOT NULL COMMENT 'Indicates the status of the script (Running, Pending, Terminated)',
  `Author` varchar(45) DEFAULT NULL COMMENT 'Name of the author of the test',
  `Description` varchar(1024) DEFAULT NULL COMMENT 'A description of the test',
  `CreationDate` datetime NOT NULL COMMENT 'Date of creation of the test',
  `OneShot` tinyint(1) NOT NULL COMMENT 'Indicate that the script is a one-shot one (set to 1) or an interactive one (set to 0)',
  `Launched` datetime DEFAULT NULL COMMENT 'Date of test starting',
  `TerminatedDate` datetime DEFAULT NULL COMMENT 'Date of test sending',
  `RunningDPUIsNominal` tinyint(1) DEFAULT NULL COMMENT 'Inidcate if when launching the test, the DPU is the nominal one (True) or the redondant one (False)',
  `XML` longtext NOT NULL COMMENT 'The XML document that fully describe the TC script.',
  `MainScript` int(10) unsigned DEFAULT NULL COMMENT 'If the script is a one-shot one, this column is mandatory and shall reference the main script linked to the test.',
  `HWVersion` longtext COMMENT 'Configuration and version of the HardWare when the test has been launched',
  `SWVersion` longtext COMMENT 'Configurations and versions of the Softwares when the test has been launched',
  `OtherConfiguration` longtext COMMENT 'Configuration and version of other components.',
  `Masked` tinyint(1) DEFAULT '0' COMMENT 'Indicates if the test is masked for the UI User',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `UUID_UNIQUE` (`UUID`),
  KEY `TestName_Index` (`TestName`)
) ENGINE=InnoDB AUTO_INCREMENT=17521 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-15 10:05:04
