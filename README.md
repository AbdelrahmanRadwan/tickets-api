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
## Scalable System Design
![System Design](https://github.com/AbdelrahmanRadwan/tickets-api/blob/master/system_design/design.png  "System Design")

📖 API
================
## Create a new ticket
```http request
curl -X POST http://0.0.0.0:8080/ticket -H 'cache-control: no-cache' -H 'content-type: application/json'
```
*Response*
```
{
"id":"22535006-3c3e-11ea-8e4c-8c1645e0f94e",
"timestamp":1579604814.9747176
}
```

## Retrieve a ticket or all tickets
```http request
curl -X GET http://0.0.0.0:8080/ticket?id="22535006-3c3e-11ea-8e4c-8c1645e0f94e"
```
*Response*
```
{
"tickets":[
    {
        "id":"22535006-3c3e-11ea-8e4c-8c1645e0f94e",
        "timestamp":1579604814.9747176
    }
]}
```

