from dataclasses import dataclass,field
@dataclass
class Member:
    name: str
    member_id: str
    session_attended: int = 0
    calories_burned: list[int] = field(default_factory=list)
    def log_session(self, calories: int):
        self.session_attended += 1
        self.calories_burned.append(calories)
    def avg_calories(self) -> float:
        return sum(self.calories_burned)/len(self.calories_burned) if self.calories_burned else 0.0
@dataclass
class FitnessClass:
    class_name: str
    instructor: str
    capacity: int
    members: list["Member"] = field(default_factory=list)
    enrolled: int = field(init=False)
    def __post_init__(self):
        self._refresh()
    def _refresh(self):
        self.enrolled = len(self.members)
    def enroll(self, member: Member) -> bool:
        if self.enrolled >= self.capacity:
            return False
        self.members.append(member)
        self._refresh()
        return True
    def best_performer(self) -> str:
        if not self.members:
            return "No data"
        top_member = max(self.members, key=lambda m: m.avg_calories())
        if top_member.avg_calories == 0.0:
            return "No data"
        return top_member.name
    def class_stats(self) -> str:
        self._refresh()
        res = f"{self.class_name} ({self.instructor}):\n"
        for m in self.members:
            res += f"  {m.name} - {m.session_attended} sessions, avg {m.avg_calories():.1f} cal\n"
        res += f"Enrolled: {self.enrolled}/{self.capacity}"
        return res
