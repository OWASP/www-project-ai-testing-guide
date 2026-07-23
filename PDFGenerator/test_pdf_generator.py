import tempfile
import unittest
from pathlib import Path

from PDFGenFinal import parse_toc_file, resolve_config_path


class PdfGeneratorPathTests(unittest.TestCase):
    def test_config_paths_are_relative_to_config_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "pdf" / "config.txt"

            resolved = resolve_config_path(config_path, "ToC.md")

            self.assertEqual(resolved, (config_path.parent / "ToC.md").resolve())

    def test_toc_github_links_resolve_from_repository_root(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            content_path = repo_root / "Document" / "content" / "chapter.md"
            content_path.parent.mkdir(parents=True)
            content_path.write_text("# Chapter\n", encoding="utf-8")
            toc_path = repo_root / "PDFGenerator" / "ToC.md"
            toc_path.parent.mkdir()
            toc_path.write_text(
                "[Chapter](https://github.com/OWASP/"
                "www-project-ai-testing-guide/blob/main/"
                "Document/content/chapter.md)\n",
                encoding="utf-8",
            )

            entries = parse_toc_file(toc_path, repo_root)

            self.assertEqual(
                entries,
                [
                    (
                        "https://github.com/OWASP/"
                        "www-project-ai-testing-guide/blob/main/"
                        "Document/content/chapter.md",
                        content_path.resolve(),
                    )
                ],
            )


if __name__ == "__main__":
    unittest.main()
