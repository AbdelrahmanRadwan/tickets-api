# Tickets System

## How to Run
- Install the requirements
```
pip3 install -r requirements.txt
```
- Run the Endpoint
```
python3 main.py
```
Route based URL: http://0.0.0.0:8080/

![System Design](https://github.com/AbdelrahmanRadwan/tickets-api/blob/master/design.png  "System Design")





📖 API
================

#### Examples:
##### POST Request sample
```http request
curl -X POST \
  http://0.0.0.0:8080/interviews_calendar/interviewer/add-slots \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{"interviewers": ["Morgan", "Geni mardoc", "JC-Quillet"], "start_times": ["12-1-2017 22:30", "01-01-2018 10:30"]}'
```


```http request
curl -X GET \
  http://0.0.0.0:8080/interviews_calendar/interviewee/available-times \
  -H 'cache-control: no-cache'
```


```http request
curl -X POST \
  http://0.0.0.0:8080/interviews_calendar/interviewee/available-times \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"interviewee": "interviewee name :)",
	"slot_id": 1
}'
```


```http request
curl -X GET \
  http://0.0.0.0:8080/interviews_calendar/admin/view-all \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json'
```
