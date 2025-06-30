# LLM Character Twin

This project is designed to create a digital twin of a person's online presence by crawling and processing data from various sources like GitHub, Medium, and other social platforms. The collected data is then used to build a Retrieval-Augmented Generation (RAG) system, allowing users to interact with a character that mirrors the person's knowledge and communication style.

## Features

- **Data Crawling**: Modular crawlers for different platforms (starting with GitHub).
- **MongoDB Integration**: Stores crawled data in a MongoDB database.
- **Robust Testing**: Unit tests written with `pytest` and `pytest-mock`.
- **Modern Python Tooling**: Uses `poetry` for dependency management and a `src` layout.

## Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd llm_character
    ```

2.  **Install dependencies using Poetry:**
    ```bash
    poetry install
    ```

### Configuration

This project uses a `.env` file to manage environment variables and secrets. 

1. Create a `.env` file in the root of the project.
2. Add the necessary configuration variables for the services you intend to use (e.g., `GITHUB_TOKEN`, `MONGO_URI`).

## Running Tests

This project uses `pytest` for testing. To run the test suite, execute the following command from the project's root directory:

```bash
poetry run pytest
```

This will discover and run all tests located in the `tests/` directory.

## Dependencies

This project uses Poetry for dependency management. 

### Adding New Dependencies

To add a new dependency to the project:

```bash
poetry add package-name
```

For development dependencies:

```bash
poetry add --group dev package-name
```

### Key Dependencies

<details>
<summary>Click to view key dependencies</summary>

#### Core Libraries
- **Python**: 3.12
- **pydantic**: Data validation and settings management

#### AI & LLM Integration
- **langchain**: Framework for LLM applications
- **sentence-transformers**: Sentence embeddings

#### Data Storage
- **qdrant-client**: Vector database client
- **pymongo**: MongoDB client

#### Web & UI
- **gradio**: Web UI for ML models

</details>


## License

See the [LICENSE](LICENSE) file for details.