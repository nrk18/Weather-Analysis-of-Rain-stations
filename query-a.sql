SELECT `date time` as `Date and Time`,`location` AS `Location`,`nox` AS `Max NOx` 
FROM `readings`,`stations` WHERE `nox`= (SELECT MAX(`nox`) FROM `readings` 
                                         WHERE YEAR(`date time`)=2019) AND `readings`.`SiteID`=`stations`.`SiteID`;
