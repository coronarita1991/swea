SELECT
  COUNT(*)                           AS FISH_COUNT,         -- 잡은 수(Null 포함해서 모두 카운트)
  MAX(COALESCE(LENGTH, 10))          AS MAX_LENGTH,         -- 최대 길이(≤10cm는 10으로 간주)
  FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(COALESCE(LENGTH, 10)) >= 33  -- 평균 길이 33cm 이상 (≤10cm는 10으로 간주)
ORDER BY FISH_TYPE ASC;