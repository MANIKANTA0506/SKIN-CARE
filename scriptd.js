document.addEventListener('DOMContentLoaded', function () {
    const days = 30;

    // Unlock days based on local storage
    for (let i = 1; i <= days; i++) {
        if (localStorage.getItem(`day${i}Completed`)) {
            document.getElementById(`day${i}`).classList.remove('disabled');
        }
    }

    // Unlock the next day if the previous day is completed
    for (let i = 1; i < days; i++) {
        if (localStorage.getItem(`day${i}Completed`)) {
            document.getElementById(`day${i+1}`).classList.remove('disabled');
        }
    }
});
