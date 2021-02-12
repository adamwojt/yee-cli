import json
import socket
import sys
from pathlib import Path

import click
import yeelight
from webcolors import CSS3_NAMES_TO_HEX as COLOR_NAMES

from yee.yee import Room


class HandleSocketError(click.Group):
    def __call__(self, *args, **kwargs):
        try:
            return self.main(*args, **kwargs)
        except yeelight.main.BulbException as exc:
            if isinstance(exc.__cause__, socket.error):
                click.echo(exc)
                click.echo(
                    """Please check below:
    * IP addresses of bulbs in config are correct.
    * LAN Control is ON (https://www.yeelight.com/faqs/lan_control).
    * You are connected to same WIFI network as your bulbs.
    * For more debug ideas visit https://github.com/skorokithakis/python-yeelight"""
                )
                sys.exit(1)
            raise


@click.group(invoke_without_command=True, cls=HandleSocketError)
@click.argument("room_name", required=False)
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True),
    envvar="YEE_ROOM_CONFIG",
)
@click.pass_context
def main(context, room_name, config):
    """Yeelight room control CLI.

    \b
    Example usage:
        yee office dim 100
        yee bedroom toggle
        yee living color red
        yee color_list

    \b
    Config:
        Location: $HOME/.yee_rooms
        Format: JSON
        Example: {
            "office": ["192.1.1.1", "192.1.1.2"],
            "bedroom": ["192.1.1.3"]
        }
        To get bulb IPs use tools like nmap, nutty or check Yeelight app.
    """
    CONFIG_PATH = Path(config) if config else Path(Path.home()) / ".yee_rooms"
    if not CONFIG_PATH.is_file():
        click.echo(context.get_help())
        raise click.UsageError(f"Room config missing at {CONFIG_PATH}")
    try:
        with open(CONFIG_PATH) as f:
            rooms = json.load(f)
    except json.decoder.JSONDecodeError as e:
        raise click.UsageError(f"Invalid JSON config file: {CONFIG_PATH}") from e

    ROOMS = {room: Room(bulb_ips) for room, bulb_ips in rooms.items()}

    if room_name == "color_list":
        context.invoke(color_list)
        return
    if context.invoked_subcommand is None:
        click.echo(context.get_help())
        return
    try:
        context.room = ROOMS[room_name]
    except KeyError as e:
        raise click.BadParameter(f"Room does not exist, check your config at {CONFIG_PATH}") from e


@main.command()
@click.pass_context
def toggle(context):
    """Toggle lights."""
    context.parent.room.toggle()


@main.command()
@click.pass_context
@click.argument("level", type=click.INT)
def dim(context, level):
    """Dim lights to level (1-100)."""
    context.parent.room.dim(level)


@main.command()
@click.pass_context
@click.argument("color_name")
def color(context, color_name):
    """Set lights to given color."""
    try:
        context.parent.room.color(color_name)
    except ValueError as e:
        raise click.BadParameter("Wrong color name, see `color_list` command.") from e


@main.command("random_color")
@click.pass_context
def random_color(context):
    """Switch to random color."""
    context.parent.room.random_color()


@main.command()
@click.pass_context
def on(context):
    """Turn lights on."""
    context.parent.room.on()


@main.command()
@click.pass_context
def off(context):
    """Turn lights off."""
    context.parent.room.off()


@main.command("color_list")
def color_list():
    """ Available color list """
    for color_name in COLOR_NAMES:
        click.echo(color_name)


if __name__ == "__main__":
    sys.exit(main())  # pylint: disable=E1120
