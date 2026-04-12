import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    
    songs = []
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convert numerical fields to float/int
                song = {
                    'id': int(row['id']),
                    'title': row['title'],
                    'artist': row['artist'],
                    'genre': row['genre'],
                    'mood': row['mood'],
                    'energy': float(row['energy']),
                    'tempo_bpm': int(row['tempo_bpm']),
                    'valence': float(row['valence']),
                    'danceability': float(row['danceability']),
                    'acousticness': float(row['acousticness'])
                }
                songs.append(song)
        
        print(f"Successfully loaded {len(songs)} songs.")
        return songs
    
    except FileNotFoundError:
        print(f"Error: File '{csv_path}' not found.")
        return []
    except KeyError as e:
        print(f"Error: Missing expected column in CSV: {e}")
        return []
    except ValueError as e:
        print(f"Error: Could not convert field to number: {e}")
        return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    reasons = []
    total_score = 0.0
    
    # Genre match: +2.0 if matches
    if song['genre'] == user_prefs['favorite_genre']:
        total_score += 2.0
        reasons.append("genre match (+2.0)")
    else:
        reasons.append("genre mismatch (0.0)")
    
    # Mood match: +1.0 if matches
    if song['mood'] == user_prefs['favorite_mood']:
        total_score += 1.0
        reasons.append("mood match (+1.0)")
    else:
        reasons.append("mood mismatch (0.0)")
    
    # Energy similarity: 1 - abs(song_energy - user_energy)
    energy_diff = abs(song['energy'] - user_prefs['target_energy'])
    energy_similarity = 1 - energy_diff
    total_score += energy_similarity
    reasons.append(f"energy similarity ({energy_similarity:.2f})")
    
    # Tempo similarity: 1 - abs(song_tempo - user_tempo) / 200
    tempo_diff = abs(song['tempo_bpm'] - user_prefs['target_tempo'])
    tempo_similarity = 1 - (tempo_diff / 200)
    total_score += tempo_similarity
    reasons.append(f"tempo similarity ({tempo_similarity:.2f})")
    
    return total_score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Score each song and collect results
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))
    
    # Sort by score descending
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    
    # Return top k
    return scored_songs[:k]
