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

# Версия проекта (сбрасывает старый кэш на GitHub Actions)
version = 0.3

# Современный стабильный python3 и pygame-ce
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

# ХАРДКОРНЫЙ КОСТЫЛЬ ГРАФИКИ: Передаем переменные среды SDL2 прямо в Java-слой при старте
android.environment = SDL_RENDER_DRIVER=software,SDL_VIDEO_GL_DRIVER="",SDL_VIDEO_GLES_DRIVER="",SDL_VIDEO_EGL_ALLOW_EGLATTRS="0"

# ВАЖНО: Актуальная ветка master, где исправлены краши FORTIFY на Android 13+
p4a.branch = master

[buildozer]

# Уровень логов (2 — показывать всё, включая ошибки компилятора Си)
log_level = 2

# Предупреждать, если билд запущен от root-пользователя
warn_on_root = 1
