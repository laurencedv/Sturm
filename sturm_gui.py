# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.propgrid as pg

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

        self.status_main = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.tab_main = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_CLOSE_ON_ACTIVE_TAB|wx.aui.AUI_NB_DEFAULT_STYLE|wx.aui.AUI_NB_MIDDLE_CLICK_CLOSE|wx.aui.AUI_NB_SCROLL_BUTTONS|wx.aui.AUI_NB_TAB_MOVE|wx.aui.AUI_NB_TAB_SPLIT )
        self.m_panel1 = wx.Panel( self.tab_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.tab_main.AddPage( self.m_panel1, u"opEdit", True, wx.Bitmap( u"media/opEdit-small.png", wx.BITMAP_TYPE_ANY ) )

        bSizer1.Add( self.tab_main, 1, wx.EXPAND |wx.ALL, 1 )


        self.SetSizer( bSizer1 )
        self.Layout()

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


###########################################################################
## Class frame_opedit
###########################################################################

class frame_opedit ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 797,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        opedit_grid = wx.GridBagSizer( 3, 3 )
        opedit_grid.SetFlexibleDirection( wx.BOTH )
        opedit_grid.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

        self.file_path_picker = wx.FilePickerCtrl( self, wx.ID_ANY, u"./", u"Select a file", u"*.json", wx.DefaultPosition, wx.Size( 400,-1 ), wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
        opedit_grid.Add( self.file_path_picker, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.EXPAND, 0 )

        self.btn_save = wx.Button( self, wx.ID_SAVE, u"Save", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        opedit_grid.Add( self.btn_save, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 0 )

        box_nodes = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nodes" ), wx.VERTICAL )

        grid_nodes = wx.GridBagSizer( 0, 0 )
        grid_nodes.SetFlexibleDirection( wx.BOTH )
        grid_nodes.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.btn_node_add = wx.Button( box_nodes.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        grid_nodes.Add( self.btn_node_add, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 3 )

        self.btn_node_rem = wx.Button( box_nodes.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        grid_nodes.Add( self.btn_node_rem, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 3 )

        list_nodeChoices = [ u"Node1" ]
        self.list_node = wx.ListBox( box_nodes.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_nodeChoices, wx.LB_SINGLE|wx.LB_SORT )
        grid_nodes.Add( self.list_node, wx.GBPosition( 1, 0 ), wx.GBSpan( 8, 2 ), wx.ALL|wx.EXPAND, 3 )


        box_nodes.Add( grid_nodes, 1, wx.EXPAND, 0 )


        opedit_grid.Add( box_nodes, wx.GBPosition( 1, 0 ), wx.GBSpan( 6, 2 ), wx.EXPAND, 0 )

        box_options = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( box_options.GetStaticBox(), wx.ID_ANY, u"OPTIONS!!!!", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        box_options.Add( self.m_staticText1, 0, 0, 5 )


        opedit_grid.Add( box_options, wx.GBPosition( 1, 2 ), wx.GBSpan( 4, 4 ), wx.EXPAND, 0 )

        box_link = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Links" ), wx.VERTICAL )

        grid_link = wx.GridBagSizer( 0, 0 )
        grid_link.SetFlexibleDirection( wx.BOTH )
        grid_link.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.btn_link_add = wx.Button( box_link.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        grid_link.Add( self.btn_link_add, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 3 )

        self.btn_link_rem = wx.Button( box_link.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        grid_link.Add( self.btn_link_rem, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 3 )

        list_linkChoices = [ u"linkA" ]
        self.list_link = wx.ListBox( box_link.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_linkChoices, wx.LB_SINGLE|wx.LB_SORT )
        grid_link.Add( self.list_link, wx.GBPosition( 1, 0 ), wx.GBSpan( 8, 2 ), wx.ALL|wx.EXPAND, 3 )


        box_link.Add( grid_link, 1, wx.EXPAND, 5 )


        opedit_grid.Add( box_link, wx.GBPosition( 5, 2 ), wx.GBSpan( 2, 2 ), wx.EXPAND, 0 )

        box_support = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Support" ), wx.VERTICAL )

        self.m_staticText3 = wx.StaticText( box_support.GetStaticBox(), wx.ID_ANY, u"Supports", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        box_support.Add( self.m_staticText3, 0, wx.ALL, 5 )


        opedit_grid.Add( box_support, wx.GBPosition( 5, 4 ), wx.GBSpan( 2, 2 ), wx.EXPAND, 0 )

        box_var = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Variables" ), wx.HORIZONTAL )

        grid_var = wx.FlexGridSizer( 2, 1, 0, 0 )
        grid_var.SetFlexibleDirection( wx.BOTH )
        grid_var.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_treeCtrl1 = wx.TreeCtrl( box_var.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.TR_DEFAULT_STYLE|wx.TR_EDIT_LABELS|wx.TR_HAS_BUTTONS|wx.TR_HAS_VARIABLE_ROW_HEIGHT )
        grid_var.Add( self.m_treeCtrl1, 0, wx.ALL, 5 )

        self.propertyGridManager_var = pg.PropertyGridManager(box_var.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.propgrid.PGMAN_DEFAULT_STYLE|wx.propgrid.PG_ALPHABETIC_MODE|wx.propgrid.PG_AUTO_SORT|wx.propgrid.PG_BOLD_MODIFIED|wx.PG_COMPACTOR|wx.propgrid.PG_DESCRIPTION|wx.FULL_REPAINT_ON_RESIZE)
        self.propertyGridManager_var.SetExtraStyle( wx.propgrid.PG_EX_AUTO_UNSPECIFIED_VALUES|wx.propgrid.PG_EX_HELP_AS_TOOLTIPS|wx.propgrid.PG_EX_MODE_BUTTONS|wx.propgrid.PG_EX_MULTIPLE_SELECTION )
        grid_var.Add( self.propertyGridManager_var, 0, wx.ALL, 5 )


        box_var.Add( grid_var, 1, wx.EXPAND, 5 )


        opedit_grid.Add( box_var, wx.GBPosition( 1, 6 ), wx.GBSpan( 6, 3 ), wx.EXPAND, 0 )


        self.SetSizer( opedit_grid )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


