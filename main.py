import wx

mainapp = wx.App()
windows = wx.Frame(None,title='baidu api interface')
btn1 = wx.Button(windows,label='Test',pos=wx.DefaultPosition,size=wx.DefaultSize)
windows.Show()

mainapp.MainLoop()