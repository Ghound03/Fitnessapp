// FitTrack Pro JavaScript

document.addEventListener("DOMContentLoaded", function () {
    const chartCanvas = document.getElementById("calorieChart");

    if (chartCanvas && typeof workoutLabels !== "undefined") {
        new Chart(chartCanvas, {
            type: "bar",
            data: {
                labels: workoutLabels,
                datasets: [
                    {
                        label: "Calories Burned",
                        data: calorieData
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: true
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
});