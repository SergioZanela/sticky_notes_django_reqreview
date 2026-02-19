"""Forms for creating and editing sticky notes."""

from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """ModelForm for creating and editing :class:`~notes.models.Note`."""

    class Meta:
        """Form configuration for the Note model."""

        model = Note
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title"}),
            "content": forms.Textarea(attrs={"placeholder": "Write your note..."}),
        }
