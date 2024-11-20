# Scribeo Backend

The backend of **Scribeo**, a user blog management platform, is built with Django, Django REST Framework, and PostgreSQL. It provides APIs for user authentication, blog CRUD operations, and image uploading. 

---

## Features

1. **User Authentication & Authorization**:
   - User registration and login using JSON Web Tokens (JWT).
   - Role-based access: Only authenticated users can create, update, and delete their own posts.

2. **Post Management**:
   - CRUD operations for blog posts.
   - Validation for title, content, and image uploads.

3. **Image Uploading**:
   - Secure storage of images via **Cloudinary**.
   - Integration with posts.

4. **Database**:
   - PostgreSQL for structured data storage.
   - Optimized schema for user and blog data relationships.

5. **Production-Ready Deployment**:
   - Gunicorn as the WSGI server.
   - Dockerized setup for easy deployment.

---

## Installation & Setup

### Prerequisites:
- Python 3.10+
- PostgreSQL
- Docker (Optional for containerized deployment)

### Steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd scribeo-backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgresql://user:password@localhost/db_name
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=your_db_port
   ALLOWED_HOSTS=your_allowed_hosts
   CLOUDINARY_API_KEY=your_cloudinary_api_key
   CLOUDINARY_API_SECRET=your_cloudinary_secret_key
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. (Optional) Start using Docker:
   ```bash
   docker build -t scribeo-backend .
   docker run -p 8000:8000 scribeo-backend
   ```

---

## Dependencies

Refer to `requirements.txt`:
- Django
- Django REST Framework
- PostgreSQL driver (`psycopg2-binary`)
- JWT for authentication
- Docker and Gunicorn for deployment

---
