from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serving the frontend

@app.route('/api/commissions/create', methods=['POST'])
def create_commission():
    data = request.json
    commission = {
        "commission_type": data['commissionType'],
        "time_period": {
            "start_date": data['startDate'],
            "end_date": data['endDate']
        },
        "currency": data['currency'],
        "geo_zone": data['geoZone'],
        "commission_rate": data['commissionRate'],
        "transaction_types": data.get('transaction_types', []),  # Corrected key
        "threshold": {
            "min_amount": data['minAmount'],
            "max_amount": data['maxAmount']  # Corrected to match frontend
        }
    }
    return jsonify({
        "status": "success",
        "message": "Commission structure created successfully",
        "data": commission
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

