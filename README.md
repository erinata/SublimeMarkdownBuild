# MarkdownBuild (version 0.4.0)

This is a Sublime Text plugin for building markdown into html and open it in browser.

## Installation

Install using Package Control (Recommanded)

1. I guess most Sublime Text 2 users are using Sublime Package Control. If not, please install it from here <http://wbond.net/sublime_packages/package_control>
2. Go to Preference > Package Control, and Choose "Install Package"
3. Choose the package named "MarkdownBuild" to install it

Install manually

1. Download the repo
2. Copy everything in the repo to a folder named "MarkdownBuild" under the package folder of SublimeText 2 (create it if it doesn't exist)

## Usage

Originally this plugin is named "SublimeMarkdown" which features automatic bullet points, numbered lists etc. Now the bullet points functionality is extracted to a separated plugin named "SublimeBullet" <https://github.com/erinata/SublimeBullet> 

Press Ctrl+b to build the markdown file to html and view it in the browser. It used Python-markdown to build the html file but you do not need to have Python installed in order to use this plugin. This package utilizes the Python inside Sublime Text to get the job done.

I also include a Markdown.tmLanguage file so the markdown files' syntax should be highlighted. It works well with the theme "SunBurst" but it should work for other themes too.

## Customization

You can customize the behaviour of MarkdownBuild in that MarkdownBuild.sublime-settings file.

- output_html - set it to true if you want to have an html file generated at the same folder of your markdown file (default: false)
- use_css - set it to false if you do not want to use css in the generated file (default: true)
- charset - the charset in the meta tag of html, (default: "UTF-8")

## Building documents other than Markdown

This project only target at building Markdown. But it can be modified to support other formats.

For textile support please see Xkeeper's SublimeTextileBuild <https://github.com/Xkeeper/SublimeTextileBuild>

## Contribution

Please fork this project if you want it to support other document formats. In most case the only part of code that you need to change is the line

    md = markdown_python.markdown(contents)

in the file `MarkdownBuild.py`. Just change it to the parser you likem, this plugin will build the html and show it in the browser accordingly.

Of course you can rename the files, commands, or css ...... etc. Xkeeper's SublimeTextileBuild <https://github.com/Xkeeper/SublimeTextileBuild> is a good example.

## Operating Systems

This package works on Windows, OSX, and Linux

## License

Copyright (C) 2012 Tom Lam. MIT License.
  
