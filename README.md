# PyEel-Desktop-App

このプロジェクトは、PythonのバックエンドとHTML/CSS/JavaScriptを組み合わせたモダンなEelベースのデスクトップアプリケーションです。

## セットアップ手順

### Minicondaを使用する場合の仮想環境でのセットアップ

#### 必要なツール
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) がインストールされている必要があります。

#### 手順

1. **プロジェクトをクローンする**

    ```bash
    git clone https://github.com/your-username/PyEel-Desktop-App.git
    cd PyEel-Desktop-App
    ```

2. **Conda環境を作成**

    `env.yml`ファイルを使用して、新しい仮想環境を作成します。

    ```bash
    conda env create -f env.yml
    ```

3. **環境をアクティベート**

    作成した仮想環境をアクティベートします。

    ```bash
    conda activate eel_env
    ```

4. **アプリケーションの実行**

    環境が整ったら、以下のコマンドでアプリケーションを起動します。

    ```bash
    python run.py
    ```

### 既にPythonがインストールされている場合（`requirements.txt`を使用）

#### 必要なツール
- Python 3.8 以上がインストールされている必要があります。

#### 手順
2, 3の仮想環境の構築は任意です。

1. **プロジェクトをクローンする**

    ```bash
    git clone https://github.com/your-username/PyEel-Desktop-App.git
    cd PyEel-Desktop-App
    ```

2. **仮想環境の作成（オプション）**

    仮想環境を手動で作成することをお勧めします。`venv`モジュールを使って仮想環境を作成します。

    ```bash
    python -m venv eel_env
    ```

3. **仮想環境のアクティベート**

    - **Windows**:
      ```bash
      eel_env\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source eel_env/bin/activate
      ```

4. **依存関係のインストール**

    `requirements.txt`ファイルを使用して、必要なパッケージをインストールします。

    ```bash
    pip install -r requirements.txt
    ```

5. **アプリケーションの実行**

    仮想環境がアクティブな状態で、以下のコマンドを使ってアプリケーションを起動します。

    ```bash
    python run.py
    ```

---

## 動作確認

アプリケーションが正常に起動すると、Eelベースのウィンドウが立ち上がり、簡単なUIが表示されます。ボタンをクリックすると、Pythonからのメッセージが表示されます。（2024年10月19日時点では何も返って来ません。）

---

## トラブルシューティング

1. **モジュールが見つからない**エラーが発生した場合は、依存関係が正しくインストールされていない可能性があります。以下を確認してください。

    ```bash
    pip install -r requirements.txt  # Pythonが既にある場合
    ```

    または

    ```bash
    conda env create -f env.yml  # Miniconda環境を使う場合
    ```

2. **仮想環境がアクティブでない**場合は、仮想環境を再度アクティベートしてください。
