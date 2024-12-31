#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

# Setup logging to handle error messages and info logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Run administrative tasks."""
    try:
        # Get the environment variable to set the appropriate Django settings
        environment = os.getenv('DJANGO_ENV', 'development').lower()
        settings_module = f'career_dendrogram.settings_{environment}'

        # Default settings if environment variable is not set
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_dendrogram.settings')

        # Log the settings module being used
        logger.info(f'Using Django settings: {settings_module}')
        
        # Import Django and execute commands
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)

    except ImportError as exc:
        logger.error("Couldn't import Django. Are you sure it's installed and available?")
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    except Exception as e:
        # Catch all other exceptions
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
