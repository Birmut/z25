 CREATE TABLE users (
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE );

 CREATE TABLE questions (
  id SERIAL NOT NULL PRIMARY KEY,
  questions TEXT NOT NULL,
   );  

 CREATE TABLE answers (
  id SERIAL NOT NULL PRIMARY KEY,
  answers TEXT NOT NULL );  

 CREATE TABLE users_answers(
  id_user INTEGER references users(id),
  id_answers Integer references answers(id),
  PRIMARY KEY (id_user , id_answers)
   );


 INSERT INTO users(name, email)
 VALUES ('putin', 'putin@gmail.ru'),
        ('messi', 'messi@gmail.ru'),
        ('mapke', 'mapke@gmail.ru');

 INSERT INTO questions(questions)
 VALUES ('сколько будет 2+2'),
        ('арбуз - это?'),
        ('синус 30 равен');

 INSERT INTO answers(answers)
 VALUES ('4' || '5' || '6'),
       ('яблоко' || 'ягода' || 'фрукт'),
        ('1.5' || '2' || '3');


