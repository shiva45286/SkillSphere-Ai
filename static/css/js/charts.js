// =========================================
// Skill Distribution Chart
// =========================================

const skillsCanvas =
    document.getElementById("skillsChart");

if (skillsCanvas) {

    new Chart(skillsCanvas, {

        type: "bar",

        data: {

            labels: [
                "Python",
                "Java",
                "SQL",
                "Machine Learning",
                "Web Development"
            ],

            datasets: [{

                label: "Skill Level",

                data: [
                    90,
                    70,
                    80,
                    65,
                    85
                ],

                backgroundColor: [
                    "#3B82F6",
                    "#10B981",
                    "#F59E0B",
                    "#EF4444",
                    "#8B5CF6"
                ],

                borderWidth: 1

            }]
        },

        options: {

            responsive: true,

            plugins: {

                title: {

                    display: true,

                    text: "Skill Distribution"

                }
            }
        }
    });
}


// =========================================
// Career Readiness Doughnut
// =========================================

const careerCanvas =
    document.getElementById("careerChart");

if (careerCanvas) {

    new Chart(careerCanvas, {

        type: "doughnut",

        data: {

            labels: [
                "Completed",
                "Remaining"
            ],

            datasets: [{

                data: [
                    75,
                    25
                ],

                backgroundColor: [
                    "#10B981",
                    "#E5E7EB"
                ]
            }]
        },

        options: {

            responsive: true,

            plugins: {

                title: {

                    display: true,

                    text:
                    "Career Readiness Score"
                }
            }
        }
    });
}


// =========================================
// Learning Progress Chart
// =========================================

const progressCanvas =
    document.getElementById("progressChart");

if (progressCanvas) {

    new Chart(progressCanvas, {

        type: "line",

        data: {

            labels: [
                "Week 1",
                "Week 2",
                "Week 3",
                "Week 4"
            ],

            datasets: [{

                label:
                "Learning Progress",

                data: [
                    20,
                    40,
                    65,
                    90
                ],

                fill: false,

                borderColor:
                "#2563EB",

                tension: 0.4

            }]
        },

        options: {

            responsive: true,

            plugins: {

                title: {

                    display: true,

                    text:
                    "Learning Progress"
                }
            }
        }
    });
}


// =========================================
// Certificate Platform Chart
// =========================================

const certificateCanvas =
    document.getElementById(
        "certificateChart"
    );

if (certificateCanvas) {

    new Chart(certificateCanvas, {

        type: "pie",

        data: {

            labels: [
                "Coursera",
                "Udemy",
                "NPTEL",
                "Infosys Springboard"
            ],

            datasets: [{

                data: [
                    5,
                    3,
                    2,
                    1
                ],

                backgroundColor: [

                    "#3B82F6",
                    "#10B981",
                    "#F59E0B",
                    "#EF4444"
                ]
            }]
        },

        options: {

            responsive: true,

            plugins: {

                title: {

                    display: true,

                    text:
                    "Certificate Platforms"
                }
            }
        }
    });
}