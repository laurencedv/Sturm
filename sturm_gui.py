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
        self.mi_tool_opedit = wx.MenuItem( self.menu_tool, wx.ID_ANY, u"opEdit", wx.EmptyString, wx.ITEM_NORMAL )
        self.mi_tool_opedit.SetBitmap( wx.Bitmap( u"media/opEdit-small.png", wx.BITMAP_TYPE_ANY ) )
        self.menu_tool.Append( self.mi_tool_opedit )

        self.mi_tool_opcnc = wx.MenuItem( self.menu_tool, wx.ID_ANY, u"opCnC", wx.EmptyString, wx.ITEM_NORMAL )
        self.mi_tool_opcnc.SetBitmap( wx.Bitmap( u"media/opCnC-small.png", wx.BITMAP_TYPE_ANY ) )
        self.menu_tool.Append( self.mi_tool_opcnc )

        self.menu_tool.AppendSeparator()

        self.mi_tool_oplog = wx.MenuItem( self.menu_tool, wx.ID_ANY, u"opLog", wx.EmptyString, wx.ITEM_NORMAL )
        self.mi_tool_oplog.SetBitmap( wx.Bitmap( u"media/opLog-small.png", wx.BITMAP_TYPE_ANY ) )
        self.menu_tool.Append( self.mi_tool_oplog )

        self.mi_tool_opview = wx.MenuItem( self.menu_tool, wx.ID_ANY, u"opView", wx.EmptyString, wx.ITEM_NORMAL )
        self.mi_tool_opview.SetBitmap( wx.Bitmap( u"media/opView-small.png", wx.BITMAP_TYPE_ANY ) )
        self.menu_tool.Append( self.mi_tool_opview )

        self.mi_tool_opgraph = wx.MenuItem( self.menu_tool, wx.ID_ANY, u"opGraph", wx.EmptyString, wx.ITEM_NORMAL )
        self.mi_tool_opgraph.SetBitmap( wx.Bitmap( u"media/opGraph-small.png", wx.BITMAP_TYPE_ANY ) )
        self.menu_tool.Append( self.mi_tool_opgraph )

        self.mi_tool_oparchive = wx.MenuItem( self.menu_tool, wx.ID_ANY, u"opArchive", wx.EmptyString, wx.ITEM_NORMAL )
        self.mi_tool_oparchive.SetBitmap( wx.Bitmap( u"media/opArchive-small.png", wx.BITMAP_TYPE_ANY ) )
        self.menu_tool.Append( self.mi_tool_oparchive )

        self.m_menubar1.Append( self.menu_tool, u"Tool" )

        self.menu_view = wx.Menu()
        self.mi_view_operationmap = wx.MenuItem( self.menu_view, wx.ID_ANY, u"Operation Map", wx.EmptyString, wx.ITEM_NORMAL )
        self.mi_view_operationmap.SetBitmap( wx.Bitmap( u"media/opMap-small.png", wx.BITMAP_TYPE_ANY ) )
        self.menu_view.Append( self.mi_view_operationmap )

        self.m_menubar1.Append( self.menu_view, u"View" )

        self.menu_help = wx.Menu()
        self.mi_help_about = wx.MenuItem( self.menu_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_help.Append( self.mi_help_about )

        self.m_menubar1.Append( self.menu_help, u"Help" )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.file_open_cb, id = self.mi_file_open.GetId() )
        self.Bind( wx.EVT_MENU, self.onClose, id = self.mi_file_exit.GetId() )
        self.Bind( wx.EVT_MENU, self.opedit_create_cb, id = self.mi_tool_opedit.GetId() )
        self.Bind( wx.EVT_MENU, self.opcnc_create_cb, id = self.mi_tool_opcnc.GetId() )
        self.Bind( wx.EVT_MENU, self.oplog_create_cb, id = self.mi_tool_oplog.GetId() )
        self.Bind( wx.EVT_MENU, self.opview_create_cb, id = self.mi_tool_opview.GetId() )
        self.Bind( wx.EVT_MENU, self.opgraph_create_cb, id = self.mi_tool_opgraph.GetId() )
        self.Bind( wx.EVT_MENU, self.oparchive_create_cb, id = self.mi_tool_oparchive.GetId() )
        self.Bind( wx.EVT_MENU, self.opmap_view_cb, id = self.mi_view_operationmap.GetId() )
        self.Bind( wx.EVT_MENU, self.about_view_cb, id = self.mi_help_about.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def file_open_cb( self, event ):
        event.Skip()

    def onClose( self, event ):
        event.Skip()

    def opedit_create_cb( self, event ):
        event.Skip()

    def opcnc_create_cb( self, event ):
        event.Skip()

    def oplog_create_cb( self, event ):
        event.Skip()

    def opview_create_cb( self, event ):
        event.Skip()

    def opgraph_create_cb( self, event ):
        event.Skip()

    def oparchive_create_cb( self, event ):
        event.Skip()

    def opmap_view_cb( self, event ):
        event.Skip()

    def about_view_cb( self, event ):
        event.Skip()


