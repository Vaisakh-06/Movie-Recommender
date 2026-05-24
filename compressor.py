import pickle
import numpy as np

similarity = pickle.load(open('similarity.pkl','rb'))
similarity = np.array(similarity, dtype=np.float32)

pickle.dump(similarity, open('similarity.pkl', 'wb'))