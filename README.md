# E-commerce-API-3project

# Clone the repository
git clone <repo-url>
cd <project-name>/backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements/development.txt

# Set up the environment variables
cp env-example.txt .env
# Open the .env file and fill in the required values

# Install and configure pre-commit hooks
pre-commit install
pre-commit autoupdate

# Make the start script executable
chmod +x start.sh

# Run the project
./start.sh
```

```commandline
celery -A config worker --loglevel=info
```