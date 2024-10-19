#!/usr/bin/env python3
# coding: utf8

import os

import eel

# Webディレクトリの初期化
eel.init(os.path.join(os.path.dirname(__file__), "web"))

# アプリケーションを起動
eel.start("index.html", size=(1000, 800))  # ウィンドウのサイズ設定
