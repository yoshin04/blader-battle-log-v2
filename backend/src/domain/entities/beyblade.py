from dataclasses import dataclass
from uuid import UUID
from enum import Enum

class BetType(Enum):
  ATTACK = 'attack'
  DEFENSE = 'defense'
  BALANCE = 'balance'
  STAMINA = 'stamina'

@dataclass
class Blade:
  id: UUID
  name: str
  attack: int
  defense: int
  stamina: int
  weight: float

@dataclass
class Ratchet:
  id: UUID
  name: str
  attack: int
  defense: int
  stamina: int
  weight: float

@dataclass
class Bit:
  id: UUID
  name: str
  attack: int
  defense: int
  stamina: int
  dash: int
  burst_resistance: int
  weight: float

@dataclass
class BeyBlade:
  id: UUID
  blade_id: UUID
  ratchet_id: UUID
  bit_id: UUID
  type: BetType
  is_environment: bool
  environment_score: Optional[int] = None
  memo: Optional[str] = None
