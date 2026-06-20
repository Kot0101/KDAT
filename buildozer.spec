[app]
title = KDAT
package.name = kdat
package.domain = org.kotoland
source.dir = .
source.include_exts = py,png,jpg,jpeg,ogg,wav,ttf,txt,json

# Версия 1.5
version = 1.5

# Чистые требования под Pygame
requirements = python3,pygame-ce,jnius,android

orientation = landscape
fullscreen = 1

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25c
android.archs = arm64-v8a
android.allow_backup = True
android.presplash_color = #000000
android.meta_data = android.app.lib_name=main

# Используем стабильную ветку релиза
p4a.branch = release-2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
