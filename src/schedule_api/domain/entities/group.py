from dataclasses import dataclass


@dataclass(slots=True)
class GroupDM:
    group_id: int
    group_name: str
    group_slug: str
