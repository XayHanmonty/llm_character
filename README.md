# llm_character

A project for creating and managing LLM-based characters.

## Setup and Installation

### Prerequisites

- Python 3.12 (specifically versions >=3.12,<3.13)
- [Poetry](https://python-poetry.org/) for dependency management

### Installing Dependencies

This project uses Poetry for dependency management. Follow these steps to set up your development environment:

1. **Install Poetry** (if not already installed):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/llm_character.git
   cd llm_character
   ```

3. **Set Python version** (ensure you have Python 3.12 installed):

   ```bash
   poetry env use /path/to/python3.12
   ```

   For example with Homebrew on macOS:
   ```bash
   poetry env use /opt/homebrew/bin/python3.12
   ```

4. **Install dependencies**:

   ```bash
   poetry install
   ```

5. **Activate the virtual environment**:

   ```bash
   poetry shell
   ```

### Current Dependencies

The project uses the following main dependencies:

#### Core Libraries
- **Python**: 3.12 (>=3.12,<3.13)
- **pydantic**: Data validation and settings management
- **pydantic-settings**: Settings management for pydantic

#### Data Processing & Machine Learning
- **numpy**: Numerical computing
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning algorithms
- **datasets**: Hugging Face datasets library
- **unstructured**: Document parsing and processing

#### AI & LLM Integration
- **langchain**: Framework for LLM applications
- **langchain-openai**: OpenAI integration for LangChain
- **langchain-community**: Community extensions for LangChain
- **litellm**: LLM API abstraction
- **sentence-transformers**: Sentence embeddings
- **instructorembedding**: Instruction-based embeddings
- **huggingface-hub**: Hugging Face model hub integration

#### Vector Database & Storage
- **qdrant-client**: Vector database client
- **pymongo**: MongoDB client

#### Web & UI
- **gradio**: Web UI for ML models
- **selenium**: Web browser automation
- **html2text**: HTML to text conversion

#### AWS Integration
- **aws-lambda-powertools**: AWS Lambda utilities
- **sagemaker**: Amazon SageMaker SDK

#### Messaging & Communication
- **pika**: RabbitMQ client

#### Utilities & Development
- **structlog**: Structured logging
- **rich**: Rich text and formatting in terminal
- **ruff**: Python linter
- **gdown**: Google Drive downloader
- **comet-ml**: ML experiment tracking
- **opik**: Utility library

## Running Tests

This project uses `pytest` for testing. To run the test suite, execute the following command from the project's root directory:

```bash
poetry run pytest
```

### Adding New Dependencies

To add a new dependency to the project:

```bash
poetry add package-name
```

For development dependencies:

```bash
poetry add --group dev package-name
```

## Project Structure

```
.
├── src/
│   └── data_crawling/
│       └── crawlers/
├── pyproject.toml    # Project configuration and dependencies
├── poetry.lock      # Locked dependencies
└── README.md        # This file
```

## License

See the [LICENSE](LICENSE) file for details.