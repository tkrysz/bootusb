"""Generuje statyczną stronę (do wdrożenia np. na GitHub Pages) do katalogu dist/."""
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from i18n import DEFAULT_LANG, LANGS, UI, get_methods

ROOT = Path(__file__).parent
DIST = ROOT / "dist"


def build():
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html"]),
    )

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    # Strony językowe: dist/<lang>/index.html
    guide = env.get_template("index.html")
    for lang in LANGS:
        out = DIST / lang / "index.html"
        out.parent.mkdir()
        out.write_text(
            guide.render(lang=lang, langs=LANGS, t=UI[lang], methods=get_methods(lang)),
            encoding="utf-8",
        )

    # Strona główna: wykrywa język w przeglądarce i przekierowuje
    root = env.get_template("redirect.html")
    (DIST / "index.html").write_text(
        root.render(langs=LANGS, default_lang=DEFAULT_LANG),
        encoding="utf-8",
    )

    # GitHub Pages: wyłącza przetwarzanie Jekyllem
    (DIST / ".nojekyll").touch()

    print(f"Wygenerowano {len(LANGS) + 1} stron w {DIST}")


if __name__ == "__main__":
    build()
