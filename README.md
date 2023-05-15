# Notification service

It offers a RESTful API, protected by JWT authentication, for sending notifications and supports email notifications.
It has a scalable architecture that allows you to easily add support for other types of notifications.

## Features

* Send notifications to users via email.
* Easy integration with existing applications through the RESTful API.
* Scalable and efficient architecture.

## Getting Started

### Prerequisites

* Python 3.10
* Poetry
* Docker

### Installation

1. Clone the repository:

```shell
git clone https://github.com/patriarch11/notif_service.git
```

2. Navigate to the project directory:

```shell
cd notif_service
```

3. Set the environment:
```shell
poetry env use python3.10
```
```shell
poetry shell
```
4. Install the dependencies:
```shell
poetry install
```
### Configuration
1. Rename the .env.example file to .env:
2. Edit the .env file and provide the necessary configuration values, such as API keys for email or push notification services.
### Usage
1. Start the application using Docker Compose:
```shell
docker-compose up
```
2. The API will be available at http://localhost:8000.