function pythonCall() {
    eel.python_function()((response) => {
        alert(response);  // Pythonからの応答を表示
    });
}
