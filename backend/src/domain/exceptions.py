class DomainError(Exception):
  def __init__(self, code: str, message: str):
      self.code = code
      self.message = message

class BladerNotFoundError(DomainError):
  def __init__(self):
      super().__init__(
          code="BLADER_NOT_FOUND",
          message="指定されたブレーダーが見つかりません"
      )

class InvalidBattleDataError(DomainError):
  def __init__(self, detail: str):
      super().__init__(
          code="INVALID_BATTLE_DATA",
          message=f"バトルデータが不正です: {detail}"
      )