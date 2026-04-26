"""Tests for DocumentProcessor date filtering and ID-matching logic."""
import datetime
from pathlib import Path
from unittest.mock import patch

import pytest

from src.config import ProcessorConfig
from src.document_processor import DocumentProcessor


def _make_config(tmp_path: Path, start_date: datetime.date | None = None) -> ProcessorConfig:
    """Build a minimal ProcessorConfig pointing at tmp_path subdirectories."""
    if start_date is None:
        start_date = datetime.date(2020, 1, 1)
    source = tmp_path / "source"
    output = tmp_path / "output"
    source.mkdir()
    output.mkdir()
    return ProcessorConfig(
        source_folder=str(source),
        output_folder=str(output),
        start_date=start_date,
    )


class TestDateFiltering:
    def test_skips_files_before_start_date(self, tmp_path):
        cfg = _make_config(tmp_path, start_date=datetime.date(2024, 1, 1))
        (cfg.source_folder / "G123 Report.pdf").touch()

        with patch("src.document_processor.get_file_date", return_value=datetime.date(2020, 6, 1)):
            stats = DocumentProcessor(cfg).process_documents()

        assert stats["skipped_date"] == 1
        assert stats["processed"] == 0

    def test_processes_file_on_start_date(self, tmp_path):
        start = datetime.date(2024, 1, 1)
        cfg = _make_config(tmp_path, start_date=start)
        (cfg.source_folder / "G123 Report.pdf").touch()

        with patch("src.document_processor.get_file_date", return_value=start), \
             patch("src.document_processor.merge_pdf_files", return_value=True):
            stats = DocumentProcessor(cfg).process_documents()

        assert stats["skipped_date"] == 0
        assert stats["processed"] == 1

    def test_processes_file_after_start_date(self, tmp_path):
        cfg = _make_config(tmp_path, start_date=datetime.date(2024, 1, 1))
        (cfg.source_folder / "G123 Report.pdf").touch()

        with patch("src.document_processor.get_file_date", return_value=datetime.date(2024, 6, 15)), \
             patch("src.document_processor.merge_pdf_files", return_value=True):
            stats = DocumentProcessor(cfg).process_documents()

        assert stats["skipped_date"] == 0
        assert stats["processed"] == 1


class TestIdFiltering:
    def test_skips_file_with_no_valid_id(self, tmp_path):
        cfg = _make_config(tmp_path)
        (cfg.source_folder / "NoIDReport.pdf").touch()

        with patch("src.document_processor.get_file_date", return_value=datetime.date(2024, 6, 1)):
            stats = DocumentProcessor(cfg).process_documents()

        assert stats["skipped_format"] == 1
        assert stats["processed"] == 0

    def test_processes_file_with_valid_id(self, tmp_path):
        cfg = _make_config(tmp_path)
        (cfg.source_folder / "G123 Report.pdf").touch()

        with patch("src.document_processor.get_file_date", return_value=datetime.date(2024, 6, 1)), \
             patch("src.document_processor.merge_pdf_files", return_value=True):
            stats = DocumentProcessor(cfg).process_documents()

        assert stats["skipped_format"] == 0
        assert stats["processed"] == 1

    def test_empty_source_folder_returns_zero_counts(self, tmp_path):
        cfg = _make_config(tmp_path)
        stats = DocumentProcessor(cfg).process_documents()
        assert stats["processed"] == 0
        assert stats["skipped_format"] == 0
        assert stats["skipped_date"] == 0
