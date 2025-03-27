document.addEventListener("DOMContentLoaded", function () {
    const institutionInput = document.getElementById("institution");
    const ctxOriginal = document.getElementById("originalChart").getContext("2d");
    const ctxComparison = document.getElementById("comparisonChart").getContext("2d");
    
    let originalChartInstance = null;
    let comparisonChartInstance = null;

    function fetchData(instnm) {
        if (!instnm) return;
        fetch(`/highered/api/data/?instnm=${encodeURIComponent(instnm)}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error("Error:", data.error);
                    return;
                }

                // Extract institution data (Original Chart)
                const institutionData = data.institution_data;
                const years = institutionData.map(d => d.YEAR);
                const admissions = institutionData.map(d => d.ADMSSN);
                const enrollments = institutionData.map(d => d.ENRLT);
                const admissionRates = institutionData.map(d => d.ADMISSIONRATE);
                const enrollmentRates = institutionData.map(d => d.ENROLLMENTRATE);

                // Update Original Chart
                if (originalChartInstance) originalChartInstance.destroy();
                originalChartInstance = new Chart(ctxOriginal, {
                    type: "bar",
                    data: {
                        labels: years,
                        datasets: [
                            { 
                                label: "Admissions", 
                                data: admissions, 
                                backgroundColor: "blue",
                                zIndex: 1,  // Lower zIndex for bars
                                datalabels: {
                                    display: false // Hide data labels for bars
                                }
                            },
                            { 
                                label: "Enrollments", 
                                data: enrollments, 
                                backgroundColor: "green",
                                zIndex: 1,  // Lower zIndex for bars
                                datalabels: {
                                    display: false // Hide data labels for bars
                                }
                            },
                            { 
                                label: "Admission Rate", 
                                data: admissionRates, 
                                type: "line", 
                                borderColor: "red", 
                                yAxisID: "y1",
                                zIndex: 2,  // Higher zIndex for lines
                                datalabels: {
                                    anchor: 'end',
                                    align: 'top',
                                    color: 'black',
                                    font: {
                                        weight: 'bold'
                                    },
                                    formatter: function(value) {
                                        return value + '%'; // Add percentage to the labels
                                    }
                                }
                            },
                            { 
                                label: "Enrollment Rate", 
                                data: enrollmentRates, 
                                type: "line", 
                                borderColor: "orange", 
                                yAxisID: "y1",
                                zIndex: 2,  // Higher zIndex for lines
                                datalabels: {
                                    anchor: 'end',
                                    align: 'top',
                                    color: 'black',
                                    font: {
                                        weight: 'bold'
                                    },
                                    formatter: function(value) {
                                        return value + '%'; // Add percentage to the labels
                                    }
                                }
                            },
                        ]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: { beginAtZero: true, title: { display: true, text: "Count" } },
                            y1: { beginAtZero: true, position: "right", title: { display: true, text: "Rate (%)" } }
                        },
                        plugins: {
                            datalabels: {
                                display: false // Hide data labels by default for non-rate datasets
                            }
                        }
                    },
                    plugins: [ChartDataLabels] // Ensure the plugin is applied to the chart
                });

                // Extract comparison data (Comparison Chart)
                const comparisonData = data.comparison_data;
                const comparisonYears = [...new Set(comparisonData.map(item => item.YEAR))].sort();

                // Group data by institution
                const institutions = [...new Set(comparisonData.map(item => item.INSTNM))];
                const datasets = institutions.map((institution, index) => {
                    const institutionData = comparisonData.filter(item => item.INSTNM === institution);
                    const rates = comparisonYears.map(year => {
                        const record = institutionData.find(d => d.YEAR === year);
                        return record ? record.ADMISSIONRATE : null;
                    });

                    return {
                        label: institution,
                        data: rates,
                        borderColor: `hsl(${index * 60}, 70%, 50%)`,
                        backgroundColor: `hsl(${index * 60}, 70%, 50%, 0.2)`,
                        borderWidth: 2,
                        fill: false,
                        zIndex: 2,  // Set a higher zIndex for the lines (on top)
                        datalabels: {
                            anchor: 'end',
                            align: 'top',
                            color: 'black',
                            font: {
                                weight: 'bold'
                            },
                            formatter: function(value) {
                                return value + '%'; // Add percentage to the labels
                            }
                        }
                    };
                });

                // Update Comparison Chart
                if (comparisonChartInstance) comparisonChartInstance.destroy();
                comparisonChartInstance = new Chart(ctxComparison, {
                    type: "line",
                    data: {
                        labels: comparisonYears,
                        datasets: datasets
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            title: {
                                display: true,
                                text: "Admission Rate Comparison (Sector & State)"
                            },
                            tooltip: {
                                mode: "index",
                                intersect: false
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 100,
                                title: { display: true, text: "Admission Rate (%)" }
                            }
                        },
                        plugins: {
                            datalabels: {
                                display: false // Hide data labels by default for non-rate datasets
                            }
                        }
                    },
                    plugins: [ChartDataLabels] // Ensure the plugin is applied to the chart
                });
            })
            .catch(error => console.error("Error fetching data:", error));
    }

    institutionInput.addEventListener("change", function () {
        fetchData(this.value);
    });
});

var ctx = document.getElementById('admissionChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'bar', // You can use 'line', 'bar', or both
    data: {
        labels: ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'], // Sample data labels
        datasets: [{
            label: 'Admissions',
            data: [100, 200, 150, 170, 220, 250, 190, 210, 230], // Sample data for admissions
            backgroundColor: 'rgba(0,123,255,0.5)',
            borderColor: 'rgba(0,123,255,1)',
            borderWidth: 1,
            zIndex: 1, // Set a lower zIndex for the bars
            datalabels: {
                display: false // Hide data labels for bars
            }
        }, {
            label: 'Enrollment',
            data: [80, 180, 130, 160, 200, 240, 180, 200, 210], // Sample data for enrollment
            backgroundColor: 'rgba(40,167,69,0.5)',
            borderColor: 'rgba(40,167,69,1)',
            borderWidth: 1,
            zIndex: 1, // Set a lower zIndex for the bars
            datalabels: {
                display: false // Hide data labels for bars
            }
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            datalabels: {
                display: false // Hide data labels by default for non-rate datasets
            }
        }
    },
    plugins: [ChartDataLabels] // Ensure the plugin is applied to the chart
});
