-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 16, 2020 at 12:59 PM
-- Server version: 5.7.31-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rocken8_customer`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminuser`
--

CREATE TABLE `adminuser` (
  `adminUserID` int(11) NOT NULL,
  `password` varchar(200) CHARACTER SET utf8 NOT NULL,
  `paymentContact` tinyint(1) NOT NULL,
  `level` tinyint(4) NOT NULL,
  `userID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminuser`
--

INSERT INTO `adminuser` (`adminUserID`, `password`, `paymentContact`, `level`, `userID`) VALUES
(1, '', 1, 1, 1),
(2, '', 1, 1, 2),
(3, 'password', 1, 1, 3),
(7, 'collegefields', 0, 2, 8);

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `contactID` int(11) NOT NULL,
  `type` tinyint(4) NOT NULL,
  `detail` varchar(500) CHARACTER SET utf8 NOT NULL,
  `customerID` int(11) NOT NULL,
  `userID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`contactID`, `type`, `detail`, `customerID`, `userID`) VALUES
(1, 0, 'craig.miranda@rockenbrew.com', 8, 1),
(2, 1, '+44 (0)742 190 2110', 8, 1),
(3, 0, 'anna@venueavenue.pl', 1, 2),
(4, 0, 'jon.swain@hackneybrewery.co.uk', 9, 3),
(12, 0, 'd@wimbledonbrewery', 24, 8),
(13, 2, '8 College Fields, Prince Georges Road, Wimbledon, United Kingdom, SW19 2PT', 24, 8);

-- --------------------------------------------------------

--
-- Table structure for table `countdata`
--

CREATE TABLE `countdata` (
  `countDataID` int(11) NOT NULL,
  `week1970` int(11) NOT NULL,
  `countCount` int(11) NOT NULL,
  `boxWidth` float NOT NULL,
  `sumAutoCount` int(11) NOT NULL,
  `sumManualCount` int(11) NOT NULL,
  `sumAdd` int(11) NOT NULL,
  `sumDelete` int(11) NOT NULL,
  `sumHomogenity` float NOT NULL,
  `userID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customerID` int(11) NOT NULL,
  `rbCustomerID` varchar(50) CHARACTER SET utf8 NOT NULL,
  `companyName` varchar(200) CHARACTER SET utf8 NOT NULL,
  `companyLocalID` varchar(200) CHARACTER SET utf8 NOT NULL,
  `companyLocalIDType` varchar(100) CHARACTER SET utf8 NOT NULL,
  `custTypeID` int(11) NOT NULL,
  `startDate` date NOT NULL,
  `domicile` varchar(2) CHARACTER SET utf8 NOT NULL COMMENT 'ISO3166a2'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customerID`, `rbCustomerID`, `companyName`, `companyLocalID`, `companyLocalIDType`, `custTypeID`, `startDate`, `domicile`) VALUES
(1, '1004', 'Venue Avenue', '', '', 8, '2018-09-19', 'PL'),
(2, '1001', 'HSBC Bank plc', '00014259', 'CH', 8, '2013-04-08', 'GB'),
(3, '1003', 'Mondo Brewing Company ltd', '09210166', 'CH', 1, '2018-06-26', 'GB'),
(6, '1002', 'East London Brewing Company ltd', '07627432', 'CH', 1, '2014-09-01', 'GB'),
(8, '1005', 'Rockenbrew Limited', '08478509', 'CH', 8, '2017-12-10', 'GB'),
(9, '1006', 'Hackney Brewery Ltd', '07696446', 'CH', 1, '2018-11-01', 'GB'),
(24, '1008', 'The Wimbledon Brewery Company Limited', '08387172', 'CH', 1, '2019-07-14', 'GB');

-- --------------------------------------------------------

--
-- Table structure for table `customertype`
--

