document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".table-reservation tbody");

    function getSelectedReservationType() {
        const selectedType = document.querySelector('input[name="res-type"]:checked').value;
        return selectedType;
    }

    function updateTableValues() {
        const selectedType = getSelectedReservationType();
        let newValue;

        switch (selectedType) {
            case '1':
                newValue = "30 zł";
                break;
            case '2':
                newValue = "0 zł";
                break;
            case '3':
                newValue = "80 zł";
                break;
            case '4':
                newValue = "20 zł";
                break;
            default:
                newValue = "30 zł";
        }

        const cells = document.querySelectorAll(".table-reservation td.res");
        cells.forEach(cell => {
            if (!cell.classList.contains("booked")) {
                cell.textContent = newValue;
            }
        });
    }

    table.addEventListener("click", function (e) {
        if (e.target.classList.contains("res")) {
            if (e.target.classList.contains("booked")) {
                alert("To pole jest już zarezerwowane.");
            } else {
                const reservationType = getSelectedReservationType();
                e.target.classList.toggle("selected");
                e.target.classList.remove("zwykla", "liga-format", "trening", "karnety");
                if (e.target.classList.contains("selected")) {
                    switch (reservationType) {
                        case '1':
                            e.target.classList.add("zwykla");
                            break;
                        case '2':
                            e.target.classList.add("liga-format");
                            break;
                        case '3':
                            e.target.classList.add("trening");
                            break;
                        case '4':
                            e.target.classList.add("karnety");
                            break;
                    }
                }
            }
        }
    });

    const form = document.getElementById("reservation-form");

    function getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length == 2) return parts.pop().split(";").shift();
    }
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const selected = document.querySelectorAll(".res.selected");
        console.log(selected)


        if (selected.length === 0) {
            alert("Proszę wybrać co najmniej jedną godzinę rezerwacji.");
            return;
        }

        selected.forEach(function (cell) {
            cell.classList.remove("selected");
            cell.classList.add("booked");
        });
        var listOfSelected = [...selected].map(a => a.id);
        console.log(listOfSelected)
        const createUrl = 'http://127.0.0.1:8000/reservations/api/create-reservation/'
        const token =
            fetch(createUrl, {
                method: "POST",
                body: JSON.stringify(listOfSelected),
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    "X-CSRFToken": getCookie("csrftoken")
                }
            }).then((response) => response.json())
                .then((json) => console.log(json))
        alert("Rezerwacja została złożona.");
    });

    function getWeekdays(startDate) {
        const weekdays = [];
        const days = ['Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'Sb', 'Nd'];

        for (let i = 0; i < 7; i++) {
            const date = new Date(startDate);
            date.setDate(startDate.getDate() + i);

            const today = new Date();
            today.setHours(0, 0, 0, 0);
            date.setHours(0, 0, 0, 0);

            const isToday = date.getTime() === today.getTime();
            weekdays.push({
                day: days[(date.getDay() + 6) % 7],
                date: date.toISOString().split('T')[0],
                isToday: isToday,
            });
        }
        return weekdays;
    }

    function generateWeekdays(startDate) {
        // const weekdays = getWeekdays(startDate);
        // const weekdaysContainer = document.querySelector(".box-weekdays");
        // weekdaysContainer.innerHTML = '';

        // weekdays.forEach((weekday) => {
        //     const li = document.createElement('li');
        //     li.className = `weekday${weekday.isToday ? ' active' : ''}`;
        //     li.setAttribute('data-date', weekday.date);
        //     li.textContent = weekday.day + (weekday.isToday ? ' (Dziś)' : '');
        //     li.addEventListener('click', function () {
        //         document.querySelectorAll('.weekday').forEach(day => day.classList.remove('active'));
        //         li.classList.add('active');
        //         setCurrentDate(weekday.date);
        //         resetTableSelections();
        //         updateTableValues();
        //     });
        //     weekdaysContainer.appendChild(li);
        // });
    }

    function setCurrentDate(dateStr) {
        document.querySelector(".current-date").textContent = dateStr || new Date().toISOString().split('T')[0];
    }

    function resetTableSelections() {
        const cells = document.querySelectorAll(".table-reservation td.res");
        cells.forEach(function (cell) {
            cell.classList.remove("selected", "booked", "zwykla", "liga-format", "trening", "karnety");
            cell.textContent = "30 zł";
        });
    }

    let currentWeekStartDate = new Date();
    currentWeekStartDate.setDate(currentWeekStartDate.getDate() - (currentWeekStartDate.getDay() + 6) % 7); // Ustaw na poniedziałek

    function updateWeek(direction) {
        const firstDayOfMonth = new Date(currentWeekStartDate.getFullYear(), currentWeekStartDate.getMonth(), 1);
        const lastDayOfMonth = new Date(currentWeekStartDate.getFullYear(), currentWeekStartDate.getMonth() + 1, 0);

        if (direction === 'prev') {
            currentWeekStartDate.setDate(currentWeekStartDate.getDate() - 7);
            if (currentWeekStartDate < firstDayOfMonth) {
                currentWeekStartDate = firstDayOfMonth;
            }
        } else if (direction === 'next') {
            currentWeekStartDate.setDate(currentWeekStartDate.getDate() + 7);
            if (currentWeekStartDate > lastDayOfMonth) {
                currentWeekStartDate = lastDayOfMonth;
            }
        }

        generateWeekdays(currentWeekStartDate);
    }

    document.querySelector('.prev-week').addEventListener('click', () => updateWeek('prev'));
    document.querySelector('.next-week').addEventListener('click', () => updateWeek('next'));

    generateWeekdays(currentWeekStartDate);
    setCurrentDate(new Date().toISOString().split('T')[0]);
    updateTableValues();

    document.querySelectorAll('input[name="res-type"]').forEach(input => {
        input.addEventListener('change', function () {
            resetTableSelections();
            updateTableValues();
        });
    });
});
