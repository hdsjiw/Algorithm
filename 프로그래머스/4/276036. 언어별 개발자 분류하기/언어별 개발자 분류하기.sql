-- 코드를 작성해주세요
SELECT
    CASE
        WHEN (d.SKILL_CODE & (
            SELECT SUM(CODE)
            FROM SKILLCODES
            WHERE CATEGORY = 'Front End'
        )) > 0
        AND (d.SKILL_CODE & (
            SELECT CODE
            FROM SKILLCODES
            WHERE NAME = 'Python'
        )) > 0
        THEN 'A'

        WHEN (d.SKILL_CODE & (
            SELECT CODE
            FROM SKILLCODES
            WHERE NAME = 'C#'
        )) > 0
        THEN 'B'

        WHEN (d.SKILL_CODE & (
            SELECT SUM(CODE)
            FROM SKILLCODES
            WHERE CATEGORY = 'Front End'
        )) > 0
        THEN 'C'
    END AS GRADE,
    d.ID,
    d.EMAIL
FROM DEVELOPERS d
HAVING GRADE IS NOT NULL
ORDER BY GRADE ASC, d.ID ASC;