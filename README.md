yeolab.github.io-source
=======================

Markdown and HTML source code for static website built via Pelican and Fabric on Travis-CI.


To set up pushes from Travis-CI, I had to encrypt a Github token in my `.travis.yml` file. First, you will need a "personal access token", which you can generate from
github by going to the settings of your account (where you would change your password),
and creating a new token with the name "Yeolab Website" (or whatever you want to call it). It will look like `1234567890qwertyuiopasdfghjklzxcvbnm`. Make sure to copy this to your clipboard because for security reasons, you'll only see it once. Note that you do not want to save this to a public place because anyone with this key can make changes to your repositories, including malicious ones.

Then, run this command, but replace the "Olga Botvinnik" and olga.botvinnik@gmail.com with your own name and email.

```
travis encrypt --add -r gbic-ucsd/gbic-ucsd.github.io-source GIT_NAME="Olga Botvinnik" GIT_EMAIL=olga.botvinnik@gmail.com GH_TOKEN=<secret personal access token from github.com>
```

## How to install, build, and view the website

### Important notes

This website relies on **both**

* The [`people`](https://github.com/olgabot/people) extension, which populates a dictionary of "persons" (i.e. individual people), their position in lab, and their status, and assigns it to the "people"
* The [`twenty-pelican-html5up`](https://github.com/YeoLab/twenty-pelican-html5up/) theme, which specifies how to make both a "person" and "people" page.

Both of these extensions are required for the website to build.

### Install requirements

Install the required python packages on the command line with,

```
pip install -r requirements.txt
```

### Build the website
Now that you have everything installed, build the website with

```
fab build
```

`fab` stands for `fabric` which is the system we use to "weave" together all of the components of the website.

### Viewing the built website

To see what the website would look like online, do

```
fab serve &
```

Which should result in the output,

```
[localhost] local: cd output && python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
```

Now, open your web browser and go to this magic website: http://localhost:8000 This is a local server on your computer only (not a public website) which allows the HTML pages to talk to each other and load data. Every time you make a change and want to see it on the built website, refresh the page.

The "`&`" (ampersand) is the symbol for "do this operation in the background," which is helpful for when you edit the website and re-build it multiple times. *You only need to serve once* - you don't need to re-serve after you build. Just refresh the page.

## Editing the website

### Adding people

To add a new person to the people page, copy an existing person's markdown file (in `content/pages/people/*.md`) (it's easiest if you pick someone from the same position, e.g. an existing grad student for a new grad student), and copy their information in.

The top of the `.md` (markdown) file is a bunch of metadata. The critical stuff that is required is (HTML comments on what the thing is are inline):

```markdown
<!-- Name of the person -->
Title: Olga Botvinnik  

<!-- A date is required to build - use approximate date started in the lab -->
Date: 2013-06-01

<!-- Position of the person, one of "Principal Investigator", "Post-Doctoral Fellow", "Graduate Student" or "Staff" -->
Position: Graduate Student

<!-- A suffix to add after the position. Mostly relevant for Staff Research Associates, so here for them you would put "Research Associate II" or "Bioinformatics Analyst I", whichever position they are-->
Position_suffix:

<!-- Department the person is tied to. If unknown, leave blank -->
Affiliation: Bioinformatics and Systems Biology

<!-- UCSD-related email to contact the person. gmail and hotmail not okay here -->
Email: obotvinn@ucsd.edu

<!-- Name of the fellowship, if applicable. If none, leave blank. Leave out the word "Fellowship" -->
Fellowship: NDSEG

<!-- Location of the person's square headshot, relative to the folder "content/" -->
Headshot: /images/people/botvinnik_olga_headshot.jpeg

<!-- don't touch this! if it doesn't say "person" here then they don't get a page :( -->
Template: person
```


### Debugging

If you get the error, `CRITICAL: UndefinedError: 'page' is undefined`, double check that you have put individual "person" pages **only** in `content/pages/people`. If it's in `content/`  but not the subdirectory `people`, then Pelican will try to use the Article template instead of the Page template, leading to `page` being undefined.
