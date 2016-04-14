import sublime, sublime_plugin

class MoveCursorTopCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        screenful = self.view.visible_region()

        col = self.view.rowcol(self.view.sel()[0].begin())[1]
        row = self.view.rowcol(screenful.a)[0]
        target = self.view.text_point(row, col)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(target))

class MoveCursorMiddleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        screenful = self.view.visible_region()

        col = self.view.rowcol(self.view.sel()[0].begin())[1]
        row_a = self.view.rowcol(screenful.a)[0]
        row_b = self.view.rowcol(screenful.b)[0]

        middle_row = (row_a + row_b) / 2
        target = self.view.text_point(middle_row, col)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(target))

class MoveCursorBottomCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        screenful = self.view.visible_region()

        col = self.view.rowcol(self.view.sel()[0].begin())[1]
        row = self.view.rowcol(screenful.b)[0] - 1
        target = self.view.text_point(row, col)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(target))
