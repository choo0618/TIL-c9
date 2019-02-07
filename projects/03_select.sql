-- 1.
SELECT 영화이름 FROM movies WHERE 상영시간 >= 150;
-- 2.
SELECT 영화코드, 영화이름 FROM movies WHERE 장르 = '애니메이션';
-- 3.
SELECT 영화이름 FROM movies WHERE 장르 = '애니메이션' and 제작국가 = '덴마크';
-- 4.
SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수 > 1000000 and 관람등급 = '청소년관람불가';
-- 5.
SELECT * FROM movies WHERE 개봉연도 between 20000101 and 20091231;
-- 6.
SELECT distinct 장르 FROM movies;