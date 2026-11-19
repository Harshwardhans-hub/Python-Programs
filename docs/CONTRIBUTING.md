# Contributing

Thanks for helping improve Python-Programs. The repository is a collection of beginner-friendly Python exercises and reusable examples.

## Before submitting a change

1. Keep each exercise small and give public functions descriptive names.
2. Prefer the Python standard library unless a third-party dependency is necessary.
3. Add docstrings that describe behavior, inputs, and important edge cases.
4. Avoid changing the behavior of existing examples unless the change fixes a documented bug.
5. Add tests for normal inputs, boundary conditions, and invalid inputs.

## Run the tests

Use Python 3.11 or newer:

```bash
python -m unittest discover -s tests -v
```

The same command runs in GitHub Actions on pushes and pull requests targeting `main`.

## Style

- Use four spaces for indentation.
- Add type hints to reusable helpers.
- Raise clear exceptions for invalid arguments rather than silently guessing.
- Do not include credentials, private data, generated caches, or machine-specific files.

## Pull requests

Describe the problem, summarize the behavior added or fixed, and list the test command you ran. A focused change with tests is preferred over unrelated formatting or large rewrites.
