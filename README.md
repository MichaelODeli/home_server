<!-- alt+m hotkey -->
# Документация по проекту 'Home server'
## Содержание
0. [Содержание](#содержание)
1. [О проекте.](#о-проекте)
1. [Структура проекта.](#структура-проекта)
1. [Установка и необходимые зависимости.](#установка-и-необходимые-зависимости)
1. [Запуск и работа проекта.](#запуск-и-работа-проекта)
1. [Управление системами проекта.](#управление-системами-проекта)
    - [Панель для удаленного управления.](#панель-для-удаленного-управления)
    - [Панель для локального управления.](#панель-для-локального-управления)
1. [Модуль 1. Загрузчик торрентов.](#модуль-1-загрузчик-торрентов)
1. [Модуль 2. Менеджер файлов.](#модуль-2-менеджер-файлов)
1. [Модуль 3. Менеджер подписок.](#модуль-3-менеджер-подписок)
1. [Модуль 4. Системный монитор.](#модуль-4-системный-монитор)
1. [Модуль 5. Сортировщик данных.](#модуль-5-сортировщик-данных)
1. [Модуль 6. Видеонаблюдение.](#модуль-6-видеонаблюдение)
1. [Модуль 7. Поиск.](#модуль-7-поиск)
1. [Модуль 8. Видеоплеер.](#модуль-8-видеоплеер)

## О проекте.
Система управления умным домом.   

## Структура проекта.
Проект представляет собой объединение некоторых репозиториев, для более удобного управления   
[Библиотека 'File sorter'](https://github.com/MichaelODeli/home_server-filesorter)   
[localGUI-PC](https://github.com/MichaelODeli/home_server-localGUI)   
[Информационный репозиторий](https://github.com/MichaelODeli/home_server)   

### Клиент:
[localGUI-PC](https://github.com/MichaelODeli/home_server-localGUI) может быть полноценно запущен с клиентского устройства с минимальным разрешением 1024*600. Включает все необходимые библиотеки   
Структура файлов:
```
localGUI-PC/
    localScreenGUI.py
    settings.ini
```
### Сервер:
Структура файлов:
```
server-side/
    cgi-bin/
        HTML.py
        search.py
        settings.ini.symlink
        fileSearch.py.symlink
        fileManager.py.symlink
        storageLib_Yt.ini.symlink
        storageLib_Films.ini.symlink
        storageLib_Serials.ini.symlink
    storage/
        youtube/
            channel-name/*.mp4
        serials/
            serial-name/*.mp4
        films/
            films-category/*.mp4
        settings.ini
        fileSearch.py
        fileManager.py
        storageLib_Yt.ini
        storageLib_Films.ini
        storageLib_Serials.ini
        mklinks.py
    subs_manager/
        engine.py
    system_stats/    
        engine.py
    index.html
    search.html
```
> Обратите внимание, папка server-side должна быть прописана в конфигурации apache2 как домашняя директория.    
> Файлы с припиской `.symlink` относятся к своим оригиналам без данной приписки
## Установка и необходимые зависимости.
WIP

## Запуск и работа проекта.
WIP

## Управление системами проекта.
WIP

### Панель для удаленного управления.
PySimpleGUIWeb (Remi)

### Панель для локального управления.
PySimpleGUI (TKinter)

## Модуль 1. Загрузчик торрентов.
#### Используемые зависимости
`qbittorrent`
#### Стуктура кода
Описание
#### Использование
Вкладка 'Torrents'

## Модуль 2. Менеджер файлов.
#### Используемые зависимости
Встроенная библиотека `torrentSorter`
#### Стуктура кода
Описание
#### Использование
Библиотека запускается автоматически, после завершения загрузки торрент-файлов

## Модуль 3. Менеджер подписок.
#### Используемые зависимости
Встроенная библиотека `subsManager`
#### Стуктура кода
Описание
#### Использование
Вкладка 'Subs'

## Модуль 4. Системный монитор.
#### Используемые зависимости
Сторонняя библиотека `psutil`
#### Стуктура кода
По нажатию пользователем кнопки 'Update stats', происходит обновление системных показателей - потребление ОЗУ и процент нагрузки ЦП. Данные запрашиваются с помощью библиотеки `psutil`
#### Использование
Вкладка 'Stats'

## Модуль 5. Сортировщик данных.
#### Используемые зависимости
Встроенная библиотека `fileManager`
#### Стуктура кода
Описание
#### Использование
Вкладка 'Video' / Кнопки Rebuild lists

## Модуль 6. Видеонаблюдение.
#### Используемые зависимости
WIP
#### Стуктура кода
WIP
#### Использование
WIP

## Модуль 7. Поиск.
#### Используемые зависимости
Встроенная библиотека `fileSearch`
#### Стуктура кода
Описание
#### Использование
Вкладка 'Search'

## Модуль 8. Видеоплеер.
#### Используемые зависимости
`vlc`
#### Стуктура кода
Описание
#### Использование
Вкладка 'Video'
