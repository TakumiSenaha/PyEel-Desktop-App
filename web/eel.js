function logToPython(message) {
    eel.log_message(message);
}

function pythonCall() {
    eel.python_function()((response) => {
        alert(response);  // Pythonからの応答を表示
    });
}
// 全ての時刻表データを表示する関数
function showAllTimetables() {
    eel.get_all_timetables()((response) => {
        console.log(response);  // コンソールに全データを表示
        logToPython(response);
        document.getElementById("all-timetables").innerText = JSON.stringify(response, null, 2);
    });
}

function showTimetable(date, stop) {
    // Pythonのget_timetable関数を呼び出し
    eel.get_timetable(date, stop)((response) => {
        console.log(response);  // コンソールに時刻表データを表示
        document.getElementById("timetable").innerText = response;
    });
}
