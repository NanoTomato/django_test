# django_test

Есть две таблицы: в одной проекты, в другой сотрудники.

                                Table "public.polls_project"
 Column |         Type          |                         Modifiers                          
--------|-----------------------|------------------------------------------------------------
 id     | integer               | not null default nextval('polls_project_id_seq'::regclass)
 name   | character varying(30) | not null


                                  Table "public.polls_employee"
   Column   |         Type          |                          Modifiers                          
------------|-----------------------|-------------------------------------------------------------
 id         | integer               | not null default nextval('polls_employee_id_seq'::regclass)
 name       | character varying(30) | not null
 birthdate  | date                  | not null
 project_id | integer               | not null

Есть админка, есть приложение polls, которое предоставляет RESTful API.
Соответственно /polls/projects(/[0-9]+)? - для взаимодействия с проектами
               /polls/employee(/[0-9]+)? - для взаимодействия с сотрудниками
