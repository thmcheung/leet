SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(project_id) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(project_id) AS cnt
        FROM Project
        GROUP BY project_id
    ) AS max_cnt_subquery
);
