import pandas as pd
import matplotlib.pyplot as plt


def generate_chart(candidates):

    df = pd.DataFrame({
        "Candidate": [c.name for c in candidates],
        "Votes": [c.votes for c in candidates]
    })

    plt.figure(figsize=(8, 5))

    plt.bar(
        df["Candidate"],
        df["Votes"]
    )

    plt.title("Resultados de la Votacion")

    plt.xlabel("Candidatos")

    plt.ylabel("Votos")

    plt.savefig("votes_chart.png")

    plt.close()