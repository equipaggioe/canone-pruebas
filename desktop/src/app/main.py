"""Show one window with the theme applied."""

import sys

from PySide6.QtWidgets import QApplication, QLabel

from app import theme


def main() -> int:
    """Run the app."""
    app = QApplication(sys.argv)
    theme.apply(app)
    label = QLabel("Hello")
    label.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
