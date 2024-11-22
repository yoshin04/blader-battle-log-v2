from dataclass import dataclass
from uuid import UUID
from typing import Optional, Dict

@dataclass
class Blader:
    id: UUID
    name: str
    rank: int
    team_id: Optional[UUID] = None
    rank_history: Optional[Dict] = None
    win_rate: Optional[float] = None
