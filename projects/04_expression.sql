-- 1.
SELECT sum(누적관객수) as 누적관객수합계 from movies;
-- 2.
SELECT 영화이름, max(누적관객수) as 누적관객수 from movies;
-- 3.
SELECT 장르, min(상영시간) as 상영시간 from movies;
-- 4.
SELECT avg(누적관객수) as 평균누적관객수 from movies WHERE 제작국가 = '한국';
-- 5.
SELECT count(영화코드) as 영화개수 from movies WHERE 관람등급 = '청소년관람불가';
-- 6.
SELECT count(영화코드) as 영화개수 from movies WHERE 장르 = '애니메이션' and 상영시간 >= 100;