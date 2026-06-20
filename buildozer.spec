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

# Версия твоей игры
version = 0.2

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
android.ndk = 25c

# Архитектуры процессоров, для которых собирается игра
android.archs = arm64-v8a

# Разрешить бэкап данных приложения встроенными средствами Android
android.allow_backup = True

# Цвет фонового экрана при запуске приложения (черный)
android.presplash_color = #000000

android.meta_data = sdl.audio_driver=dummy

# ВАЖНО: Указываем стабильную ветку p4a ИМЕННО ЗДЕСЬ (внутри секции [app])
p4a.branch = release-2024.01.21

[buildozer]

# Уровень логов (2 — показывать всё, включая ошибки компилятора Си)
log_level = 2

# Предупреждать, если билд запущен от root-пользователя
warn_on_root = 1
