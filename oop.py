
# coding: utf-8

# In[1]:


class Man:
    """functions of class """

    def __init__(self, name):
        self.name = name
        print("Initilized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")


# In[2]:


m =Man("Dawld") 


# In[3]:


m.hello()


# In[4]:


m.goodbye()

