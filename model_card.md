# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeMatch Recommender 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender system is designed to suggest songs based on a user's preferences for genre, mood, energy, and tempo. It generates a ranked list of songs that best match these features using a simple scoring system. It assumes that user preferences can be represented using numerical and categorical features. This system is intended for classroom learning and experimentation, not for real-world music recommendations.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model works by comparing each song’s features with a user’s preferences. It uses genre and mood matches as categorical signals and calculates similarity scores for numerical features like energy and tempo. Each match contributes to a total score, and songs with higher scores are ranked higher. The final recommendations are the top-scoring songs after all comparisons. This is a simplified version of real-world recommender systems that use weighted scoring.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset contains a small collection of songs stored in a CSV file with about 18 songs. Each song includes features such as genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset includes a limited range of genres and moods, so it does not represent all types of music. No data was removed, but additional synthetic songs were added to increase variety. Some aspects of musical taste, such as lyrics and cultural context, are not included.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for simple and clearly defined user preferences, such as high-energy pop or calm chill music. It correctly identifies songs that match strong feature patterns like high energy or matching mood. The scoring system is transparent, so it is easy to understand why a song was recommended. It performs especially well when user preferences align closely with available song features.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The recommender system only uses a few features like genre, mood, energy, and tempo. Because of this, it does not capture more detailed aspects of music such as lyrics or emotional meaning. Some genres or moods may be overrepresented in the dataset, which can create bias in recommendations. The scoring system can also over-prioritize certain features depending on the weights. This can cause different users to receive similar recommendations even when their preferences are different.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the recommender using different user profiles such as High Energy Pop, Chill Lofi, and Deep Intense Rock. The system produced different rankings for each profile, showing that it responds to changes in user preferences. I looked at whether the top songs matched the expected mood, genre, and energy levels. One thing I noticed was that some songs appeared across multiple profiles, especially when they had balanced feature values. Overall, the results made sense but showed limitations in personalization due to the simple scoring system.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Future improvements could include adding more features such as lyrics or listening history. The system could also be improved by increasing dataset size and diversity to reduce bias. Another improvement would be to introduce diversity in recommendations so that similar songs are not always ranked at the top. Finally, user feedback could be used to dynamically adjust weights in the scoring system.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

This project helped me understand how recommender systems turn user preferences into ranked outputs using simple weighted scoring. I learned that even basic algorithms can produce realistic-looking recommendations. I was surprised by how sensitive the system is to small changes in feature weights. Using AI tools helped speed up debugging and implementation, but I still needed to understand and fix logic errors myself. This project changed how I think about recommendation systems and how platforms like Spotify might prioritize different features.