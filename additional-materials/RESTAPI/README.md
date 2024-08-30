# What is REST?

REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on stateless, client-server communication and uses standard HTTP methods for interactions. Key principles of REST include:

- **Statelessness:** Each request from a client must contain all the information needed to process the request.
- **Client-Server Architecture:** Separation of client and server responsibilities.
- **Uniform Interface:** A consistent and uniform way of interacting with resources.
- **Cacheability:** Responses must explicitly indicate whether they are cacheable.
- **Layered System:** The API should be designed with layers, where each layer interacts only with the adjacent layer.

## HTTP Methods Used in REST

REST APIs use standard HTTP methods to perform operations on resources:

- **GET:** Retrieve data from the server.
- **POST:** Create a new resource on the server.
- **PUT:** Update an existing resource.
- **DELETE:** Remove a resource from the server.
- **PATCH:** Apply partial updates to a resource.

## Resources and Endpoints

- **Resource:** An entity or object that you interact with, such as a user or a product.
- **Endpoint:** A specific URL where resources are accessed.

## Status Codes

HTTP status codes indicate the result of an API request:

- **200 OK:** The request was successful.
- **201 Created:** A resource was successfully created.
- **204 No Content:** The request was successful, but there's no content to return.
- **400 Bad Request:** The request was invalid.
- **401 Unauthorized:** Authentication is required or failed.
- **403 Forbidden:** Access to the resource is denied.
- **404 Not Found:** The requested resource was not found.
- **500 Internal Server Error:** An error occurred on the server.
