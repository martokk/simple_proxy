import typer
from loguru import logger
from rich.console import Console

from simple_proxy import version
from simple_proxy.constants import PACKAGE_DESCRIPTION, PACKAGE_NAME
from simple_proxy.core.app import app

# Configure Rich Console
console = Console()

# Configure Typer
typer_app = typer.Typer(
    name=PACKAGE_NAME,
    help=PACKAGE_DESCRIPTION,
    add_completion=False,
)


# Typer Command Callbacks
def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]{PACKAGE_NAME}[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


# Typer Commands
@typer_app.command()
def main(
    print_version: bool = typer.Option(  # pylint: disable=unused-argument
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the '{APP_NAME}' package.",
    ),
) -> None:
    """Main entrypoint into application"""

    # Start Server
    logger.info("Starting App...")
    app()
