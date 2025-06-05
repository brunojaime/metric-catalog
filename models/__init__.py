from dataclasses import dataclass, field, asdict
from typing import List, Optional
import re

@dataclass
class AttributeMetadata:
    attribute_id: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    examples: List[str] = field(default_factory=list)
    semantic_purpose: Optional[str] = None
    synonyms: List[str] = field(default_factory=list)
    common_phrases: List[str] = field(default_factory=list)
    preferred_in_prompt: Optional[bool] = None
    weight: Optional[float] = None
    confusable_with: List[str] = field(default_factory=list)
    usage_notes: Optional[str] = None
    example_questions: List[str] = field(default_factory=list)

    @staticmethod
    def generate_attribute_id(display_name: str) -> str:
        return re.sub(r"\s+", "_", display_name.strip().lower())

    @classmethod
    def from_display_name(cls, display_name: str) -> "AttributeMetadata":
        return cls(
            attribute_id=cls.generate_attribute_id(display_name),
            display_name=display_name
        )

    def to_dict(self) -> dict:
        return asdict(self)
