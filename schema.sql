--This file contains the definitions of the tables used in the application
--
--
--Town table
create table town(townID serial primary key, town_name varchar(20));
--
--State/Region table
create table state_region(state_regionID serial primary key, townID integer references town(townID), state_region_name varchar(20)  );
--
--Country table
create table country(countryID serial primary key, state_regionID integer references state_region(state_regionID), country_name varchar(20));
--
--Location table
create table location(zipCode integer primary key,countryID integer references country(countryID), state_regionID integer references state_region(state_regionID), townID integer references town(townID) );
--
--Collection Center table
create table collectionCenter(collectionCenterID serial primary key, zipCode integer references location(zipCode), street varchar(20),collection_center_name varchar(20));
--
--Resource type table
create table resourceType(resourceTypeID serial primary key, resource_type varchar(20));
--
--Resources table
create table resources(resourceID serial primary key, collectionCenterID integer references collectionCenter(collectionCenterID), resourceTypeID integer references resourceType(resourceTypeID), purchased_free varchar(9), resource_price integer,qty integer);
--
--User type table
create table userType(userTypeID serial primary key, user_type varchar(20));
--
--Users table
create table users(userID serial primary key, userTypeID integer references userType(userTypeID), zipCode integer references location(zipCode), user_first_name varchar(20), user_last_name varchar(20), user_email varchar(20));
--
--Users password table
create table userPassword(userPassID serial primary key, userID integer references users(userID), user_value varchar(20));
--
--User Request table
create table userRequest(requestID serial primary key, userID integer references users(userID),resourceID integer references resources(resourceID), req_first_name varchar(20),req_last_name varchar(20), req_email varchar(20), req_phone varchar(20), street varchar(20), zipCode integer, town_name varchar(20), state_region_name varchar(20), country varchar(20));
--
--Water type table
create table waterType(waterTypeID serial primary key, water_type varchar(20));
--
--Water resource table
create table water(waterID serial primary key, resourceID integer references resources(resourceID), waterTypeID integer references waterType(waterTypeID), qty integer);
--
--Food type table
create table foodType(foodTypeID serial primary key, food_type varchar(20));
--
--Food resource table
create table food(foodID serial primary key, resourceID integer references resources(resourceID), foodTypeID integer references foodType(foodTypeID), qty integer);
--
--Ice resource table
create table ice(iceID serial primary key, resourceID integer references resources(resourceID), qty integer);
--
--Clothing type table
create table clothingType(clothingTypeID serial primary key, clothing_type varchar(20));
--
--Clothing resource table
create table clothing(clothingID serial primary key, resourceID integer references resources(resourceID),clothingTypeID integer references clothingType(clothingTypeID),clothing_size varchar(20),qty integer);
--
--Gas type table
create table gasType(gasTypeID serial primary key, gas_type varchar(20));
--
--Gas resource table
create table gas(gasID serial primary key, resourceID integer references resources(resourceID), gasTypeID integer references gasType(gasTypeID), qty integer );
--
--Medical devices type table
create table medicalDeviceType(medicalDeviceTypeID serial primary key, medicalDevice_type varchar(20));
--
--Medical devices table
create table medicalDevices(medicalDevicesID serial primary key, resourceID integer references resources(resourceID), medicalDeviceTypeID integer references medicalDeviceType(medicalDeviceTypeID), medDevName varchar(20), medDevManufacturer varchar(20),qty integer);
--
--Heavy equipment type table
create table heavyEquipmentType(heavyEquipmentTypeID serial primary key, heavyEquipment_type varchar(20));
--
--Heavy equipment table
create table heavyEquipment(heavyEquipmentID serial primary key, resourceID integer references resources(resourceID), heavyEquipmentTypeID integer references heavyEquipmentType(heavyEquipmentTypeID), qty integer);
--
--Tool type table
create table toolType(toolTypeID serial primary key, tool_type varchar(20));
--
--Tools resource table
create table tools(toolsID serial primary key, resourceID integer references resources(resourceID), toolTypeID references toolType(toolTypeID), qty integer);
--
--Power generator type table
create table powerGeneratorType(powerGeneratorTypeID serial primary key, powerGenerator_type varchar(20));
--
--Power generators table
create table powerGenerator(powerGeneratorID serial primary key, resourceID integer references resources(resourceID), powerGeneratorTypeID integer references powerGeneratorType(powerGeneratorTypeID), watts integer, qty integer);
--
--Battery type table
create table batteryType(batteryTypeID serial primary key, batteries_type varchar(20));
--
--Batteries resource table
create table batteries(batteriesID serial primary key, resourceID integer references resources(resourceID), batteryTypeID integer references batteryType(batteryTypeID), qty integer);
--
--Medicine category table
create table medicineCategory(medicine_categoryID serial primary key, medicine_type varchar(20));
--
--Medicine resource table
create table medicine(medicineID serial primary key, resourceID integer references resources(resourceID), medicine_categoryID integer references medicineCategory(medicine_categoryID), medicine_name varchar(20), medicine_exp_date date, medicine_manufacture varchar(20));
