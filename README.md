cat > README.md << 'EOF'
# alx_travel_app_0x00

This is a Django project for a travel application, focusing on property listings, bookings, and reviews.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/alx_travel_app_0x00.git](https://github.com/your-username/alx_travel_app_0x00.git)
    cd alx_travel_app_0x00/alx_travel_app
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Windows: .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt # Make sure you have a requirements.txt, or install manually: pip install Django djangorestframework
    ```

4.  **Apply database migrations:**
    ```bash
    python3 manage.py makemigrations listings
    python3 manage.py migrate
    ```

5.  **Seed the database with sample data:**
    This command will populate your database with example listings, bookings, and reviews. It will also create a default superuser (`admin`/`adminpassword`) if no users exist.
    ```bash
    python3 manage.py seed
    ```

6.  **Create a superuser (if you skipped seeding or want another admin):**
    ```bash
    python3 manage.py createsuperuser
    ```

7.  **Run the development server:**
    ```bash
    python3 manage.py runserver
    ```
    The application should now be accessible at `http://127.0.0.1:8000/`.

## Database Models

This project includes the following core models:

* **`Listing`**: Represents a property available for booking.
    * `title`, `description`, `address`, `city`, `country`, `price_per_night`, `max_guests`, `bedrooms`, `bathrooms`, `amenities`, `is_active`, `created_at`, `updated_at`.
* **`Booking`**: Represents a reservation made for a `Listing`.
    * `listing` (ForeignKey to Listing), `guest` (ForeignKey to User), `check_in_date`, `check_out_date`, `total_price`, `status`, `created_at`, `updated_at`.
* **`Review`**: Represents a review provided by a `guest` for a `Booking`.
    * `booking` (OneToOneField to Booking), `guest` (ForeignKey to User), `rating`, `comment`, `created_at`, `updated_at`.

## API Endpoints (Future)

## Data Seeding

The project includes a custom Django management command to seed the database:

* **`python3 manage.py seed`**: Populates the database with sample `Listing`, `Booking`, and `Review` data. It also creates some default users if none exist.
EOF
