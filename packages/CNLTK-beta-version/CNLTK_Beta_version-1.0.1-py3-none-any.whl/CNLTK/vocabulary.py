import pickle

with open("models/vocab_model2.pkl", "rb") as f:
        vocab_model = pickle.load(f)
        
print(vocab_model)

# VOCABULARY OF THE MODEL
def get_VOCAB_model():
    with open("models/vocab_model2.pkl", "rb") as f:
        vocab_model = pickle.load(f)
        
    return vocab_model