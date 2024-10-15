document.getElementById('commissionForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = {
        commissionType: document.getElementById('commissionType').value,
        startDate: document.getElementById('startDate').value,
        endDate: document.getElementById('endDate').value,
        currency: document.getElementById('currency').value,
        geoZone: document.getElementById('geoZone').value,
        commissionRate: document.getElementById('commissionRate').value,
        minAmount: document.getElementById('minAmount').value,
        maxAmount: document.getElementById('maxAmount').value
    };

    const response = await fetch('/api/commissions/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    });

    const result = await response.json();

    // Display the JSON result in a formatted popup alert
    alert(JSON.stringify(result.data, null, 2));  // Pretty-print JSON in alert
});
