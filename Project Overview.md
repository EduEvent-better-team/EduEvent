# EduEvent — project overview

EduEvent is a web application for organising and participating in educational events, such as lectures, workshops, and training sessions. It brings event information, registrations, waiting lists, attendance, and reports together in one place.

## How the application works

Organisers create and publish events with a title, description, date and time, location, category, presenter, and participant limit. Participants browse the event catalogue, search and filter events, and register for the events they want to attend.

When an event is full, a participant joins its waiting list. If someone cancels their registration, the next person in the queue automatically receives the vacant place. Users receive notifications and reminders within the application.

Organisers record attendance, and participants can view their participation history. Reports summarise events, registrations, and attendance, with CSV export. The calendar presents events in day, week, and month views.

The application supports three user roles:

- **Participant:** browses events, manages their own registrations, and views notifications and participation history.
- **Organiser:** manages their own events and records attendance.
- **Administrator:** manages users and roles and accesses system-wide administration and reports.

## Current implementation

The repository currently contains the shared Django application skeleton, a home page, and a base layout. It uses Django 5.2, PostgreSQL 17, and HTML templates. The functional modules described above are the planned scope and still need to be implemented.

Setup instructions and the repository structure are described in the [README](../README.md).

## Group responsibilities

| Group | Members | Area | Responsibilities |
|---|---|---|---|
| 1 | Antoni Usajewicz, Mateusz Jurek | Architecture and integration | Prepare the shared application structure, home page, and navigation; agree the project structure and data model; integrate modules; coordinate work; and maintain consistent system documentation. |
| 2 | Maksymilian Kaczmarek, Fabian Rudnicki | Accounts and permissions | Registration, login, user profiles, roles, user administration, and basic application settings. |
| 3 | Konrad Kargul, Antoni Ciszewski | Events and communication | Creating, editing, publishing, and cancelling events; managing categories; and providing notifications and reminders within the application. |
| 4 | Karol Jóźwiak, Mikołaj Niezbrzycki | Registrations and waiting lists | Event registration and cancellation, capacity checks, waiting lists, and automatically assigning a vacant place to the next person in the queue. |
| 5 | Antoni Jankowski, Tymon Granecki | Event catalogue | Event lists and details, search, filtering, and sorting. |
| 6 | Oskar Warda, Jakub Drozdalski | Participation, reports, and calendar | Attendance recording, participation history, basic reports, CSV export, and calendar views. |

## Working together

Each group implements the screens, application logic, and database changes for its own area. It also prepares the tests, UML diagrams, and technical and user documentation for that area, and fixes issues found during integration.

The groups share one Django application and one PostgreSQL database. Agree on shared models and relationships before implementing them or changing fields used by another group. Follow the module and directory conventions in the README.

Event data and categories belong to group 3; registrations, queue order, and availability calculations belong to group 4. The catalogue, calendar, and reports use those shared data and rules. Group 4 provides registration changes to group 3 for notifications.

Antoni coordinates groups 2 and 3, while Mateusz coordinates groups 4, 5, and 6. Antoni leads requirements, scheduling, documentation completeness, and presentation organisation. Mateusz leads the shared data model and SQL reviews. Both architects agree on changes affecting several modules and coordinate integration.
