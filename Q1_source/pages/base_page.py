#https://github.com/s376782/HIT137_2024_S2_CAS_072_Assignment3/tree/main/Q1_source
from tkinter import Frame

class BasePage(Frame):
    '''
    BasePage is a template for screens in a Tkinter app. It manages layout, filling the screen,
    and can be extended with custom functionality. Supports encapsulation, method overriding, 
    and can work with multiple inheritance if needed.
    '''

    def __init__(self, master, controller):
        '''
        Initializes BasePage with layout settings and a main frame.
        Can be overridden for page-specific functionality.

        Args:
            master: The root window or parent widget.
            controller: A reference to the controller managing page navigation.
        '''
        super().__init__(master)

        self._controller = controller
        '''(protected) used by derived classes for navigation'''

        # Get screen width and height
        self._screen_width = master.winfo_screenwidth()
        '''(protected) used to store width of screen'''
        self._screen_height = master.winfo_screenheight()
        '''(protected) used to store height of screen'''
        # Set the main_frame to fill the screen
        self._main_frame = Frame(self, bg="#FFFFFF", height=self._screen_height, width=self._screen_width)
        '''(protected) main content frame'''

        self._main_frame.pack(fill="both", expand=True)  # Ensure it expands to fill the entire screen

        # self.main_frame.pack_propagate(0)
        self._main_frame.grid_rowconfigure(0, weight=1)
        self._main_frame.grid_columnconfigure(0, weight=1)
