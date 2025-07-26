from dataclasses import dataclass


@dataclass
class ScheduleDM:
    schedule_id: int
    number_of_lessons: int
    audience: str
    week_type: bool | None
    is_active: bool
    lesson_id: int
    group_id: int
