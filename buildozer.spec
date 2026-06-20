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

# ВАЖНО: Изменили на 0.3, чтобы заставить GitHub Actions полностью сбросить старый кэш библиотек
version = 0.3

# ВАЖНО: Убрали жесткую старую версию Python. Теперь ставится современный стабильный python3
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

# ВАЖНО: Переключаемся на актуальную ветку master, где исправлены краши FORTIFY pthread_mutex на Android 13+
p4a.branch = master

[buildozer]

# Уровень логов (2 — показывать всё, включая ошибки компилятора Си)
log_level = 2

# Предупреждать, если билд запущен от root-пользователя
warn_on_root = 1
