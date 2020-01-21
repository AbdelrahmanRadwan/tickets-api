import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, jsonify, request
from tickets_system.tickets_system import TicketsSystem

app = Flask(__name__)
tickets_system = TicketsSystem()


@app.route('/', methods=['GET'])
def heartbeat():
    """
    A dummy route to check if the endpoints is up or not!
    :return:
    """
    return jsonify({})


@app.route('/interviews_calendar/interviewee/available-times', methods=['GET', 'POST'])
def available_times():
    """
    the interviewee's interface through the interviewer's schedule, from where he/she can view and select a slot
    :return: return the assigned time or the whole available times
    """
    req = request.get_json()
    if request.method == 'GET':
        response = interviews_calendar.get_available_slots()
        return jsonify(response)

    elif request.method == 'POST':
        interviewee = req["interviewee"]
        slot_id = req["slot_id"]
        response = interviews_calendar.set_interview(interviewee=interviewee, slot_id=slot_id)
        return jsonify(response)


app.run(debug=False, port=8080, host='0.0.0.0')  # Running on http://0.0.0.0:8080/
