[app]

# Название приложения на экране телефона
title = KDAT

# Имя пакета и домен (должны быть уникальными, без капса и спецсимволов)
package.name = kdat
package.domain = org.kotoland

# Где лежат исходники (точка означает текущую папку)
source.dir = .

# Расширения файлов, которые Buildozer упакует внутрь APK
source.include_exts = py,png,jpg,jpeg,ogg,wav,ttf,txt,json

# ВАЖНО: Смена версии на 0.4 принудительно очистит сломанный кэш на GitHub Actions
version = 0.5

# Чистый и стабильный набор требований для Pygame-CE
requirements = python3,pygame-ce,jnius,android

# Ориентация экрана (landscape - альбомная, portrait - портретная)
orientation = landscape

# Скрывать ли панель уведомлений телефона (1 — да, 0 — нет)
fullscreen = 1

# Стабильная связка Android API для сборщика
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25c

# Архитектуры процессоров, для которых собирается игра (только 64-бит ARM)
android.archs = arm64-v8a

# Разрешить бэкап данных приложения встроенными средствами Android
android.allow_backup = True

# Цвет фонового экрана при запуске приложения (черный)
android.presplash_color = #000000

# Инициализируем имя нативной библиотеки SDL2 в манифесте
android.meta_data = android.app.lib_name=main

# ВАЖНО: Уходим с сырого master на проверенный релизный тег с фиксом pthread_mutex
p4a.branch = release-2024.01.21

[buildozer]

# Уровень логов (2 — показывать всё, включая ошибки компилятора Си)
log_level = 2

# Предупреждать, если билд запущен от root-пользователя
warn_on_root = 1
