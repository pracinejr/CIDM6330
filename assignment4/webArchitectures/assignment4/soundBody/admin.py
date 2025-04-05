from django.contrib import admin

# Register your models here.
from .models import Musician, Exercise, Trainer


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = (
        "musicianId",
        "name",
        "email",
        "instrument",
        "fitnessLevel",
        "joinDate",
    )
    search_fields = ("name", "email")
    list_filter = ("fitnessLevel",)
    ordering = ("name",)
    fieldsets = (
        (None, {"fields": ("name", "email", "instrument", "fitnessLevel", "joinDate")}),
        ("CV Upload", {"fields": ("cv",)}),
    )

    def has_module_permission(self, request):
        return True


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "exerciseId",
        "name",
        "instructions",
        "muscleGroup",
        "difficultyLevel",
    )
    search_fields = ("name",)
    list_filter = ("muscleGroup", "difficultyLevel")
    ordering = ("name",)
    fieldsets = (
        (None, {"fields": ("name", "instructions", "muscleGroup", "difficultyLevel")}),
        ("CV Upload", {"fields": ("cv",)}),
    )

    def has_module_permission(self, request):
        return True


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = (
        "trainerId",
        "name",
        "email",
        "expertise",
        "certification",
        "joinDate",
    )
    search_fields = ("name", "email")
    list_filter = ("expertise",)
    ordering = ("name",)
    fieldsets = (
        (None, {"fields": ("name", "email", "expertise", "certification", "joinDate")}),
        ("CV Upload", {"fields": ("cv",)}),
    )

    def has_module_permission(self, request):
        return True
