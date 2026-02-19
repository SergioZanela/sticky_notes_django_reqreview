"""Class-based views for listing and managing sticky notes."""

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import NoteForm
from .models import Note


class NoteListView(ListView):
    """Display a list of notes, ordered by most recently updated."""

    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"
    ordering = ["-updated_at"]


class NoteDetailView(DetailView):
    """Display a single note."""

    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"


class NoteCreateView(CreateView):
    """Create a new note."""

    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note_list")


class NoteUpdateView(UpdateView):
    """Update an existing note."""

    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note_list")


class NoteDeleteView(DeleteView):
    """Delete an existing note."""

    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("note_list")
