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
create table resourceType(resourceTypeID serial primary key, resource_type varchar(15));
--
--Resources table
create table resources(resourceID serial primary key, collectionCenterID integer references collectionCenter(collectionCenterID), resourceTypeID integer references resourceType(resourceTypeID), qty integer);
--
--Water resource table
create table water(waterID serial primary key, resourceID integer references resources(resourceID), water_type varchar(10), qty integer);
--
--Food resource table
create table food(foodID serial primary key, resourceID integer references resources(resourceID), food_type char(10), qty integer);
--
--Ice resource table
create table ice(iceID serial primary key, resourceID integer references resources(resourceID), qty integer);
--
--Clothing resource table
create table clothing(clothingID serial primary key, resourceID integer references resources(resourceID),clothing_type varchar(15),clothing_size varchar(10),qty integer);
--
--Gas resource table
create table gas(gasID serial primary key, resourceID integer references resources(resourceID), gas_type varchar(10), qty integer );
--
--Medical devices table
create table medicalDevices(medicalDevicesID serial primary key, resourceID integer references resources(resourceID), medicalDevice_type varchar(20), qty integer);
--
--Heavy equipment table
create table heavyEquipment(heavyEquipmentID serial primary key, resourceID integer references resources(resourceID), heavyEquipment_type varchar(20), qty integer);
--
--Tools resource table
create table tools(toolsID serial primary key, resourceID integer references resources(resourceID), tools_type varchar(20), qty integer);
--
--Power generators table
create table powerGenerator(powerGeneratorID serial primary key, resourceID integer references resources(resourceID), powerGenerator_type varchar(20), watts integer, qty integer);
--
--Batteries resource table
create table batteries(batteriesID serial primary key, resourceID integer references resources(resourceID), batteries_type varchar(10), qty integer);
--
--Medicine category table
create table medicineCategory(medicine_categoryID serial primary key, medicine_type varchar(20));
--
--Medicine resource table
create table medicine(medicineID serial primary key, resourceID integer references resources(resourceID), medicine_categoryID integer references medicineCategory(medicine_categoryID), medicine_name varchar(20), medicine_exp_date date, medicine_manufacture varchar(20));
