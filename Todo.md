# TODO List

## 1. Project Setup
- [x] Set up the project directory structure for a **FastAPI** application.
- [x] Create a Python virtual environment (`venv` or `conda`) for isolated development.
- [x] Install FastAPI and essential dependencies:
  - `fastapi`
  - `uvicorn[standard]` (for running the FastAPI app)
  - `sqlalchemy` (for database interactions)
  - `pydantic` (for validation and settings)
  - `cadquery` (for geometry generation)
  - `numpy`
  - `pytest`
- [x] Initialise a Git repository and push to GitHub using the desktop app.
- [x] Add a `.gitignore` file (e.g., ignore `__pycache__`, `.DS_Store`, virtual environments, STL files, etc.).
- [x] Create a basic FastAPI project structure:
  - `track_app/` for core logic.
  - `templates/` and `static/` for web interface assets (if needed).
- [x] Set up Docker for local deployment:
  - Create a `Dockerfile` to containerize the FastAPI application.
  - Create a `docker-compose.yml` file to manage dependencies and services.
  - Verify the application runs successfully in Docker.

---

## 2. Core Functionality

### a. Database Models
- [ ] Define models for track components in `models.py`:
  - Straight Track: Include length and other parameters.
  - Chairs: Include dimensions and types (minimal for MVP).
  - Rails: Placeholder for future iterations.
- [ ] Use SQLAlchemy to implement the database.
- [ ] Create migrations and populate the database with example data using Alembic.

### b. Geometry and STL Export
- [ ] Implement a function to generate geometry for straight tracks.
- [ ] Integrate geometry generation with FastAPI routes.
- [ ] Use CadQuery to generate STL files based on user input.
- [ ] Validate STL file integrity using lightweight checks (e.g., watertightness).
- [ ] Provide basic feedback if STL integrity checks fail during testing.
- [ ] Provide a downloadable STL file through the FastAPI app.

### c. User Interface
- [ ] Create a simple web interface or API for:
  - Submitting track parameters (e.g., length).
  - Viewing and downloading the generated STL file.
- [ ] Test for usability and responsiveness.

---

## 3. Testing
- [ ] Write unit tests for models, routes, and geometry generation functions using `pytest`.
- [ ] Test STL export functionality with various track lengths.
- [ ] Validate edge cases, such as:
  - Extremely short or long tracks.
  - Invalid user inputs.

---

## 4. Deployment (Local Testing Only)
- [ ] Deploy the FastAPI app on Docker Desktop for local testing.
- [ ] Verify the Docker setup:
  - Ensure all dependencies are included.
  - Validate the app runs correctly within the container.
- [ ] Document the steps for building and running the Docker container.

---

## 5. Documentation
- [ ] Write a clear **Getting Started** guide for contributors.
- [ ] Document all database models and their relationships.
- [ ] Provide usage examples for API endpoints.
- [ ] Create a troubleshooting guide for common issues.
- [ ] Include detailed steps for setting up the FastAPI app locally and in Docker.

---

## 6. Future Enhancements (Post-MVP)
- [ ] Add support for curves and turnouts.
- [ ] Introduce more advanced track configurations and layouts.
- [ ] Implement REST API endpoints for programmatic access.
- [ ] Plan for web hosting and deployment on a cloud platform (e.g., AWS or DigitalOcean).
