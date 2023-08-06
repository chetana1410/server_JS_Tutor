# Personal JavaScript Tutor Backend

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Initializing the App](#initializing-the-app)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The Personal JavaScript Tutor app is an interactive tool built using Langchain, Streamlit, and FastAPI. This backend component of the app provides two API endpoints that facilitate communication between the client and the OpenAI API. The backend receives client requests, validates them, and forwards them to OpenAI using the API key stored as an environment variable. Once the response is received from the OpenAI endpoint, it is sent back as a response to the client.

## Getting Started

### Prerequisites

To run the app locally, make sure you have the following installed:

- Python (>=3.6)
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/your_username/your_project.git
cd your_project
```

2. Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## Environment Variables

Before starting the server, make sure to set the following environment variable:

- `OPENAI_API_KEY`: This variable stores the API key required to access the OpenAI API. Obtain your API key from OpenAI and pass it into the `.env` file.

## Initializing the App

To start the server, run the following command:

```
uvicorn main:app --port 7000
```

The backend will be up and running, ready to serve requests from the client.

## Contributing

We welcome contributions to improve the Personal JavaScript Tutor app. If you find any bugs, have suggestions, or want to add new features, feel free to submit a pull request or open an issue in the repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it according to the terms of the license.

## Acknowledgments

We express our gratitude to the Langchain, Streamlit, and FastAPI communities for providing powerful tools to build this app. We also thank OpenAI for granting access to their API, enabling us to create an enhanced learning experience for JavaScript enthusiasts.