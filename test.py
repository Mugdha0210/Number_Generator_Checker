#!/usr/bin/env python
# coding: utf-8

# In[1]:


# load json and create model
def loadModel():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    
    # load weights into new model
    loaded_model.load_weights("model.h5")
    return loaded_model


# In[ ]:


from numpy import genfromtxt


# In[ ]:


def testPNG(model, filename, number):  
    my_data = genfromtxt(filename, delimiter=',')
    
    #reshaping array 
    my_data = my_data.reshape(28, 28)
    my_data = my_data.reshape(1, 28, 28, 1)
    
    y_test = np.array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
    y_test[number] = 1.
    score = model.evaluate(my_data, y_test, verbose=0) 
    accuracy = score[1]
    
    #likelihood of each number in terms of probability
    prob_array = model.predict(my_data)
    
    #returns a probability array of size 1, 10
    return [accuracy, prob_array]

