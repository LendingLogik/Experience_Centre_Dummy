class ChartManager {
    constructor() {
        this.chartElement = document.getElementById('main-chart');
    }

    async fetchData() {
        try {
            const response = await fetch('/api/data');
            return await response.json();
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    async renderChart() {
        const data = await this.fetchData();
        const trace = {
            x: data.x,
            y: data.y,
            type: 'scatter'
        };

        const layout = {
            title: 'Experience Center Analytics',
            responsive: true
        };

        Plotly.newPlot(this.chartElement, [trace], layout);
    }
}

// Initialize charts
document.addEventListener('DOMContentLoaded', () => {
    const chartManager = new ChartManager();
    chartManager.renderChart();
});
