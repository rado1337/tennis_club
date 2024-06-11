document.addEventListener("DOMContentLoaded", function () {
    const table = document.querySelector(".table-reservation tbody");

    // Pobierz aktualnie wybrany typ rezerwacji
    function getSelectedReservationType() {
        const selectedType = document.querySelector('input[name="res-type"]:checked').value;
        return selectedType;
    }

    // Funkcja do zmiany wartości wyświetlanej w tabeli w zależności od typu rezerwacji
    function updateTableValues() {
        const selectedType = getSelectedReservationType();
        let newValue;

        switch (selectedType) {
            case '1':
                newValue = "30 zł"; // Zwykła
                break;
            case '2':
                newValue = "0 zł"; // Liga Format
                break;
            case '3':
                newValue = "80 zł"; // Trening
                break;
            case '4':
                newValue = "20 zł"; // Club Card
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

    // Obsługa kliknięcia na polu rezerwacji
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
    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const selected = document.querySelectorAll(".res.selected");

        if (selected.length === 0) {
            alert("Proszę wybrać co najmniej jedną godzinę rezerwacji.");
            return;
        }

        selected.forEach(function (cell) {
            cell.classList.remove("selected");
            cell.classList.add("booked");
        });

        alert("Rezerwacja została złożona.");
    });

    // Funkcja do pobrania dni tygodnia
    function getWeekdays(startDate) {
        const weekdays = [];
        const days = ['Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'Sb', 'Nd'];
        for (let i = 0; i < 7; i++) {
            const date = new Date(startDate);
            date.setDate(startDate.getDate() + i);
            const isToday = date.toDateString() === new Date().toDateString();
            weekdays.push({
                day: days[(i + 1) % 7], // Start od poniedziałku
                date: date.toISOString().split('T')[0],
                isToday: isToday,
            });
        }
        return weekdays;
    }

    // Funkcja do generowania listy dni tygodnia
    function generateWeekdays(startDate) {
        const weekdays = getWeekdays(startDate);
        const weekdaysContainer = document.querySelector(".box-weekdays");
        weekdaysContainer.innerHTML = ''; // Czyść istniejący kontent

        weekdays.forEach((weekday) => {
            const li = document.createElement('li');
            li.className = `weekday${weekday.isToday ? ' active' : ''}`;
            li.setAttribute('data-date', weekday.date);
            li.textContent = weekday.day + (weekday.isToday ? ' (Dziś)' : '');
            li.addEventListener('click', function () {
                document.querySelectorAll('.weekday').forEach(day => day.classList.remove('active'));
                li.classList.add('active');
                setCurrentDate(weekday.date);
                resetTableSelections(); // Resetuje zaznaczenia w tabeli
                updateTableValues(); // Aktualizuje wartości w tabeli
            });
            weekdaysContainer.appendChild(li);
        });
    }

    // Funkcja do ustawienia aktualnej daty
    function setCurrentDate(dateStr) {
        document.querySelector(".current-date").textContent = dateStr || new Date().toISOString().split('T')[0];
    }

    // Funkcja do resetowania zaznaczeń w tabeli rezerwacji
    function resetTableSelections() {
        const cells = document.querySelectorAll(".table-reservation td.res");
        cells.forEach(function (cell) {
            cell.classList.remove("selected", "booked", "zwykla", "liga-format", "trening", "karnety");
            cell.textContent = "30 zł"; // Przywróć domyślną wartość tekstu
        });
    }

    // Obsługa zmiany tygodni
    let currentWeekStartDate = new Date();

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

    // Wygeneruj dni tygodnia i ustaw aktualną datę
    generateWeekdays(currentWeekStartDate);
    setCurrentDate();
    updateTableValues(); // Ustaw wartość tabeli na podstawie domyślnego typu rezerwacji

    // Nasłuchiwanie na zmianę typu rezerwacji
    document.querySelectorAll('input[name="res-type"]').forEach(input => {
        input.addEventListener('change', function () {
            resetTableSelections(); // Resetuje zaznaczenia w tabeli przy zmianie typu rezerwacji
            updateTableValues(); // Aktualizuje wartości w tabeli przy zmianie typu rezerwacji
        });
    });
});
