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
    "id":"4fcd3656-3c79-11ea-8e4c-8c1645e0f94e",
    "timestamp":1579630231.5780213,
    "valid":true
}

```

## Retrieve a ticket or all tickets
```http request
curl -X GET http://0.0.0.0:8080/ticket?id="fbee5350-3c7b-11ea-8e4c-8c1645e0f94e"
```
*Response*
```
[
    {
        "id":"fbee5350-3c7b-11ea-8e4c-8c1645e0f94e",
        "timestamp":1579631379.3566003,
        "valid":true
    }
]
```
```http request
curl -X GET http://0.0.0.0:8080/ticket
```
```buildoutcfg
[
   {
      'id':UUID(      'ab3fa18e-3c7b-11ea-8e4c-8c1645e0f94e'      ),
      'valid':True,
      'timestamp':1579631243.9940078
   },
   {
      'id':UUID(      'ab3fa18f-3c7b-11ea-8e4c-8c1645e0f94e'      ),
      'valid':True,
      'timestamp':1579631243.9940224
   },
   {
      'id':UUID(      'ab3fa190-3c7b-11ea-8e4c-8c1645e0f94e'      ),
      'valid':True,
      'timestamp':1579631243.9940288
   },
   {
      'id':UUID(      'ab3fa191-3c7b-11ea-8e4c-8c1645e0f94e'      ),
      'valid':True,
      'timestamp':1579631243.994033
   },
   {
      'id':UUID(      'ab3fa192-3c7b-11ea-8e4c-8c1645e0f94e'      ),
      'valid':True,
      'timestamp':1579631243.9940372
   }
]
```
# Invalidate a ticket
```http request
curl -X UPDATE http://0.0.0.0:8080/ticket/invalidate?id="d9d961be-3c7c-11ea-8e4c-8c1645e0f94e"
```
```buildoutcfg
{
    "id":"d9d961be-3c7c-11ea-8e4c-8c1645e0f94e",
    "timestamp":1579631751.6735783,
    "valid":false
}
```
# Validate a ticket
```http request
curl -X UPDATE http://0.0.0.0:8080/ticket/validate?id="d9d961be-3c7c-11ea-8e4c-8c1645e0f94e"
```
```buildoutcfg
{
    "id":"d9d961be-3c7c-11ea-8e4c-8c1645e0f94e",
    "timestamp":1579631751.6735783,
    "valid":true
}
```