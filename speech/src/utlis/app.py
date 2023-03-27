""" Prebuilt imports. """
import tkinter as tk

""" Class imports. """
from .controller import Controller

class App(tk.Tk): 

    """ A class representation of the application. 
    
    ```
    
    Attributes
    ----------

    title : str
    size : list 
    container : tk.Frame
    controller : tk.Frame
        

    Methods
    -------
    run(): 
        Runs the application. 

    """

    """ Initialize the class instance. 
    
    @return null
    """
    def __init__(self):
        super().__init__()

        self.title = "" 
        self.size = [] 
        
        self.container = None 
        self.controller = None 
        self.viewer = None

    """ Return the apps title. 
    
    @return title : The title
    @rtype title : str
    """
    def get_title(self): 
        return self.title 
    
    """ Sets the apps title. 
    
    @param title : The title
    @type title : str
    """
    def set_title(self, title): 
        self.title = title 

    """ Returns the apps size. 
     
    @return size : The size 
    @rtype size : list
    """
    def get_size(self): 
        return self.size 
    
    """ Sets the apps size. 
    
    @param size : The size 
    @type size : list
    """
    def set_size(self, size): 
        self.size = size 

    """ Returns the apps container. 
    
    @return container : The container
    @rtype container : tk.Frame
    """
    def get_container(self): 
        return self.container 
    
    """ Sets the apps container.
    
    @param container : The container 
    @type container : tk.Frame
    """
    def set_container(self, container): 
        self.container = container 

    """ Returns the apps controller. 
    
    @return controller : The controller
    @rtype controller : utils.Controller
    """
    def get_controller(self): 
        return self.controller 
    
    """ Sets the controller. 
    
    @param controller : The controller 
    @type controller : utils.Controller
    """
    def set_controller(self, controller): 
        self.controller = controller 

    """ Configures the container. 
    
    @return null
    """
    def container_config(self): 

        self.set_container(tk.Frame(self))
        self.get_container().pack()
        
    """ Configures the super class. 
    
    @return null 
    """
    def super_config(self): 
        
        geo = str(self.get_size()[0]) + "x" + str(self.get_size()[1]) 
        super().geometry(geo)

        super().title('Speech Data Analyzer')
        super().attributes("-topmost", True)
        super().resizable(width=False, height=False)

    """ Sets tk configurations. 
    
    @return null
    """
    def configure(self):

        self.set_size([400, 200])
        self.super_config()
        self.container_config()

        self.set_controller(Controller(self))
        self.get_controller().configure()

    """ Runs the application. 
    
    @return null
    """
    def run(self): 

        self.configure()
        self.mainloop()