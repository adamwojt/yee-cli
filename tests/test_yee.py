#!/usr/bin/env python
from unittest import mock

import pytest
from click.testing import CliRunner

from yee import cli


@mock.patch("yee.yee.Room._execute_on_all_bulbs", lambda *args, **kwargs: None)
def test_command_line_interface(cfg):
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["-c", cfg])

    # Test help msg
    assert result.exit_code == 0
    assert "Yeelight room control CLI" in result.output

    # Test color_list
    color_list = runner.invoke(cli.main, ["-c", cfg, "color_list"])
    assert "aliceblue\nantiquewhite\naqua\naquamarine" in color_list.output

    # Test dim
    dim_result = runner.invoke(cli.main, ["-c", cfg, "kitchen", "dim", "100"])
    assert dim_result.exit_code == 0

    dim_without_level_result = runner.invoke(cli.main, ["-c", cfg, "kitchen", "dim"])
    assert dim_without_level_result.exit_code == 2

    # Test on
    on_result = runner.invoke(cli.main, ["-c", cfg, "bedroom", "on"])
    assert on_result.exit_code == 0

    # Test off
    off_result = runner.invoke(cli.main, ["-c", cfg, "kitchen", "off"])
    assert off_result.exit_code == 0

    # Test toggle
    toggle_result = runner.invoke(cli.main, ["-c", cfg, "office", "toggle"])
    assert toggle_result.exit_code == 0

    # Test random_color
    random_color_result = runner.invoke(cli.main, ["-c", cfg, "kitchen", "random_color"])
    assert random_color_result.exit_code == 0

    # Test non-existent room
    no_room_result = runner.invoke(cli.main, ["-c", cfg, "living_room", "random_color"])
    assert no_room_result.exit_code == 2
    assert "Room does not exist" in no_room_result.output
