#Проект автоматизации тестирования API Яндекс.Самокат

Основа для написания автотестов — фреймворк pytest и библиотека requests.
Отчёты формируются в Allure.

##Установка

pip install -r requirements.txt

##Запуск тестов

pytest --alluredir=allure_results

##Генерация отчёта

allure generate allure_results -o allure-report --clean