import smtplib, os

message = '''From: %email_from%
To: %email_to%
Subject: Invite
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. После окончания курса у тебя будет 2 месяца, чтобы догнать программу. 
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
FRIEND_NAME = "Друг"
ANOTHER_FRIEND_NAME = "Другой Друг"

message = message.replace("%email_from%",EMAIL_FROM).replace("%email_to%",EMAIL_TO).replace('%website%', 'dvmn.org').replace('%friend_name%',FRIEND_NAME).replace('%my_name%', ANOTHER_FRIEND_NAME)

message = message.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(LOGIN, PASSWORD)
server.sendmail(LOGIN, LOGIN, message)
server.quit()