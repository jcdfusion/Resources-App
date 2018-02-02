--This file contains the definitions of the tables used in the application
--***** NEW AWS DB ******
--Collection Center table
create table collectionCenter(collectionCenterID serial primary key, zipCode integer, street varchar(20), town varchar(20), state_region varchar(20), country varchar(20), collection_center_name varchar(20));
--
--Resources table
create table resources(resourceID serial primary key, collectionCenterID integer references collectionCenter(collectionCenterID), resourceType varchar(20), buy_free boolean, market_price money,qty integer);
--

--User type table
create table userType(userTypeID serial primary key, user_type varchar(20));
--
--Users table
create table users(userID varchar(20) primary key, userTypeID integer references userType(userTypeID), user_first_name varchar(20), user_last_name varchar(20), user_email varchar(20));
--
--Users password table
create table userPassword(userPassID serial primary key, userID varchar references users(userID), user_value varchar(20));
--
--User Request table
create table userRequest(requestID serial primary key, userID varchar references users(userID),resourceID integer references resources(resourceID), req_first_name varchar(20),req_last_name varchar(20), req_email varchar(20), req_phone varchar(20), street varchar(20), zipCode integer, town_name varchar(20), state_region_name varchar(20), country varchar(20));
--
--Water resource table
create table water(waterID serial primary key, resourceID integer references resources(resourceID), waterType varchar(20), waterBrand varchar(20), qtyMeasure real);
--
--Food resource table
create table food(foodID serial primary key, resourceID integer references resources(resourceID), foodTypeID varchar(20), foodName varchar(20), qtyWeight real);
--
--Ice resource table
create table ice(iceID serial primary key, resourceID integer references resources(resourceID), iceBrand varchar(20), qtyWeight real);
--
--
--Clothing resource table
create table clothing(clothingID serial primary key, resourceID integer references resources(resourceID),clothingType varchar(20),clothing_size varchar(20),clothingBrand varchar(20), clothingColor varchar(20), qty real);
--
--
--Gas resource table
create table fuel(gasID serial primary key, resourceID integer references resources(resourceID), gasTypeID varchar(20), gasBrand varchar(20), gasOctanage real, qty real);

--
--Medical devices table
create table medicalDevices(medicalDevicesID serial primary key, resourceID integer references resources(resourceID), medicalDeviceType varchar(20), medDevName varchar(20), medDevManufacturer varchar(20),toTreat varchar(20), qty integer);
--
--Heavy equipment table
create table heavyEquipment(heavyEquipmentID serial primary key, resourceID integer references resources(resourceID), heavyEquipmentType varchar(20), heavyEquipmentBrand varchar(20), qty real);
--
--Tools resource table
create table tools(toolsID serial primary key, resourceID integer references resources(resourceID), toolType varchar(20), toolBrand varchar(20), qty integer);
--

--Power generators table
create table powerGenerator(powerGeneratorID serial primary key, resourceID integer references resources(resourceID), powerGeneratorType varchar(20), powerGeneratorBrand varchar(20), watts real, qty integer);
--

--
--Batteries resource table
create table batteries(batteriesID serial primary key, resourceID integer references resources(resourceID), batteryType varchar(20), batteryBrand varchar(20), batteryVoltage real, qty integer);

--
--Medicine resource table
create table medicine(medicineID serial primary key, resourceID integer references resources(resourceID), medicineType varchar(20), medicine_form varchar(20), medicine_name varchar(20), medicine_exp_date date, medicine_manufacturer varchar(20), medicineQty real);
--

--CreditCards table 
create table creditcards(ccNumb integer primary key, userID varchar references users(userID), ccFirst char(20), ccLast char(20), expDate date, CVC integer, cType char(20));
--
--Purchases table
create table purchases(purchaseID serial primary key, userID varchar references users(userID), resourcesID integer references resources(resourceID), requestID integer references userRequest(requestID), ccNumb integer references creditcards(ccNumb), resourceQty integer);
-- 
--Transactions Table
create table transaction(transactionid serial primary key, userid varchar references users(userID), resourceid integer references resources(resourceID), ccnumb integer references creditcards(ccNumb));
