from typing import List
import json

__file_name__ = "recommendation.json"

class RecommendationModel:
    name: str
    recommended_by: str
    voters: List[str]

    def __init__(self, name: str, recommended_by: str) -> None:
        self.name = name
        self.recommended_by = recommended_by
        self.voters = []


def add_recommendation(recommendation: RecommendationModel):
    with open(__file_name__, "w") as f:
        json.dump(recommendation, f)


def open_file() -> List[RecommendationModel]:
    with open(__file_name__, "r") as f:
        return json.load(f)
