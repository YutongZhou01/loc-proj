## JSON Formatting for all API Endpoints

The purpose of this document is to provide structure for how all API endpoints should return JSON data to the frontend (files and other binary data may need to be handled differently, that's ok)

Below is an example of how the JSON should be structured. All returned JSON data should have a "success" property (a boolean) and a "data" property (a JSON object). 

```json
{
    "success": true,
    "data" : {
        "documentID": "4c4a9aba9780b3c956bafdf9bd631a5f",
        "fileURL": "www.example.com/document.pdf",
        "filetype": "application/pdf"
    }
}
```

- The success property is a boolean used to inform the client if the request was a success or not, even if the HTTP status code was 200.
- The data property is used to return any extra information or data to the user. What is contained within it will differ depending on the endpoint, but generally all GET requests should return something in here. POST requests may leave this empty, as they may not need to return any data.

If a request is not successful (success = false), then a "reason" property should be provided. This provides information to both the user and the client as to why the request failed and potentially how to remedy the issue. See below for an example on how this might be formatted:

```json
{
    "success": false,
    "reason": "The required parameters were not supplied in the request",
    "data" : {}
}
```