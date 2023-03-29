
""" Prebuilt imports. """
import tkinter as tk
import os 
import sys

class Analyzer(tk.Frame): 

    """ A class representation of the analyzer. 
    
    ```
    
    Attributes
    ----------
    root : tk.Tk

    name_label : tk.Label
    date_label : tk.Label
    intent_label : tk.Label
    translation_label : tk.Label

    name_entry : tk.Entry
    date_entry : tk.Entry
    intent_entry : tk.Entry
    translation_entry : tk.Entry
    

    Methods
    -------
    super_config(): 
        Configures the super class.     
    configure():
        Configures various parts of the controller.
    label_config(): 
        Configures the labels. 
    """

    """ Initialize the class instance. 
    
    @return null
    """
    def __init__(self, root):

        self.set_root(root)
        super().__init__(self.get_root().get_container())
        
        self.destination_label = None 
        self.name_label = None 
        self.date_label = None 
        self.intent_label = None 
        self.translation_label = None

        self.destination_entry = None 
        self.name_entry = None 
        self.data_entry = None 
        self.intent_entry = None 
        self.translation_entry = None 

    """ Returns the controllers root. 
    
    @return root : The application
    @rtpye root : tk.Tk
    """
    def get_root(self): 
        return self.root
    
    """ Sets the controllers root.
    
    @param root : The application 
    @type root : tk.Tk
    """
    def set_root(self, root): 
        self.root = root 

    """ Return the destination label. 
    
    @return destination_label : The destination label. 
    @rtype destination_label : tk.Label
    """
    def get_destination_label(self): 
        return self.destination_label
    
    """ Sets the destination label. 
    
    @param destination_label : The destination label. 
    @type destination_label : tk.Label
    """
    def set_destination_label(self, destination_label): 
        self.destination_label = destination_label
        
    """ Return the name label. 
    
    @return name_label : The name label. 
    @rtype name_label : tk.Label
    """
    def get_name_label(self): 
        return self.name_label
    
    """ Sets the name label. 
    
    @param name_label : The name label. 
    @type name_label : tk.Label
    """
    def set_name_label(self, name_label): 
        self.name_label = name_label
        
    """ Return the date label. 
    
    @return date_label : The date label. 
    @rtype date_label : tk.Label
    """
    def get_date_label(self): 
        return self.date_label
    
    """ Sets the date label. 
    
    @param date_label : The date label. 
    @type date_label : tk.Label
    """
    def set_date_label(self, date_label): 
        self.date_label = date_label
    
    """ Return the intent label. 
    
    @return intent_label : The intent label. 
    @rtype intent_label : tk.Label
    """
    def get_intent_label(self): 
        return self.intent_label
    
    """ Sets the intent label. 
    
    @param intent_label : The intent label. 
    @type intent_label : tk.Label
    """
    def set_intent_label(self, intent_label): 
        self.intent_label = intent_label
        
    """ Return the translation label. 
    
    @return translation_label : The translation label. 
    @rtype translation_label : tk.Label
    """
    def get_translation_label(self): 
        return self.translation_label
    
    """ Sets the translation label. 
    
    @param translation_label : The translation label. 
    @type translation_label : tk.Label
    """
    def set_translation_label(self, translation_label): 
        self.translation_label = translation_label
        
    """ Return the destination entry. 
    
    @return destination_entry : The destination entry. 
    @rtype destination_entry : tk.Label
    """
    def get_destination_entry(self): 
        return self.destination_entry
    
    """ Sets the destination entry. 
    
    @param destination_entry : The destination entry. 
    @type destination_entry : tk.Label
    """
    def set_destination_entry(self, destination_entry): 
        self.destination_entry = destination_entry
    
    """ Return the name entry. 
    
    @return name_entry : The name entry. 
    @rtype name_entry : tk.Entry
    """
    def get_name_entry(self): 
        return self.name_entry
    
    """ Sets the name entry. 
    
    @param name_entry : The name entry. 
    @type name_entry : tk.Entry
    """
    def set_name_entry(self, name_entry): 
        self.name_entry = name_entry
        
    """ Return the date entry. 
    
    @return date_entry : The date entry. 
    @rtype date_entry : tk.Entry
    """
    def get_date_entry(self): 
        return self.date_entry
    
    """ Sets the date entry. 
    
    @param date_entry : The date entry. 
    @type date_entry : tk.Entry
    """
    def set_date_entry(self, date_entry): 
        self.date_entry = date_entry
    
    """ Return the intent entry. 
    
    @return intent_entry : The intent entry. 
    @rtype intent_entry : tk.Entry
    """
    def get_intent_entry(self): 
        return self.intent_entry
    
    """ Sets the intent entry. 
    
    @param intent_entry : The intent entry. 
    @type intent_entry : tk.Entry
    """
    def set_intent_entry(self, intent_entry): 
        self.intent_entry = intent_entry
        
    """ Return the translation entry. 
    
    @return translation_entry : The translation entry. 
    @rtype translation_entry : tk.Entry
    """
    def get_translation_entry(self): 
        return self.translation_entry
    
    """ Sets the translation entry. 
    
    @param translation_entry : The translation entry. 
    @type translation_entry : tk.Entry
    """
    def set_translation_entry(self, translation_entry): 
        self.translation_entry = translation_entry 

    """ Resets the entries. 
    
    @return null
    """
    def entry_reset(self): 

        self.get_destination_entry().delete(0, 'end')
        self.get_destination_entry().insert(0, "localhost:5000")  
        self.get_destination_entry().configure(fg="grey")  
 
        self.get_name_entry().delete(0, 'end')
        self.get_name_entry().insert(0, "Noah Jennings")  
        self.get_name_entry().configure(fg="grey")  
 
        self.get_date_entry().delete(0, 'end')
        self.get_date_entry().insert(0, "03282023") 
        self.get_date_entry().configure(fg="grey")
        
        self.get_intent_entry().delete(0, 'end')
        self.get_intent_entry().insert(0, "Greeting")
        self.get_intent_entry().configure(fg="grey") 

        self.get_translation_entry().delete(0, 'end')
        self.get_translation_entry().insert(0, "Hello")
        self.get_translation_entry().configure(fg="grey") 

    """ Places the entries. 
    
    @return null 
    """
    def entry_place(self): 

        self.get_destination_entry().grid(row=0, column=1)
        self.get_name_entry().grid(row=1, column = 1)
        self.get_date_entry().grid(row=2, column = 1)
        self.get_intent_entry().grid(row=3, column = 1)
        self.get_translation_entry().grid(row=4, column = 1)

    """ Configures the entries. 
    
    @return null
    """
    def entry_config(self): 
        
        self.set_destination_entry(tk.Entry(self))
        self.set_name_entry(tk.Entry(self))
        self.set_date_entry(tk.Entry(self))
        self.set_intent_entry(tk.Entry(self))
        self.set_translation_entry(tk.Entry(self))
        
        self.entry_reset()
        self.entry_place()

    """ Places the labels. 
    
    @return null 
    """
    def label_place(self): 

        self.get_destination_label().grid(row=0, column=0)
        self.get_name_label().grid(row=1, column = 0)
        self.get_date_label().grid(row=2, column = 0)
        self.get_intent_label().grid(row=3, column = 0)
        self.get_translation_label().grid(row=4, column = 0)

    """ Configures the labels. 
    
    @return null 
    """
    def label_config(self):
        
        self.set_destination_label(tk.Label(self, text="DESTINATION IP"))
        self.set_name_label(tk.Label(self, text="NAME: "))
        self.set_date_label(tk.Label(self, text="DATE: "))
        self.set_intent_label(tk.Label(self, text="INTENT: "))
        self.set_translation_label(tk.Label(self, text="TRANSLATION: "))

        self.label_place()
   
    """ Configures the super class. 
    
    @return null 
    """
    def super_config(self): 
        
        super().configure(highlightbackground="grey", 
                          highlightthickness=2,)
        super().grid(row=1, column=0, pady=(50, 0))
 
    """ Configures the controller. 
    
    @return null
    """
    def configure(self): 
       
        self.super_config()
        self.label_config()
        self.entry_config() 
