
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
    check_button : tk.Button
    reset_button : tk.Button
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
    reset(): 
        Resets the application.
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
        self.check_button = None 
        self.reset_button = None 
        self.close_button = None 

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
        
    """ Returns the controllers check button. 
    
    @return check_button : The check button. 
    @rtype check_button : tk.Button
    """
    def get_check_button(self): 
        return self.check_button 
    
    """ Sets the controllers check button. 
    
    @param check_button : The check button. 
    @type check_button : tk.Button 
    """
    def set_check_button(self, check_button): 
        self.check_button = check_button
        
    """ Returns the controllers reset button. 
    
    @return reset_button : The reset button. 
    @rtype reset_button : tk.Button
    """
    def get_reset_button(self): 
        return self.reset_button 
    
    """ Sets the controllers reset button. 
    
    @param reset_button : The reset button. 
    @type reset_button : tk.Button 
    """
    def set_reset_button(self, reset_button): 
        self.reset_button = reset_button

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

    """ Resets the application. 
    
    @return null 
    """
    def reset(self): 

        self.button_reset()
        self.get_root().get_analyzer().entry_reset()

    """ Closes the application. 
    
    @return null
    """
    def close(self): 
        self.get_root().destroy()

    """ Places the buttons. 
    
    @return null
    """
    def button_place(self): 

        self.get_start_button().grid(row=0, column=0)
        self.get_stop_button().grid(row=0, column=1)
        self.get_check_button().grid(row=0, column=2)
        self.get_reset_button().grid(row=0, column=3)
        self.get_close_button().grid(row=0, column=4)

    """ Resets button appearance. 
    
    @return null
    """
    def button_reset(self): 
        
        self.get_start_button().configure(state = "disabled", width=10)
        self.get_stop_button().configure(state = "disabled", width=10)
        self.get_check_button().configure(state='normal', width=10)
        self.get_reset_button().configure(state = "normal", width=10)
        self.get_close_button().configure(state = "normal", width=10)

    """ Configures the controllers buttons. 
    
    @return null
    """
    def button_config(self): 

        self.set_start_button(tk.Button(self, text='Start'))
        self.set_stop_button(tk.Button(self, text='Stop'))
        self.set_check_button(tk.Button(self, text="Check"))
        self.set_reset_button(tk.Button(self, text='Reset', command=self.reset))
        self.set_close_button(tk.Button(self, text='Close', command=self.close))

        self.button_reset()
        self.button_place()

    
    """ Configures the super class. 
    
    @return null 
    """
    def super_config(self): 
        
        super().configure(highlightbackground="black", 
                          highlightthickness=2,)
        super().grid(row=2, column=0, pady=(50, 0))
 
    """ Configures the controller. 
    
    @return null
    """
    def configure(self): 
       
        self.super_config()
        self.button_config()
