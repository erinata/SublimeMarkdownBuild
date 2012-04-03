# Sublime Markdown (version 0.5.0)

This is a Sublime Text plugin for building markdown.

## Installation

1. Download the package from https://github.com/downloads/erinata/SublimeMarkdown/SublimeMarkdownBuild-0.5.0.zip
2. Extract the folder SublimeMarkdownBuild
3. Copy the SublimeMarkdownBuild folder to the package folder of SublimeText 2

## Usage

Originally this plugin is named "SublimeMarkdown" which features automatic bullet points, numbered lists etc. Now the bullet points functionality is extracted to a separated plugin named "SublimeBullet" <https://github.com/erinata/SublimeBullet> 

Press Ctrl+b to build the markdown file to html and view it in the browser. It used Python-markdown to build the html file but you do not need to have Python installed in order to use this plugin. It used the Python inside Sublime Text to get the job done.

I also include a Markdown.tmLanguage file so the markdown files' syntax should be highlighted. It works well with the theme "SunBurst" but it should work for other themes too.

## Operating Systems

I only tested this on Windows, I hope that it works on OSX and Linux.

## License

Copyright (C) 2012 Tom Lam. MIT License.
