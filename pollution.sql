-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pollution-db` DEFAULT CHARACTER SET utf8 ;
USE `pollution-db` ;

-- -----------------------------------------------------
-- Table `pollution-db`.`stations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`stations` (
  `stationid` INT NOT NULL,
  `location` VARCHAR(48) NULL,
  `geo_point_2d` VARCHAR(24) NULL,
  PRIMARY KEY (`stationid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution-db`.`readings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`readings` (
  `readingid` INT NOT NULL,
  `datetime` DATETIME NULL,
  `nox` FLOAT NULL,
  `no2` FLOAT NULL,
  `no` FLOAT NULL,
  `pm 10` FLOAT NULL,
  `nvpm 10` FLOAT NULL,
  `vpm 10` FLOAT NULL,
  `mvpm 2.5` FLOAT NULL,
  `pm 2.5` FLOAT NULL,
  `vpm 2.5` FLOAT NULL,
  `co` FLOAT NULL,
  `o3` FLOAT NULL,
  `so2` FLOAT NULL,
  `temperature` REAL NULL,
  `rh` INT NULL,
  `air pressure` INT NULL,
  `datestart` DATETIME NULL,
  `dateend` DATETIME NULL,
  `current` TEXT(5) NULL,
  `instrumenttype` VARCHAR(32) NULL,
  `stationid-fk` INT NOT NULL,
  PRIMARY KEY (`redaingid`),
  INDEX `fk_readings_stations_idx` (`stationid-fk` ASC) VISIBLE,
  CONSTRAINT `fk_readings_stations`
    FOREIGN KEY (`stationid-fk`)
    REFERENCES `pollution-db`.`stations` (`stationid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution-db`.`schemsa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`schema` (
  `measure` VARCHAR(32) NOT NULL,
  `description` VARCHAR(64) NULL,
  `unit` VARCHAR(24) NULL,
  PRIMARY KEY (`measure`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
