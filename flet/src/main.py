"""Show one page with the theme applied."""

import flet as ft

import api
import theme


def main(page: ft.Page) -> None:
    """Build the page."""
    theme.apply(page)
    page.add(ft.Text(str(api.Reply(status=200).status)))


ft.run(main)
