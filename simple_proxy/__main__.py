from loguru import logger

from simple_proxy.core.cli import typer_app
from simple_proxy.paths import LOG_FILE

# Configure Loguru Logger
logger.add(LOG_FILE, level="TRACE", rotation="50 MB")


if __name__ == "__main__":
    logger.info(f"Starting Typer App: '{typer_app.info.name}'...")
    typer_app()
