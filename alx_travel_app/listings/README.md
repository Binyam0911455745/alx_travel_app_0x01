\# alx\_travel\_app\_0x01



\## API Endpoints



The following RESTful API endpoints are available for managing listings and bookings:



\### Listings

\- \*\*Base URL:\*\* `/api/listings/`

\- \*\*GET /\*\*: List all available listings.

\- \*\*POST /\*\*: Create a new listing (Authentication Required).

&nbsp; - Request Body (JSON): `{"title": "string", "description": "string", "price\_per\_night": "decimal", "is\_available": "boolean"}`

\- \*\*GET /{id}/\*\*: Retrieve a specific listing by ID.

\- \*\*PUT /{id}/\*\*: Update an existing listing by ID (Authentication Required).

\- \*\*PATCH /{id}/\*\*: Partially update an existing listing by ID (Authentication Required).

\- \*\*DELETE /{id}/\*\*: Delete a listing by ID (Authentication Required).



\### Bookings

\- \*\*Base URL:\*\* `/api/bookings/`

\- \*\*GET /\*\*: List bookings (Authentication Required. Users see their own bookings; Staff/Admin see all).

\- \*\*POST /\*\*: Create a new booking (Authentication Required. `guest` field is automatically set to the current user).

&nbsp; - Request Body (JSON): `{"listing": "id\_of\_listing", "start\_date": "YYYY-MM-DD", "end\_date": "YYYY-MM-DD"}`

\- \*\*GET /{id}/\*\*: Retrieve a specific booking by ID (Authentication Required. Users can only retrieve their own).

\- \*\*PUT /{id}/\*\*: Update an existing booking by ID (Authentication Required. Users can only update their own).

\- \*\*PATCH /{id}/\*\*: Partially update an existing booking by ID (Authentication Required. Users can only update their own).

\- \*\*DELETE /{id}/\*\*: Delete a booking by ID (Authentication Required. Users can only delete their own).



\### API Documentation

\- \*\*Swagger UI:\*\* `/swagger/`

\- \*\*Redoc:\*\* `/redoc/`

