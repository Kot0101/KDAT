[app]

# Название приложения на экране телефона
title = KDAT

# Имя пакета и домен (должны быть уникальными, без капса и спецсимволов)
package.name = kdat
package.domain = org.kot0101

# Где лежат исходники (точка означает текущую папку)
source.dir = .

# Расширения файлов, которые Buildozer упакует внутрь APK
source.include_exts = py,png,jpg,jpeg,ogg,wav,ttf,txt,json

# Версия твоей игры
version = 0.1

# ВАЖНО: Фиксируем Python 3.10, рабочий pygame-ce и системные библиотеки для Android
requirements = python3==3.10.11,pygame-ce,jnius,android

# Ориентация экрана (landscape - альбомная, portrait - портретная)
orientation = landscape

# Скрывать ли панель уведомлений телефона (1 — да, 0 — нет)
fullscreen = 1

# Стабильная связка Android API для сборщика
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 23b

# Архитектуры процессоров, для которых собирается игра
android.archs = arm64-v8a, armeabi-v7a

# Разрешения (если игре понадобится интернет — раскомментируй строчку ниже)
# android.permissions = android.permission.INTERNET

# Цвет фонового экрана при запуске приложения (черный)
android.presplash_color = #000000

# Разрешить бэкап данных приложения встроенными средствами Android
android.allow_backup = True

[buildozer]

# Уровень логов (2 — показывать всё, включая ошибки компилятора Си)
log_level = 2

# Предупреждать, если билд запущен от root-пользователя
warn_on_root = 1