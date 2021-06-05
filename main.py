import wx

class MainUI(wx.Frame):
    def __init__(self,parent,title):
        super(MainUI,self).__init__(parent,title=title,size=(1024,768))
        self.Center()
        self.UIinit()

    def UIinit(self):

        self.uiPanel = wx.Panel(self)
        self.uiPanel.SetBackgroundColour('white')
        # 设置字体
        self.uiFont = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        self.uiFont.SetPointSize(9)
        # 先建立一个主框架
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        # 在建立一个主框架内的内部框架
        self.topPan = wx.BoxSizer(wx.HORIZONTAL)

        # 把内部框架放进主框架内
        self.vbox.Add(self.topPan,wx.ID_ANY,wx.EXPAND|wx.ALL,0)
        # again
        self.midPan = wx.BoxSizer(wx.HORIZONTAL)

        self.vbox.Add(self.midPan,wx.ID_ANY,wx.EXPAND|wx.ALL,0)
        # add string label
        self.strlab = wx.StaticText(self.uiPanel,label='Hello world!')
        self.strlab.SetFont(self.uiFont)
        self.midPan.Add(self.strlab,flag=wx.RIGHT, border=8)
        # add input box
        self.inputbox = wx.TextCtrl(self.uiPanel)
        self.midPan.Add(self.inputbox,proportion=0.5)
        # again and again
        self.botPan = wx.BoxSizer(wx.HORIZONTAL)
        # add button
        self.okbtn = wx.Button(self.uiPanel,label='ok',size=(70,30))
        self.cancelbtn = wx.Button(self.uiPanel,label='cancel',size=(70,30))
        self.botPan.Add(self.okbtn,flag=wx.RIGHT|wx.BOTTOM,border=5)
        self.botPan.Add(self.cancelbtn,flag=wx.RIGHT|wx.BOTTOM,border=5)
        self.vbox.Add(self.botPan,wx.ID_ANY,wx.ALIGN_RIGHT|wx.RIGHT,0)
        # add a inputbox
        
        self.uiPanel.SetSizer(self.vbox)

def main():
    app = wx.App()
    ui = MainUI(None,title='BaiduAPI')
    ui.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()