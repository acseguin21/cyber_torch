# Cyber Torch

Cyber Torch is a portable Docker-based SaaS application designed for cybersecurity purposes. It integrates with common EDR tools like Microsoft Defender and aggregates alerts and incidents into a case management platform.

## Features

- **Backend**: Built with Python, includes integrations with EDR tools and case management logic.
- **Frontend**: Built with JavaScript, provides a user-friendly interface.
- **Dockerized**: Easily deployable using Docker and Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/cyber_torch.git
   cd cyber_torch
   ```

2. **Build and run the application:**

   ```bash
   docker-compose up --build
   ```

3. **Access the application:**

   Open your browser and go to `http://localhost:3000`.

## Folder Structure

- **backend/**: Contains the backend code and Docker configuration.
- **frontend/**: Contains the frontend code and dependencies.
- **docker-compose.yml**: Configuration for Docker Compose to run the application.

## Next Steps

- Implement EDR integrations in `edr_integration.py`.
- Develop case management features in `case_management.py`.
- Update the frontend to display alerts and manage cases.
- Write tests for both backend and frontend.
- Set up CI/CD pipelines for automated testing and deployment.
- Document API endpoints and usage instructions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. 