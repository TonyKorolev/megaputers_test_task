Автотест написан на Python с помощью Selenium WebDriver.

Перед запуском необходимо: 
1. Установить Python.
2. Установить в Python библиотеку Selenium
> pip install selenium
3. Установить в Python библиотеку PyTest
> pip install pytest
---
Данный автотест считывает с файла "**employees_name.csv**" ФИО сотрудников, вводит их поочередно в поле поисковика на странице 
*<https://www.megaputer.ru/produkti/sertifikat/>* . Поисковик поочередно выдает список сертификатов, в которых отражены их названия и дата выдачи. Затем считываются названия и дата сертификатов и записываются в файл "**employees_name_with_sertificate.csv**" в формате:
> ФИО сотрудника, название сертификата, дата выдачи сертификата

Сам код автотеста находится в файле **test_sert_staff.py**.

Запуск автотеста возможен только в браузерах Google Chrome и Mozilla Firefox. В корне находятся папки chromedriver и geckodriver, в которых находятся драйвера для бразуеров Google Chrome и Mozilla Firefox соответственно. Автотест подхватывает файлы драйверов автоматически исходя из выбранного браузера.

Для запуска автотеста в браузере Google Chrome ввести в консоли:
> pytest -s -v --browser_name=chrome test_sert_staff.py

Для запуска автотеста в браузере Mozilla Firefox ввести в консоли:
> pytest -s -v --browser_name=firefox test_sert_staff.py