CREATE TABLE `customertype` (
  `customerTypeID` int(11) NOT NULL,
  `type` varchar(200) NOT NULL,
  `scale` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customertype`
--

INSERT INTO `customertype` (`customerTypeID`, `type`, `scale`) VALUES
(7, 'Laboratory', 1),
(6, 'Winemaker', 3),
(5, 'Winemaker', 2),
(4, 'Winemaker', 1),
(3, 'Brewery', 999999),
(2, 'Brewery', 200),
(1, 'Brewery', 25),
(0, 'Brewery', 1),
(8, 'Medical', 1),
(9, 'School', 1);

-- --------------------------------------------------------

--
-- Table structure for table `keycode`
--

CREATE TABLE `keycode` (
  `keyCodeID` int(11) NOT NULL,
  `keyCodeVersion` smallint(6) NOT NULL,
  `keyCode` varchar(200) CHARACTER SET utf8 NOT NULL,
  `active` tinyint(1) NOT NULL,
  `date` datetime NOT NULL,
  `licenceID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `keycode`
--

INSERT INTO `keycode` (`keyCodeID`, `keyCodeVersion`, `keyCode`, `active`, `date`, `licenceID`) VALUES
(1, 0, '557676', 1, '2018-09-19 00:00:00', 1),
(2, 0, '456', 1, '2018-09-19 00:00:00', 2),
(3, 0, '18577', 1, '2019-02-25 00:00:00', 3),
(4, 0, '', 0, '0000-00-00 00:00:00', 0),
(6, 1, '100', 1, '2019-07-15 00:00:00', 8);

-- --------------------------------------------------------

--
-- Table structure for table `licence`
--

CREATE TABLE `licence` (
  `licenceID` int(11) NOT NULL,
  `type` tinyint(4) NOT NULL,
  `issueDate` date NOT NULL,
  `validFrom` date NOT NULL,
  `validTo` date NOT NULL,
  `activationCode` text NOT NULL,
  `paymentScheduleID` int(11) NOT NULL,
  `customerID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `licence`
--

INSERT INTO `licence` (`licenceID`, `type`, `issueDate`, `validFrom`, `validTo`, `activationCode`, `paymentScheduleID`, `customerID`) VALUES
(1, 0, '2018-09-19', '2018-09-19', '2018-09-21', 'Kolberga', 0, 8),
(2, 0, '2018-09-19', '2018-09-19', '2018-09-30', '', 0, 1),
(3, 0, '2019-02-25', '2019-02-25', '2022-02-25', 'LaburnumSt', 0, 9),
(8, 0, '2019-07-15', '2019-07-15', '2021-07-15', 'collegefields', 7, 24);

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `paymentID` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `operatorRef` varchar(200) CHARACTER SET utf8 NOT NULL,
  `bankRef` varchar(200) CHARACTER SET utf8 NOT NULL,
  `value` float NOT NULL,
  `paymentScheduleID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `paymentschedule`
--

CREATE TABLE `paymentschedule` (
  `paymentScheduleID` int(11) NOT NULL,
  `value` float NOT NULL,
  `frequency` float NOT NULL,
  `firstPaymentDate` date NOT NULL,
  `startDate` date NOT NULL,
  `lastPaymentDate` date NOT NULL,
  `active` tinyint(1) NOT NULL,
  `customerID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `paymentschedule`
--

INSERT INTO `paymentschedule` (`paymentScheduleID`, `value`, `frequency`, `firstPaymentDate`, `startDate`, `lastPaymentDate`, `active`, `customerID`) VALUES
(1, 0, 365, '2019-02-25', '2019-02-25', '2099-02-25', 1, 9),
(7, 384, 9999, '2019-07-15', '2019-07-15', '2019-07-15', 1, 24);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `userID` int(11) NOT NULL,
  `startDate` date NOT NULL,
  `username` varchar(100) CHARACTER SET utf8 NOT NULL,
  `city` varchar(200) CHARACTER SET utf8 NOT NULL,
  `domicile` varchar(2) CHARACTER SET utf8 NOT NULL COMMENT 'iso3166a2',
  `customerID` int(11) NOT NULL,
  `licenceID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`userID`, `startDate`, `username`, `city`, `domicile`, `customerID`, `licenceID`) VALUES
(1, '2018-09-19', 'craig', 'London', 'GB', 8, 1),
(2, '2018-09-19', 'anna', 'Krakow', 'PL', 1, 2),
(3, '2019-02-25', 'Jon', 'London', 'GB', 9, 3),
(8, '2019-07-15', 'derek', 'London', 'GB', 24, 8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminuser`
--
ALTER TABLE `adminuser`
  ADD PRIMARY KEY (`adminUserID`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`contactID`);

--
-- Indexes for table `countdata`
--
ALTER TABLE `countdata`
  ADD PRIMARY KEY (`countDataID`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customerID`),
  ADD UNIQUE KEY `rbCustomerID` (`rbCustomerID`);

--
-- Indexes for table `customertype`
--
ALTER TABLE `customertype`
  ADD PRIMARY KEY (`customerTypeID`);

--
-- Indexes for table `keycode`
--
ALTER TABLE `keycode`
  ADD PRIMARY KEY (`keyCodeID`);

--
-- Indexes for table `licence`
--
ALTER TABLE `licence`
  ADD PRIMARY KEY (`licenceID`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`paymentID`);

--
-- Indexes for table `paymentschedule`
--
ALTER TABLE `paymentschedule`
  ADD PRIMARY KEY (`paymentScheduleID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userID`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminuser`
--
ALTER TABLE `adminuser`
  MODIFY `adminUserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `contactID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `countdata`
--
ALTER TABLE `countdata`
  MODIFY `countDataID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `customerID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `customertype`
--
ALTER TABLE `customertype`
  MODIFY `customerTypeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `keycode`
--
ALTER TABLE `keycode`
  MODIFY `keyCodeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `licence`
--
ALTER TABLE `licence`
  MODIFY `licenceID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `paymentID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paymentschedule`
--
ALTER TABLE `paymentschedule`
  MODIFY `paymentScheduleID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
