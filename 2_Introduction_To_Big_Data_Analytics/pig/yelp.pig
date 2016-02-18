--run from pig -x local
--do not use dump, use store

--Question2
DESCRIBE Y_m;
Y_m2 = FILTER Y_m by num_ratings > 1;
Y_m2_al = GROUP Y_m2 ALL; --create a bag of avg_wtdstars;
avgRes = FOREACH Y_m2_al GENERATE AVG(Y_m2.avg_wtdstars);
store avgRes into '/home/cloudera/avgRes';

--Question3
resIds = JOIN Y_rate2 by business_id, Y_m2 by business_idgroup;
resIdsGroup = GROUP resIds ALL;
avgResIds = FOREACH resIdsGroup GENERATE AVG(resIds.avg_wtdstars);
store avgResIds into '/home/cloudera/avgResIds';

--Last question
Flatten;
