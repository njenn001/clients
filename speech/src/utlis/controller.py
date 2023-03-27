
""" Prebuilt imports. """
import tkinter as tk
import os 
import sys

class Controller(tk.Frame): 

    """ A class representation of the controller. 
    
    ```
    
    Attributes
    ----------
    root : tk.Tk
    
    start_button : tk.Button 
    stop_button : tk.Button 
    close_button : tk.Button
    

    Methods
    -------
    configure():
        Configures various parts of the controller.
    button_config():
        Configures the buttons.  
    button_place(): 
        Places the buttons. 
    button_reset():    
        Resets the buttons.
    run(): 
        Runs the speech analyzer. 
    close(): 
        Closes the application.
    """

    """ Initialize the class instance. 
    
    @return null
    """
    def __init__(self, root):

        self.set_root(root)
        super().__init__(self.get_root().get_container())

        self.start_button = None 
        self.stop_button = None 
        self.close_button = None 

        self.intent_label = None 
        self.translation_label = None

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

    """ Returns the controllers start button. 
    
    @return start_button : The start button. 
    @rtype start_button : tk.Button
    """
    def get_start_button(self): 
        return self.start_button 
    
    """ Sets the controllers start button. 
    
    @param start_button : The start button. 
    @type start_button : tk.Button 
    """
    def set_start_button(self, start_button): 
        self.start_button = start_button

    """ Returns the controllers stop button. 
    
    @return stop_button : The stop button
    @rtype stop_button : tk.Button
    """
    def get_stop_button(self):  
        return self.stop_button
    
    """ Sets the controllers stop button.
    
    @param stop_button : The stop button.
    @type stop_button : tk.Button 
    """
    def set_stop_button(self, stop_button): 
        self.stop_button = stop_button

    """ Return the controllers close button. 
    
    @return close_button : The close button. 
    @rtype close_button : tk.Button
    """
    def get_close_button(self): 
        return self.close_button
    
    """ Sets the controllers close button.
    
    @param close_button : The close button
    @type close_button : tk.Button
    """
    def set_close_button(self, close_button): 
        self.close_button = close_button 

    """ Closes the application. 
    
    @return null
    """
    def close(self): 
        self.get_root().destroy()
        sys.exit()

    """ Places the buttons. 
    
    @return null
    """
    def button_place(self): 

        self.get_start_button().grid(row=0, column=0)
        self.get_stop_button().grid(row=0, column=1)
        self.get_close_button().grid(row=0, column=2)

    """ Resets button appearance. 
    
    @return null
    """
    def button_reset(self): 
        
        self.get_start_button().configure(state = "disabled", width=10)
        self.get_stop_button().configure(state = "disabled", width=10)
        self.get_close_button().configure(state = "normal", width=10)

    """ Configures the controllers buttons. 
    
    @return null
    """
    def button_config(self): 

        self.set_start_button(tk.Button(self, text='Start'))
        self.set_stop_button(tk.Button(self, text='Stop'))
        self.set_close_button(tk.Button(self, text='Close', command=self.close))

        self.button_reset()
        self.button_place()

    
    """ Configures the super class. 
    
    @return null 
    """
    def super_config(self): 
        
        super().configure(highlightbackground="blue", 
                          highlightthickness=2,)
        super().grid(row=0, column=0, pady=(50, 0))
 
    """ Configures the controller. 
    
    @return null
    """
    def configure(self): 
       
        self.super_config()
        self.button_config()
        #self.input_config()

    """ Runs the application. 
    
    @return null
    """
    def run(self): 
        self.mainloop()