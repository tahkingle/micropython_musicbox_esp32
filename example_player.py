import time
import machine

from note_definitions import parse_melody


BUZZER_PIN = 9
BPM = 180

DEMO_MELODY = [
    'RQ', 'RQ', 'Q-E4', 'Q-F#4',
    'Q-G#4', 'Q-A4', 'Q-B4', 'Q-C#5',
    'H-E5', 'Q-D5', 'Q-C#5', 'Q-B4',
    'H-A4', 'RQ'
]


def _set_duty(pwm, on):
    value = 32768 if on else 0
    try:
        pwm.duty_u16(value)
    except AttributeError:
        pwm.duty(512 if on else 0)


def play_melody(melody_tokens, pin=BUZZER_PIN, bpm=BPM):
    pwm = machine.PWM(machine.Pin(pin))
    _set_duty(pwm, False)

    for freq, duration_ms in parse_melody(melody_tokens, bpm=bpm):
        if freq > 0:
            pwm.freq(int(freq))
            _set_duty(pwm, True)
        else:
            _set_duty(pwm, False)
        time.sleep_ms(duration_ms)

    _set_duty(pwm, False)
    pwm.deinit()


if __name__ == "__main__":
    play_melody(DEMO_MELODY)
