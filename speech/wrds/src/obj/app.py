""" Prebuilt imports. """
import tkinter as tk

""" Class imports. """
from .controller import Controller
from .analyzer import Analyzer 
from .status import Status

class App(tk.Tk): 

    """ A class representation of the application. 
    
    ```
    
    Attributes
    ----------

    title : str
    size : list 
    container : tk.Frame
    controller : tk.Frame
    analyzer : tk.Frame
        

    Methods
    -------
    configure(): 
        Configures various parts of the application. 
    super_config(): 
        Configures the super class. 
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

        self.status = None 
        self.controller = None 
        self.analyzer = None 
        
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

    """ Returns the apps status. 
    
    @return status : The status
    @rtype status : utils.Status
    """
    def get_status(self): 
        return self.status 
    
    """ Sets the apps status. 
    
    @param status : The status 
    @type status : utils.Status
    """
    def set_status(self, status): 
        self.status = status 

    """ Returns the apps controller. 
    
    @return controller : The controller
    @rtype controller : utils.Controller
    """
    def get_controller(self): 
        return self.controller 
    
    """ Sets the apps controller. 
    
    @param controller : The controller 
    @type controller : utils.Controller
    """
    def set_controller(self, controller): 
        self.controller = controller 

    """ Returns the apps analyzer. 
    
    @return analyzer : The analyzer.
    @rtype analyzer : utils.Analyzer 
    """
    def get_analyzer(self): 
        return self.analyzer
    
    """ Sets the apps analyzer. 
    
    @param analyzer : The analyzer.
    @type analyzer : utils.Analyzer
    """
    def set_analyzer(self, analyzer): 
        self.analyzer = analyzer 

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
        
        super().title('Speech Data Analyzer')
        super().attributes("-topmost", True)
        super().resizable(width=False, height=False)

    """ Sets tk configurations. 
    
    @return null
    """
    def configure(self):

        self.super_config()
        self.container_config()

        self.set_status(Status(self))

        self.set_controller(Controller(self))
        self.get_controller().configure()

        self.set_analyzer(Analyzer(self))
        self.get_analyzer().configure()

    """ Runs the application. 
    
    @return null
    """
    def run(self): 

        self.configure()
        self.mainloop()