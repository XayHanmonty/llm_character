# MongoDB Connection Testing Guide

This document provides guidance on testing MongoDB connections in the LLM Character project.

## Overview
This guide covers:

1. Real connection testing
2. Mock testing with mongomock
3. Troubleshooting common connection issues

## Real Connection Testing

To test a real MongoDB connection:
Run this test with:

```bash
poetry run pytest tests/test_db_connection.py::test_real_database_connection -v -s
```

## Mock Testing with mongomock

For unit tests, it's better to use a mock database to avoid external dependencies:

Run mock tests with:

```bash
poetry run pytest tests/test_db_connection.py::test_database_connection -v -s
```

## Adding Test Data

You can add test data to your mock database:


## Troubleshooting Connection Issues

### SSL/TLS Issues

If you encounter SSL handshake failures:

1. Use `certifi` to provide up-to-date SSL certificates:

```python
import certifi
from pymongo import MongoClient

client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
```

2. Check your MongoDB connection string format:

```
mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
```

### Authentication Issues

If you encounter authentication failures:

1. Verify your username and password are correct
2. Ensure the user has appropriate permissions for the database
3. Check if IP access restrictions are in place

### Connection Timeout

If connections time out:

1. Check network connectivity
2. Verify firewall settings
3. Consider increasing the timeout settings:

```python
client = MongoClient(mongo_uri, serverSelectionTimeoutMS=10000)
```

## Continuous Integration

For CI environments, consider:

1. Using mongomock for all tests
2. Setting up a dedicated test database
3. Creating and destroying test data before and after test runs

## References

- [PyMongo Documentation](https://pymongo.readthedocs.io/)
- [mongomock Documentation](https://github.com/mongomock/mongomock)
- [pytest Documentation](https://docs.pytest.org/)
