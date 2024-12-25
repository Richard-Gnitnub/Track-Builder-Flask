# PROJECT: Lightweight Track Builder (Rewrite of Templot by Martin Wynne)

## GOAL
Create a minimal Python-based engine to generate accurate model railway track, focusing on straight track and simple turnouts for 3D printing (STL export). The project will adhere to bullhead rail standards based on REA specifications, with chairs and timbers included. This MVP will serve as the foundation for a more comprehensive track design tool.

---

## KEY INSIGHTS
- Legacy `dxf_unit.pas` (Pascal) code is pivotal, containing both 2D DXF and 3D STL export logic.
- The codebase is monolithic, heavily reliant on global variables for rail/sleeper geometry, tolerances, and more.
- Decades of incremental updates have resulted in intertwined 2D and 3D logic under "DXF" routines.

---

## MVP PLAN
- Build the MVP using Flask as the framework, replacing Django for a lightweight approach.
- Create an admin panel using the Flask-Admin extension to manage track configurations and parameters.
- Focus on bullhead rail based on REA standards.
- Include chairs as part of the 3D model, as the rail sits within the chairs.
- Design track as a combination of:
  - **Timbers:** Base structure for the track.
  - **Chairs:** Components to hold the rail.
  - **Rail:** Added manually by the user post-3D printing.
- Implement functionality to generate a straight piece of track to the user’s specified length.
- Use Python CAD libraries (e.g., CadQuery) for STL file generation.
- Introduce a SQLite database to remove hardcoded data, enabling flexible storage of track parameters and configurations.

---

## WORKING ENVIRONMENT REQUIREMENTS
- The project will be developed using VS Code on a Windows laptop.
- GitHub Desktop will be used for version management.
- Instructions will provide explicit steps, including details on where files should be placed within the directory structure to ensure clarity and avoid ambiguity.
- CLI will be windows Command Prompt

---

## REFACTORING OUTLINE
- **Separation of Concerns:** Replace global variables with structured classes (e.g., `TrackSettings`).
- **Database Integration:** Replace hardcoded values with dynamic retrieval from the SQLite database for better configurability and scalability.
- **Geometry/Math Decoupling:** Keep core logic in a separate module, independent of UI/CLI.
- **Native 3D Export:** Leverage Python CAD libraries to directly generate STL geometry.
- **Track Element Modularity:** Ensure timbers, chairs, and rail are modularly designed for reusability and scalability.

---

## ATTRIBUTION
To comply with GNU GPLv3, include prominent attribution in the code comments and documentation to Martin Wynne for his original work on Templot.

---

## FUTURE ENHANCEMENTS
- Add more track types, turnout angles, and advanced details (e.g., snap-fit designs) once the MVP is stable.
- Expand REA-based models with additional variations and regional standards.
- Reintroduce specialized features like chaired track and snap-fit designs after validating the core engine.

---

## END STATE
A Flask-based, modular, and maintainable track design engine that generates STL files for REA-standard bullhead rail track, including chairs and timbers, supported by a SQLite database for flexible data management. The rail itself is intended to be added manually by the user after 3D printing.

---

## REFERENCE
[GitHub Link](https://github.com/Richard-Gnitnub/Templot5/blob/main/dxf_unit.pas)

---

## NOTES
- Develop using Python 3.12.3 (latest version as of October 2023).
- Attribution to Martin Wynne is essential to comply with GNU GPLv3.

---
## Core Application Functionality (MVP)
```
flowchart TD
    A[User Input] -->|Track Parameters| B[Input Validation]
    B -->|Check for Errors| C{Valid Input?}
    C -->|Yes| D[Fetch Data from Database]
    C -->|No| E[Return Error Message]
    D -->|Configurations Loaded| F[Process Geometry]
    F -->|Generate Timbers and Chairs| G[Create 3D Model with CadQuery]
    G -->|Convert to STL| H[STL Export]
    H -->|Save File| I[Provide Download Link]
    I -->|User Access| J[Download STL File]

    subgraph Flask Workflow
        B --> C --> D --> F
    end

    subgraph External Logic
        G --> H
    end

    subgraph Final Output
        I --> J
    end

```
---
## Future Enhancements 
```
flowchart TD
    A[User Input] -->|Advanced Parameters| B[Enhanced Validation]
    B -->|Check for Errors| C{Valid Input?}
    C -->|Yes| D[Fetch Advanced Data from Database]
    C -->|No| E[Return Error Message]
    D -->|Configurations Loaded| F[Process Advanced Geometry]
    F -->|Generate Curves, Turnouts, and Snap-Fit Designs| G[Create Advanced 3D Model]
    G -->|Convert to STL| H[STL Export]
    H --> I[Inspect STL File]
    I -->|Check for Issues| J{Issues Found?}
    J -->|Yes| K[Generate Inspection Report]
    K -->|User Opts to Repair| L[Run Mesh Repair]
    L --> M[Save Repaired STL File]
    J -->|No| N[Save Original STL File]
    M --> O[Provide Download Link]
    N --> O
    O --> P[User Access STL File or Report]

    subgraph Advanced Workflow
        F --> G --> H --> I --> J
        J --> K --> L --> M
        J --> N
    end

    subgraph Final Output
        O --> P
    end
```
---
## Core App Directory Structure

```
project/
│
├── track_app/
│   ├── __init__.py    # Application initialization
│   ├── models.py      # Database models
│   ├── routes.py      # Application routes
│   ├── geometry.py    # Track geometry logic
│   ├── templates/     # HTML templates (if needed)
│   ├── static/        # Static files (if needed)
│
├── migrations/        # Database migration files
├── tests/             # Unit tests
├── Dockerfile         # Docker container configuration
├── docker-compose.yml # Docker Compose setup
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

```
---