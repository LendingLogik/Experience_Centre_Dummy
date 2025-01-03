// static/js/salesforce.js
function showLoading() {
    document.getElementById('loading').style.display = 'block';
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

function handleError(error) {
    const errorDiv = document.getElementById('error-message');
    errorDiv.textContent = error;
    errorDiv.style.display = 'block';
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 5000);
}
