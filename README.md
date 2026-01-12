# pet-class

Simple digital pet with personality-driven needs.

## Usage

```bash
python3 -i pet.py
```

```python
from pet import Pet

pet = Pet("Mochi", personality="energetic")
print(pet.get_status())

pet.feed(amount=20)
pet.play(duration=15)
print(pet.get_status())
```