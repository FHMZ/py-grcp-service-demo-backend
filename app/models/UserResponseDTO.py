
class UserResponseDTO:
    def __init__(self, id: int, name: str, trx_id: str):
        self.id = id
        self.name = name
        self.trx_id = trx_id

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "trxId": self.trx_id
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'UserResponseDTO':
        return cls(
            id=data['id'],
            name=data['name'],
            trx_id=data['trx_id']
        )

