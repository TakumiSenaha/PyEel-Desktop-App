// Pythonのログ関数を呼び出す
function logToPython(message) {
    eel.log_message(message);
}

// Pythonの関数を直接呼び出すテスト用関数
function pythonCall() {
    eel.python_function()((response) => {
        alert(response);
    });
}

// 全ての時刻表データを表示する関数
function showAllTimetables() {
    eel.get_all_timetables()((response) => {
        console.log(response);
        logToPython("Displaying all timetables");
        document.getElementById("all-timetables").innerText = JSON.stringify(response, null, 2);
    });
}

// 日付と出発地点を指定して時刻表を表示する関数
function showTimetable(date, startLocation) {
    eel.get_timetable(date, startLocation)((response) => {
        console.log(response);
        logToPython(`Timetable for ${date} at ${startLocation}: ${response}`);
        document.getElementById("timetable").innerText = response;
    });
}

// バス停リストを取得して選択メニューを設定する関数
function populateBusStops() {
    eel.get_bus_stops()((busStops) => {
        const stopSelect = document.getElementById("stop");
        stopSelect.innerHTML = "";
        busStops.forEach(stop => {
            const option = document.createElement("option");
            option.value = stop;
            option.textContent = stop;
            stopSelect.appendChild(option);
        });
    });
}

// ページが読み込まれたときにバス停リストを設定
document.addEventListener("DOMContentLoaded", populateBusStops);
