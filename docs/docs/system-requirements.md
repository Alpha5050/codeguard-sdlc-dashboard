# CodeGuard: System Requirements

## 1. Purpose

This document describes what CodeGuard must do and the requirements it must meet. CodeGuard is a web-based dashboard for recording, monitoring and managing security findings across the Software Development Life Cycle (SDLC).

## 2. Functional Requirements

Functional requirements describe the tasks the system must perform.

- **FR01:** The system shall allow authorised users to log in and log out.
- **FR02:** The system shall display statistics about security findings.
- **FR03:** The system shall group findings into Endpoint/IDE, VCS, CI/CD, Registry and Production.
- **FR04:** The system shall allow authorised users to record security findings.
- **FR05:** The system shall classify findings as Critical, High, Medium or Low.
- **FR06:** The system shall allow users to search and filter findings.
- **FR07:** The system shall allow authorised users to update finding statuses.
- **FR08:** The system shall display charts showing findings by severity and SDLC area.
- **FR09:** The system shall allow only administrators to manage user accounts.

## 3. Non-Functional Requirements

Non-functional requirements describe how well and how securely the system must work.

- **NFR01 — Security:** Passwords must be stored securely, and users must only access functions they are authorised to use.
- **NFR02 — Usability:** The dashboard must be easy to navigate.
- **NFR03 — Performance:** Dashboard summaries should load within an agreed time under normal use.
- **NFR04 — Reliability:** Invalid inputs should be handled without crashing the application.
- **NFR05 — Maintainability:** The code should be organised into manageable components.
- **NFR06 — Compatibility:** The application should work in modern web browsers.

## 4. Scope Limitation

The initial version will use sample or manually entered security findings. Automatic detection of live cyberattacks and integration with external enterprise security systems are outside the initial scope.
