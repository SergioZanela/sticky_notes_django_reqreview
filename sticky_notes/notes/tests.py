"""Unit tests for the sticky notes application."""

from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTests(TestCase):
    """Tests for the :class:`~notes.models.Note` model."""

    def test_str_returns_title(self) -> None:
        """The model's string representation should be its title."""
        note = Note.objects.create(title="My title", content="Body")
        self.assertEqual(str(note), "My title")


class NoteViewTests(TestCase):
    """Integration-style tests for the notes views and URLs."""

    def setUp(self) -> None:
        """Create a couple of notes for use in view tests."""
        self.note1 = Note.objects.create(title="First", content="First body")
        self.note2 = Note.objects.create(title="Second", content="Second body")

    def test_note_list_view_renders(self) -> None:
        """The list view should return HTTP 200 and include created notes."""
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First")
        self.assertContains(response, "Second")

    def test_note_detail_view_renders(self) -> None:
        """The detail view should show the selected note."""
        response = self.client.get(reverse("note_detail", args=[self.note1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note1.title)
        self.assertContains(response, self.note1.content)

    def test_create_note_via_view(self) -> None:
        """Posting valid data to the create view should create a note."""
        response = self.client.post(
            reverse("note_create"),
            data={"title": "Created", "content": "Created body"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Note.objects.filter(title="Created").exists())

    def test_create_note_requires_title(self) -> None:
        """The create form should reject empty titles."""
        response = self.client.post(
            reverse("note_create"),
            data={"title": "", "content": "No title"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Note.objects.filter(content="No title").exists())
        self.assertContains(response, "This field is required", html=False)

    def test_update_note_via_view(self) -> None:
        """Posting valid data to the update view should update the note."""
        response = self.client.post(
            reverse("note_update", args=[self.note1.pk]),
            data={"title": "Updated", "content": "Updated body"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.note1.refresh_from_db()
        self.assertEqual(self.note1.title, "Updated")
        self.assertEqual(self.note1.content, "Updated body")

    def test_delete_note_via_view(self) -> None:
        """Posting to the delete view should remove the note."""
        response = self.client.post(
            reverse("note_delete", args=[self.note2.pk]),
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Note.objects.filter(pk=self.note2.pk).exists())
