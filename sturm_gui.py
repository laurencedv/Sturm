# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sturm", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.menu_file = wx.Menu()
        self.mi_file_open = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open...", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_file.Append( self.mi_file_open )

        self.mi_file_exit = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_file.Append( self.mi_file_exit )

        self.m_menubar1.Append( self.menu_file, u"File" )

        self.menu_tool = wx.Menu()
        self.m_menubar1.Append( self.menu_tool, u"Tool" )

        self.menu_help = wx.Menu()
        self.m_menubar1.Append( self.menu_help, u"Help" )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.onClose, id = self.mi_file_exit.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onClose( self, event ):
        event.Skip()


