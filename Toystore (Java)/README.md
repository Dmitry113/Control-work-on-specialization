Задание 2. Магазин игрушек (Java)
Информация о проекте
Необходимо написать проект, для розыгрыша в магазине игрушек. Функционал
должен содержать добавление новых игрушек и задания веса для выпадения
игрушек.
Как сдавать проект
Для сдачи проекта необходимо создать отдельный общедоступный
репозиторий(Github, gitlub, или Bitbucket). Разработку вести в этом
репозитории, использовать пул реквесты на изменения. Программа должна
запускаться и работать, ошибок при выполнении программы быть не должно.
Программа, может использоваться в различных системах, поэтому необходимо
разработать класс в виде конструктора
Задание
1) Напишите класс-конструктор у которого принимает минимум 3 строки,
содержащие три поля id игрушки, текстовое название и частоту выпадения
игрушки
2) Из принятой строки id и частоты выпадения(веса) заполнить минимум три
массива.
3) Используя API коллекцию: java.util.PriorityQueue добавить элементы в
коллекцию
4) Организовать общую очередь 5) Вызвать Get 10 раз и записать результат в
файл
Подсказка:
В метод put передаете последовательно несколько строк
1 2 конструктор;
2 2 робот;
3 6 кукла.
Метод Get должен случайно вернуть либо “2”, либо “3” и соответствии с весом.
В 20% случаях выходит единица
В 20% двойка
И в 60% тройка.
Критерии оценки
Приложение должно запускаться, записывать значения в файл.


Toy Store Simulator

Описание
Это приложение моделирует работу магазина игрушек с использованием Java. В нем можно добавлять игрушки, определять частоту их выпадения и симулировать розыгрыши игрушек. Результаты розыгрышей записываются в файл.

Структура Проекта
Проект состоит из трех основных классов:

ToyItem - Класс, представляющий игрушку.
ToyStore - Класс, представляющий магазин игрушек и управляемый розыгрышем игрушек.
ToyStoreSimulator - Главный класс с методом main, который запускает симуляцию.
После выполнения программы в текущей директории должен появиться файл draw_results.txt. Откройте этот файл, чтобы увидеть результаты розыгрышей игрушек.

Примеры работы программы
Пример вывода в консоль:

Результаты успешно записаны в файл draw_results.txt
Пример содержимого draw_results.txt:

3
2
1
3
2
3
3
1
2
3
Каждая строка в файле draw_results.txt представляет собой ID игрушки, выбранной в соответствующем розыгрыше.

Заключение
Этот проект демонстрирует простую модель работы магазина игрушек и розыгрыш игрушек с разной частотой выпадения. Вы можете модифицировать код, добавляя больше функциональности или изменяя логику розыгрыша по своему усмотрению.