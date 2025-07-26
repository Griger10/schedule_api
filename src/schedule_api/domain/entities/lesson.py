from dataclasses import dataclass


@dataclass
class LessonDM:
    lesson_id: int
    lesson_name: str
    lesson_slug: str
