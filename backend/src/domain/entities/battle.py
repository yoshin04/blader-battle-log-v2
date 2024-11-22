from dataclasses import dataclass
from uuid import uuid
from datetime import datetime
from enum import Enum

class FinishType(Enum):
  SPIN = ("spin", 1) # スピンフィニッシュ
  BURST = ("burst", 2) # バーストフィニッシュ
  OVER = ("over", 2) # オーバーフィニッシュ
  EXTREME = ("extreme", 3) # エクストリームフィニッシュ

@dataclass
class Battle:
  id: UUID
  blader_id: UUID
  beyblade_id: UUID
  opponet_id: uuid
  finish_type: FinishType
  points_earned: int
  points_lost: int
  is_winner: bool
  date: datetime

  def validate(self) -> bool:
    # 勝者のみfinish_typeを設定可能
    if not self.is_winner and self.finish_type:
      return False
    
    # ポイントとフィニッシュタイプの整合性
    if self.is_winner and self.points_earned != self.finish_type.value[1]:
      return False
    
    return True
  
  @property
  def points(self) -> int:
    return self.points_earned if self.is_winner else self.points_lost
