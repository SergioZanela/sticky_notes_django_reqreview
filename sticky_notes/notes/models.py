"""Database models for the sticky notes application."""

from django.db import models


class Note(models.Model):
    """A single sticky note stored in the database."""

    title = models.CharField(max_length=200)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return a human-readable representation of the note."""
        return self.title
