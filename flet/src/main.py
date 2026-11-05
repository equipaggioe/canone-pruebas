"""Show one page with the theme applied."""

import flet as ft

import theme


def main(page: ft.Page) -> None:
    """Build the page."""
    theme.apply(page)
    page.add(ft.Text("Hello"))


ft.run(main)
