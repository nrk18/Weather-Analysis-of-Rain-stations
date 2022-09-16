SELECT AVG(`pm 2.5`) AS `Average PM 2.5`,AVG(`vpm 2.5`) AS `Average PM 2.5`,`location` AS `Location` 
FROM `readings`,`stations` WHERE (CAST(`date time` AS TIME)> '07:30:00' AND CAST(`date time` AS TIME)< '08:30:00') 
AND YEAR(`date time`) BETWEEN 2010 AND 2019 AND `readings`.`SiteID`=`stations`.`SiteID` GROUP BY `location`;
