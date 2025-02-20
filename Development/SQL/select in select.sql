SELECT count(*) AS count
FROM
  (select consultation.visitor_name "Посетитель",
          consultation.feedback_dt "Вопрос: дата",
          consultation.visitor_message "Вопрос",
          consultation.visitor_email "Посетитель: почта",
          consultation.city "Посетитель: город",
          consultation.dt_validation "Ответ: дата",
          consultation.answer "Ответ",
          kladrcity.name "Прог.: город",
          specialist.title "Специалист: доктор",
          duser.email "Специалист: валидатор",
          consultationgroup.name "Категория",
          consultation.email_is_sent "Ответ: послан"
   from app_cms_freeconsultation consultation
   left join app_addresses_kladrcity kladrcity on kladrcity.id = consultation.kladr_city_id
   left join app_cms_freeconsultationgroup consultationgroup on consultationgroup.id = consultation.category_id
   left join app_mis_specialist specialist on specialist.id = consultation.specialist_doc_id
   left join app_users_user duser on duser.id = consultation.specialist_valid_id) AS virtual_table
WHERE "Ответ: дата" >= TO_TIMESTAMP('2023-05-16 00:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.US')
  AND "Ответ: дата" < TO_TIMESTAMP('2023-05-17 00:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.US')
  AND "Ответ: дата" IS NOT NULL
LIMIT 50000;

=================================================================================================================================================================

select * from (
  SELECT id,
  ROW_NUMBER() OVER(PARTITION BY column1, column2 ORDER BY id asc) AS Row
  FROM tbl
) dups
where 
dups.Row > 1

=================================================================================================================================================================

WITH it_employees AS (
    SELECT id, name, department, salary
    FROM employees
    WHERE department = 'IT'
)
SELECT name, department, salary
FROM it_employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);