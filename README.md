Автотест написан на Python с помощью Selenium.

Данный автотест считывает с файла "**employees_name.csv**" ФИО сотрудников, вводит их поочередно в поле поисковика на странице 
*<https://www.megaputer.ru/produkti/sertifikat/>* . Поисковик поочередно выдает список сертификатов, в которых отражены их названия и дата выдачи. Затем считываются названия и дата сертификатов и записываются в файл "**employees_name_with_sertificate.csv**" в формате:
> ФИО сотрудника, название сертификата, дата выдачи сертификата

Сам автотест находится в файле **test_sert_staff.py**.

Запуск автотеста возможен в браузерах Google Chrome и Mozilla Firefox. 

Для запуска автотеста в браузере Google Chrome ввести в консоли:
> pytest -s -v --browser_name=chrome test_sert_staff.py

Для запуска автотеста в браузере Mozilla Firefox ввести в консоли:
> pytest -s -v --browser_name=firefox test_sert_staff.py