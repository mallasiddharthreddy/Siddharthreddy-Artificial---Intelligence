import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would use my time wisely and not procatinate, cuz you might end up regretting later!:)"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

