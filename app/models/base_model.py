from bson import ObjectId
from datetime import datetime, timezone
from dataclasses import dataclass, field


@dataclass
class BaseModel:
    id: str = field(default_factory=lambda: str(ObjectId()), init=False)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc), init=False)
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc), init=False)

    def update_timestamp(self):
        self.updated_at = datetime.now(timezone.utc)
