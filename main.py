from flask import Flask, jsonify, request
from tickets_system.tickets_system import TicketsSystem

app = Flask(__name__)
tickets_system = TicketsSystem()


@app.route('/', methods=['GET'])
def heartbeat():
    """
    A dummy route to check if the endpoints are up or not!
    :return:
    """
    return jsonify({})


@app.route('/ticket', methods=['GET'])
def get_ticket():
    """
        Retrieve a tickets
    """
    ticket_id = request.args.get('id')
    response = tickets_system.get_ticket(ticket_id)
    return jsonify(response)


@app.route('/ticket', methods=['POST'])
def add_ticket():
    """
        Add/Generate a new ticket ot the system
    """
    response = tickets_system.add_ticket()
    return jsonify(response)


@app.route('/ticket/invalidate', methods=['UPDATE'])
def invalidate_ticket():
    """
        Add/Generate a new ticket ot the system
    """
    ticket_id = request.args.get('id')
    response = tickets_system.invalidate_ticket(ticket_id)
    return jsonify(response)


@app.route('/ticket/validate', methods=['UPDATE'])
def validate_ticket():
    """
        Add/Generate a new ticket ot the system
    """
    ticket_id = request.args.get('id')
    response = tickets_system.validate_ticket(ticket_id)
    return jsonify(response)


app.run(debug=False, port=8080, host='0.0.0.0')  # Running on http://0.0.0.0:8080/
