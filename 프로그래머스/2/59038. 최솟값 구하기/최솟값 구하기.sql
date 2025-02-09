-- 코드를 입력하세요 : 가장 먼저 들어온 것을 구해야 함. 
SELECT DATETIME AS "시간"
FROM (
    SELECT *, 
    RANK() OVER(ORDER BY DATETIME ASC) AS RANK_DATETIME
    FROM ANIMAL_INS
) AS A
WHERE A.RANK_DATETIME = 1;