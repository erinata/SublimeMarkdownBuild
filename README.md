# Sublime Markdown (version 0.2.0)

This is a Sublime Text plugin for building markdown.

## Installation

Install using Package Control (Recommanded)

1. I guess most Sublime Text 2 users are using Sublime Package Control. If not, pleast install in from here <http://wbond.net/sublime_packages/package_control>
2. Go to Preference > Package Control, and Choose "Install Package"
3. Choose the package named "MarkdownBuild" to install it

Install manually

1. Download the repo
2. Copy everything in the repo to a folder named "MarkdownBuild" under the package folder of SublimeText 2 (create it if it doesn't exist)

## Usage

Originally this plugin is named "SublimeMarkdown" which features automatic bullet points, numbered lists etc. Now the bullet points functionality is extracted to a separated plugin named "SublimeBullet" <https://github.com/erinata/SublimeBullet> 

Press Ctrl+b to build the markdown file to html and view it in the browser. It used Python-markdown to build the html file but you do not need to have Python installed in order to use this plugin. It used the Python inside Sublime Text to get the job done.

I also include a Markdown.tmLanguage file so the markdown files' syntax should be highlighted. It works well with the theme "SunBurst" but it should work for other themes too.

## Operating Systems

I only tested this on Windows, I hope that it works on OSX and Linux.

## License

Copyright (C) 2012 Tom Lam. MIT License.
