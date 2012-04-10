import sublime
import sublime_plugin
import markdown_python
import os
import tempfile


class MarkdownBuild(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        if not view:
            return
        file_name = view.file_name()
        if not file_name:
            return
        contents = view.substr(sublime.Region(0, view.size()))
        md = markdown_python.markdown(contents)
        html = '<html><meta charset="UTF-8">'
        css = os.path.join(sublime.packages_path(), 'MarkdownBuild', 'markdown.css')
        if (os.path.isfile(css)):
            styles = open(css, 'r').read()
            html += '<style>' + styles + '</style>'
        html += "<body>"
        html += md
        html += "</body></html>"
        output = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
        output.write(html.encode('UTF-8'))
        output.close()
        self.window.run_command('open_url', {"url": output.name})
