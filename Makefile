.PHONY: help install dev test run docker-build docker-run docker-stop clean lint format

help:
	@echo "Crypto Arbitrage Bot - Available Commands"
	@echo "=========================================="
	@echo "make install      - Install dependencies"
	@echo "make dev          - Install dev dependencies"
	@echo "make test         - Run unit tests"
	@echo "make lint         - Run linting checks"
	@echo "make format       - Format code with autopep8"
	@echo "make run          - Run the bot locally"
	@echo "make docker-build - Build Docker image"
	@echo "make docker-run   - Run bot in Docker"
	@echo "make docker-stop  - Stop Docker container"
	@echo "make clean        - Clean up cache and logs"
	@echo "make setup        - Complete setup wizard"

install:
	pip install --upgrade pip
	pip install -r requirements.txt

dev:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install pytest pytest-cov flake8 autopep8 bandit safety

test:
	python -m pytest test_bot.py -v --cov=. --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

format:
	autopep8 --in-place --aggressive --aggressive *.py

run:
	python crypto_bot.py

docker-build:
	docker build -t crypto-arbitrage-bot:latest .

docker-run:
	docker-compose up -d
	@echo "Bot started in Docker. View logs with: docker-compose logs -f"

docker-stop:
	docker-compose down

docker-logs:
	docker-compose logs -f crypto-arbitrage-bot

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf dist build *.egg-info
	rm -f .coverage

setup:
	@echo "Crypto Arbitrage Bot - Setup Wizard"
	@echo "===================================="
	@echo ""
	@echo "Step 1: Installing dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "✓ Dependencies installed"
	@echo ""
	@echo "Step 2: Creating .env file..."
	@if [ ! -f .env ]; then cp .env.example .env; echo "✓ .env file created"; else echo "✓ .env file already exists"; fi
	@echo ""
	@echo "Step 3: Creating logs directory..."
	mkdir -p logs
	@echo "✓ Logs directory created"
	@echo ""
	@echo "Setup complete! Now:"
	@echo "1. Edit your .env file with API keys and email configuration"
	@echo "2. Run: make test     (to verify installation)"
	@echo "3. Run: make run      (to start the bot)"

.DEFAULT_GOAL := help
