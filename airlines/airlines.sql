DROP DATABASE IF EXISTS airlines;

CREATE DATABASE airlines;

USE airlines;

DROP TABLE IF EXISTS CA;
CREATE TABLE CA (
  City varchar(32) NOT NULL,
  Country varchar(64),
  IATA varchar(32),
  ICAO varchar(32),
  Airport varchar(64),
  PRIMARY KEY (IATA)
);
SELECT * FROM CA;


DROP TABLE IF EXISTS MU;
CREATE TABLE MU (
  City varchar(32) NOT NULL,
  Country varchar(64),
  IATA varchar(32),
  ICAO varchar(32),
  Airport varchar(64),
  PRIMARY KEY (IATA)
);
SELECT * FROM MU;


DROP TABLE IF EXISTS CZ;
CREATE TABLE CZ (
  City varchar(32) NOT NULL,
  Country varchar(64),
  IATA varchar(32),
  ICAO varchar(32),
  Airport varchar(64),
  PRIMARY KEY (IATA)
);
SELECT * FROM CZ;


DROP TABLE IF EXISTS HU;
CREATE TABLE HU (
  City varchar(32) NOT NULL,
  Country varchar(64),
  IATA varchar(32),
  ICAO varchar(32),
  Airport varchar(64),
  PRIMARY KEY (IATA)
);
SELECT * FROM HU;


--
-- MySQL do not support OUTER JOIN
-- Instead, we can use a LEFT JOIN UNION a RIGHT JOIN


SELECT CA.IATA as CA, MU.IATA as MU
FROM CA 
LEFT JOIN MU ON CA.IATA = MU.IATA
UNION
SELECT CA.IATA as CA, MU.IATA as MU
FROM CA 
RIGHT JOIN MU ON CA.IATA = MU.IATA;


# add a new column in each table indicating the operation airline
ALTER TABLE CA
ADD  CA varchar(8),
ADD  MU varchar(8),
ADD  CZ varchar(8),
ADD  HU varchar(8);
# unlock safe undate mode
SET SQL_SAFE_UPDATES = 0;
UPDATE CA
SET CA = 'yes';
select * from CA;

ALTER TABLE MU
ADD  CA varchar(8),
ADD  MU varchar(8),
ADD  CZ varchar(8),
ADD  HU varchar(8);
UPDATE MU
SET MU = 'yes';

ALTER TABLE CZ
ADD  CA varchar(8),
ADD  MU varchar(8),
ADD  CZ varchar(8),
ADD  HU varchar(8);
UPDATE CZ
SET CZ = 'yes';

ALTER TABLE HU
ADD  CA varchar(8),
ADD  MU varchar(8),
ADD  CZ varchar(8),
ADD  HU varchar(8);
UPDATE HU
SET HU = 'yes';



# Combine two table CA and MU first (outter join)
DROP TABLE IF EXISTS allairline; 
CREATE TABLE allairline AS
SELECT CA.IATA, CA.CA, MU.MU FROM CA
LEFT JOIN MU 
ON CA.IATA = MU.IATA
UNION 
SELECT MU.IATA, CA.CA, MU.MU FROM CA
RIGHT JOIN MU 
ON CA.IATA = MU.IATA;

CREATE TABLE allairline2 AS
SELECT allairline.*, CZ.CZ FROM allairline
LEFT JOIN CZ
ON allairline.IATA = CZ.IATA
UNION
SELECT CZ.IATA, allairline.CA, allairline.MU, CZ.CZ FROM allairline
RIGHT JOIN CZ
ON allairline.IATA = CZ.IATA;

CREATE TABLE allairline3 AS
SELECT allairline2.*, HU.HU FROM allairline2
LEFT JOIN HU
ON allairline2.IATA = HU.IATA
UNION
SELECT HU.IATA, allairline2.CA, allairline2.MU, allairline2.CZ, HU.HU FROM allairline2
RIGHT JOIN HU
ON allairline2.IATA = HU.IATA;

select * from allairline3 order by IATA;
# So far we have a table 'allairline3' with all destinations

# Method 2
SELECT IATA, CA, MU, CZ, HU FROM CA
UNION
SELECT IATA, CA, MU, CZ, HU FROM MU
UNION
SELECT IATA, CA, MU, CZ, HU FROM CZ
UNION
SELECT IATA, CA, MU, CZ, HU FROM HU
ORDER BY IATA;



