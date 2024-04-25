import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title, size=(500, 350)):
        super().__init__(parent, title=title, size=size)

        self.init_ui()
        self.Centre()
        self.Show()

    def init_ui(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        text = wx.StaticText(panel, label="wxPython Application")
        sizer.Add(text, 0, wx.ALIGN_CENTER)

        button = wx.Button(panel, label="Close")
        button.Bind(wx.EVT_BUTTON, lambda e: self.Close())
        sizer.Add(button, 0, wx.ALIGN_CENTER)

        panel.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    MyFrame(None, title="wxPython Application")
    app.MainLoop()
