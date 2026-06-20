[app]
title = KDAT
package.name = kdat
package.domain = org.kot0101

source.dir = .
source.include_exts = py,png,jpg,jpeg,ogg,wav,ttf,txt,json

version = 0.1

# ВАЖНО: добавляем jnius и android. Они нужны для работы Pygame на Android
requirements = python3,pygame-ce,jnius,android

orientation = landscape
fullscreen = 1

# Архитектуры (для тестов на эмуляторе/телефоне лучше оставить armeabi-v7a и arm64-v8a)
android.archs = arm64-v8a, armeabi-v7a

# Стабильная связка API для Buildozer 1.5.0
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 23b

# Разрешения (если игре нужен интернет — раскомментируй)
# android.permissions = INTERNET

presplash.color = #000000