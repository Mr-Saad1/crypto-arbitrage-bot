# Contributing to Crypto Arbitrage Bot

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repo on GitHub
# Clone your fork
git clone https://github.com/YOUR-USERNAME/crypto-arbitrage-bot.git
cd crypto-arbitrage-bot

# Add upstream remote
git remote add upstream https://github.com/Mr-Saad1/crypto-arbitrage-bot.git
```

### 2. Setup Development Environment

```bash
make dev
make setup
```

### 3. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## Making Changes

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep lines under 127 characters
- Run `make lint` before committing

### Testing

```bash
# Run tests
make test

# Run specific test
python -m pytest test_bot.py::TestConfig -v

# Check coverage
make test  # generates htmlcov/index.html
```

### Commit Messages

Write clear, descriptive commit messages:

```
Fix: Resolve price parsing issue in exchange_connector

- Fixed decimal precision handling
- Added unit tests for edge cases
- Updated error handling

Fixes #42
```

Types:
- `feat:` A new feature
- `fix:` A bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, missing semicolons, etc.)
- `refactor:` Code refactoring
- `perf:` Performance improvements
- `test:` Adding or updating tests
- `chore:` Build process, dependencies, etc.

## Submitting a Pull Request

### Before You Submit

1. Update your branch with main:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Run tests and linting:
   ```bash
   make test
   make lint
   ```

3. Commit your changes:
   ```bash
   git commit -am "Your commit message"
   ```

### Create the PR

1. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Go to GitHub and create a Pull Request

3. Fill in the PR template:
   - **Description**: What does this PR do?
   - **Type**: Feature/Fix/Docs/etc.
   - **Testing**: How did you test it?
   - **Checklist**: Run through the checklist

## Pull Request Guidelines

- Describe what your PR does clearly
- Reference related issues (#42)
- Keep PRs focused on a single feature/fix
- Update documentation if needed
- Add tests for new features
- Ensure all checks pass

## Areas You Can Help

### High Priority
- Bug fixes and error handling
- Performance optimizations
- Documentation improvements
- Unit test coverage

### Medium Priority
- New exchange support
- Additional trading pair support
- Configuration enhancements
- Error message improvements

### Future Features
- WebSocket support
- Database integration
- Web dashboard
- Mobile notifications
- Advanced algorithms

## Questions?

- Check existing issues and discussions
- Open a new issue with the `question` label
- Ask in pull request comments

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

Thank you for contributing! 🚀
