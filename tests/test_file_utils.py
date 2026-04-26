"""Tests for src/file_utils.py — filename parsing and file matching logic."""
import datetime

import pytest

from src.file_utils import extract_id_from_filename, find_matching_files, get_file_date


class TestExtractIdFromFilename:
    def test_extracts_standard_id(self):
        assert extract_id_from_filename("G12345 Report.pdf") == "G12345"

    def test_extracts_lowercase_prefix(self):
        assert extract_id_from_filename("a9999 Document.pdf") == "a9999"

    def test_returns_none_when_no_id_present(self):
        assert extract_id_from_filename("Report without ID.pdf") is None

    def test_returns_none_for_empty_string(self):
        assert extract_id_from_filename("") is None

    def test_returns_none_for_numeric_only_prefix(self):
        # Pattern requires at least one leading letter
        assert extract_id_from_filename("12345 Report.pdf") is None

    def test_returns_none_for_letters_only_prefix(self):
        assert extract_id_from_filename("ABC Report.pdf") is None

    def test_custom_pattern_matches(self):
        result = extract_id_from_filename("AB123 Doc.pdf", pattern=r"^[A-Z]{2}\d+$")
        assert result == "AB123"

    def test_custom_pattern_no_match(self):
        result = extract_id_from_filename("G12345 Doc.pdf", pattern=r"^[A-Z]{2}\d+$")
        assert result is None


class TestFindMatchingFiles:
    def test_finds_matching_pdf_files(self, tmp_path):
        (tmp_path / "G123 Report.pdf").touch()
        (tmp_path / "G123 Data.pdf").touch()
        (tmp_path / "H456 Report.pdf").touch()

        result = find_matching_files(tmp_path, "G123")
        assert len(result) == 2
        assert all("G123" in p.name for p in result)

    def test_returns_empty_list_when_no_match(self, tmp_path):
        (tmp_path / "H456 Report.pdf").touch()
        result = find_matching_files(tmp_path, "G123")
        assert result == []

    def test_returns_empty_for_nonexistent_folder(self, tmp_path):
        result = find_matching_files(tmp_path / "nonexistent", "G123")
        assert result == []

    def test_returns_empty_for_empty_id(self, tmp_path):
        (tmp_path / "G123 Report.pdf").touch()
        result = find_matching_files(tmp_path, "")
        assert result == []

    def test_results_are_sorted_alphabetically(self, tmp_path):
        (tmp_path / "G123 Z_last.pdf").touch()
        (tmp_path / "G123 A_first.pdf").touch()
        result = find_matching_files(tmp_path, "G123")
        names = [p.name for p in result]
        assert names == sorted(names)

    def test_filters_by_extension(self, tmp_path):
        (tmp_path / "G123 Report.pdf").touch()
        (tmp_path / "G123 Notes.txt").touch()
        result = find_matching_files(tmp_path, "G123", extension=".pdf")
        assert len(result) == 1
        assert result[0].suffix == ".pdf"

    def test_extension_filter_excludes_wrong_type(self, tmp_path):
        (tmp_path / "G123 Notes.txt").touch()
        result = find_matching_files(tmp_path, "G123", extension=".pdf")
        assert result == []


class TestGetFileDate:
    def test_returns_date_object_for_existing_file(self, tmp_path):
        f = tmp_path / "test.pdf"
        f.touch()
        result = get_file_date(f)
        assert isinstance(result, datetime.date)

    def test_returned_date_is_today_or_recent(self, tmp_path):
        f = tmp_path / "test.pdf"
        f.touch()
        result = get_file_date(f)
        assert result is not None
        assert result >= datetime.date.today() - datetime.timedelta(days=1)

    def test_returns_none_for_missing_file(self, tmp_path):
        result = get_file_date(tmp_path / "nonexistent.pdf")
        assert result is None
