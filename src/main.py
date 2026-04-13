"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""


from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Edge-case / adversarial user profiles (Phase 4 testing)
    edge_case_profiles = [
        {
            "name": "High Energy Pop",
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9,
            "target_tempo": 130
        },
        {
            "name": "Chill Lofi",
            "favorite_genre": "lofi",
            "favorite_mood": "calm",
            "target_energy": 0.3,
            "target_tempo": 80
        },
        {
            "name": "Deep Intense Rock",
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "target_tempo": 160
        }
    ]

    # Run recommender for each profile
    for profile in edge_case_profiles:
        print("\n" + "=" * 50)
        print(f"PROFILE: {profile['name']}")
        print("=" * 50)

        recommendations = recommend_songs(profile, songs, k=5)

        print("\nTop recommendations:\n")

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print("Because:")
            for reason in explanation.split("; "):
                print(f"  - {reason}")
            print()


if __name__ == "__main__":
    main()