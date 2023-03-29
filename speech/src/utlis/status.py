
""" Prebuilt imports. """
import tkinter as tk
import socket 

class Status(tk.Frame): 

    """ A class representation of the status bar. 
    
    ```
    
    Attributes
    ----------
    root : tk.Tk

    ip_label : tk.Label
    hostname_label : tk.Label
    status_label : tk.Label 
    recording_label : tk.Label

    ip_addr : tk.Label 
    hostname : tk.Label 
    status : tk.label
    recording : tk.label

    system_status = False
    audio_recording = False 

    Methods
    -------
    super_config(): 
        Configures the super class.     
    configure():
        Configures various parts of the controller.
    init(): 
        Init the status bar. 
    """

    """ Initialize the class instance. 
    
    @return null
    """
    def __init__(self, root):

        self.set_root(root)
        super().__init__(self.get_root().get_container())
        
        self.ip_label = None 
        self.hostname_label = None 
        self.status_label = None 
        self.recording_label = None 

        self.ip_addr = None 
        self.hostname = None 
        self.status = False
        self.recording = False

        self.configure() 
        self.init()

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

    """ Returns the controllers ip label. 
    
    @return ip_label : The ip label.
    @rtype ip_label : tk.Label 
    """
    def get_ip_label(self): 
        return self.ip_label
    
    """ Sets the controllers ip label. 
    
    @param ip_label : The ip label. 
    @type ip_label : tk.Label
    """
    def set_ip_label(self, ip_label): 
        self.ip_label = ip_label 

    """ Returns the controllers hostname label. 
    
    @return hostname_label : The hostname label.
    @rtype hostname_label : tk.Label 
    """
    def get_hostname_label(self): 
        return self.hostname_label
    
    """ Sets the controllers hostname label. 
    
    @param hostname_label : The hostname label. 
    @type hostname_label : tk.Label
    """
    def set_hostname_label(self, hostname_label): 
        self.hostname_label = hostname_label 

    """ Returns the controllers status label. 
    
    @return status_label : The status label. 
    @rtype status_label : tk.Label
    """
    def get_status_label(self): 
        return self.status_label 
    
    """ Sets the controllers status label. 
    
    @param status_label : The status label. 
    @type status_label : tk.Label 
    """
    def set_status_label(self, status_label): 
        self.status_label = status_label 

    """ Returns the controllers recording label. 
    
    @return recording_label : The recording label. 
    @rtype recording_label : tk.Label
    """
    def get_recording_label(self): 
        return self.recording_label
    
    """ Sets the controllers recording label.
    
    @param recording_label : The recording label. 
    @type recording_label : tk.Label
    """
    def set_recording_label(self, recording_label): 
        self.recording_label = recording_label 

    """ Returns the controllers ip address. 
    
    @return ip_addr : The ip address.
    @rtype ip_addr : tk.Label 
    """
    def get_ip_addr(self): 
        return self.ip_addr
    
    """ Sets the controllers ip address. 
    
    @param ip_addr : The ip address. 
    @type ip_addr : tk.Label
    """
    def set_ip_addr(self, ip_addr): 
        self.ip_addr = ip_addr 

    """ Returns the controllers hostname. 
    
    @return hostname : The hostname.
    @rtype hostname : tk.Label 
    """
    def get_hostname(self): 
        return self.hostname
    
    """ Sets the controllers hostname. 
    
    @param hostname : The hostname. 
    @type hostname : tk.Label
    """
    def set_hostname(self, hostname): 
        self.hostname = hostname 

    """ Returns the controllers status. 
    
    @return status : The status. 
    @rtype status : tk.Label
    """
    def get_status(self): 
        return self.status 
    
    """ Sets the controllers status. 
    
    @param status : The status. 
    @type status : tk.Label 
    """
    def set_status(self, status): 
        self.status = status 

    """ Returns the controllers recording. 
    
    @return recording : The recording. 
    @rtype recording : tk.Label
    """
    def get_recording(self): 
        return self.recording
    
    """ Sets the controllers recording.
    
    @param recording : The recording. 
    @type recording : tk.Label
    """
    def set_recording(self, recording): 
        self.recording = recording 

    """ Places the labels. 
    
    @return null 
    """
    def label_place(self): 

        self.get_ip_label().grid(row=0, column=0)
        self.get_hostname_label().grid(row=0, column=3)
        self.get_status_label().grid(row=0, column=5)
        self.get_recording_label().grid(row=0, column=7)

        print()

    """ Configures the labels. 
    
    @return null 
    """
    def label_config(self):

        self.set_ip_label(tk.Label(self, text="IP Address: "))
        self.set_hostname_label(tk.Label(self, text="Hostname: "))
        self.set_status_label(tk.Label(self, text="Status: "))
        self.set_recording_label(tk.Label(self, text="Recording: "))
        
        self.label_place()
   
    """ Configures the super class. 
    
    @return null 
    """
    def super_config(self): 
        
        super().configure(highlightbackground="grey", 
                          highlightthickness=2,)
        super().grid(row=0, column=0, pady=(0, 20))
 
    """ Configures the controller. 
    
    @return null
    """
    def configure(self): 
       
        self.super_config()
        self.label_config()

    """ Initialize the Status bar. 
    
    @return null 
    """
    def init(self): 

        self
