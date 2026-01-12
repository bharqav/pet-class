"""A simple digital pet with personality-driven needs."""

from __future__ import annotations

from typing import Dict, List


def _clamp(value: float, lower: float = 0.0, upper: float = 100.0) -> float:
    return max(lower, min(upper, value))


class Pet:
    """Represents a digital pet with basic needs and a personality."""

    PERSONALITY_PRESETS: Dict[str, Dict[str, float]] = {
        "balanced": {"happiness_gain": 1.0, "hunger_drain": 1.0},
        "energetic": {"happiness_gain": 1.2, "hunger_drain": 1.3},
        "chill": {"happiness_gain": 0.9, "hunger_drain": 0.8},
        "curious": {"happiness_gain": 1.1, "hunger_drain": 1.0},
        "grumpy": {"happiness_gain": 0.8, "hunger_drain": 1.0},
    }

    def __init__(
        self,
        name: str,
        personality: str = "balanced",
        hunger: float = 50.0,
        happiness: float = 50.0,
    ) -> None:
        self.name = name
        self.personality = personality if personality in self.PERSONALITY_PRESETS else "balanced"
        self.hunger = _clamp(hunger)
        self.happiness = _clamp(happiness)

    def feed(self, amount: float = 15.0) -> Dict[str, object]:
        """Reduce hunger and slightly boost happiness."""
        self.hunger = _clamp(self.hunger - amount)
        self.happiness = _clamp(self.happiness + amount * 0.1)
        return self.get_status()

    def play(self, duration: float = 10.0) -> Dict[str, object]:
        """Play with the pet; affects hunger and happiness based on personality."""
        modifiers = self.PERSONALITY_PRESETS[self.personality]
        happiness_gain = duration * 0.8 * modifiers["happiness_gain"]
        hunger_increase = duration * 0.6 * modifiers["hunger_drain"]

        self.happiness = _clamp(self.happiness + happiness_gain)
        self.hunger = _clamp(self.hunger + hunger_increase)
        return self.get_status()

    def get_status(self) -> Dict[str, object]:
        """Return the current status of the pet."""
        return {
            "name": self.name,
            "personality": self.personality,
            "hunger": round(self.hunger, 1),
            "happiness": round(self.happiness, 1),
            "mood": self._derive_mood(),
            "needs": self._needs(),
        }

    def _derive_mood(self) -> str:
        if self.happiness >= 75 and self.hunger <= 40:
            return "joyful"
        if self.happiness >= 50 and self.hunger <= 60:
            return "content"
        if self.hunger >= 80:
            return "starving"
        if self.happiness <= 25:
            return "sad"
        return "restless"

    def _needs(self) -> List[str]:
        needs: List[str] = []
        if self.hunger >= 70:
            needs.append("feed soon")
        if self.happiness <= 35:
            needs.append("play together")
        if not needs:
            needs.append("doing fine")
        return needs

    def __repr__(self) -> str:
        status = self.get_status()
        return (
            f"Pet(name={status['name']!r}, personality={status['personality']!r}, "
            f"hunger={status['hunger']}, happiness={status['happiness']}, "
            f"mood={status['mood']!r})"
        )
