[app]
title = Ultra Music Player
package.name = ultramusic
package.domain = org.arman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
requirements = python3,kivy==2.2.1,kivymd==1.1.1,plyer,pyjnius,mutagen
version = 1.0.0
orientation = portrait
fullscreen = 0
android.permissions = READ_MEDIA_AUDIO,INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True
android.build_tools_version = 33.0.0
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 0
