# micropython_musicbox_esp32

MicroPython note/rhythm helpers for ESP32 projects with buzzers or speakers.

## What is included
- `note_definitions.py`: note/frequency conversion + tokenized rhythm parser
- `example_player.py`: simple PWM melody player for ESP32

## Melody token format
- Notes: `<duration>-<note><octave>`
  - Examples: `Q-E4`, `H.-A5`, `E-C#5`
- Rests: `R<duration>`
  - Examples: `RQ`, `RE`, `RH.`

Supported duration codes:
- Notes: `W`, `H`, `Q`, `E`, `S`, `T` and dotted variants like `Q.`
- Rests: `RW`, `RH`, `RQ`, `RE`, `RS`, `RT` and dotted variants like `RQ.`

## Quick start
1. Copy `note_definitions.py` and `example_player.py` to your MicroPython board.
2. Update `BUZZER_PIN` in `example_player.py` to match your wiring.
3. Run:

```python
import example_player
example_player.play_melody(example_player.DEMO_MELODY)
```

## Notes
- `parse_melody()` returns `(frequency_hz, duration_ms)` tuples.
- Rests are emitted as `frequency_hz = 0`.
- If you use passive buzzers, PWM output works well; active buzzers may need on/off logic only.
