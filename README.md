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

Now, open your web browser and go to this magic website: http://localhost:8000 This is a local server which allows the HTML pages to talk to each other and load data. Every time you make a change and want to see it on the built website, refresh the page.

The "`&`" (ampersand) is the symbol for "do this operation in the background," which is helpful for when you edit the website and re-build it multiple times. *You only need to serve once* - you don't need to re-serve after you build. Just refresh the page.

## Editing the website

### Adding people

To add a new person to the people page, copy an existing person's markdown file (in `content/pages/people/*.md`) (it's easiest if you pick someone from the same position, e.g. an existing grad student for a new grad student), and copy their information in.

The top of the `.md` (markdown) file is a bunch of metadata. The critical stuff that is required is:

```markdown
Title: Olga Botvinnik  <!-- Name of the person -->
Date: 2013-06-01  <!-- A date is required to build - use approximate date started in the lab -->
Position: Graduate Student <!-- Position of the person, one of "Principal Investigator", "Post-Doctoral Fellow", "Graduate Student" or "Staff" -->
Affiliation: Bioinformatics and Systems Biology <!-- Department the person is tied to. If unknown, use Gene's department: "Cellular and Molecular Medicine" -->
Email: obotvinn@ucsd.edu  <!-- UCSD-related email to contact the person. gmail and hotmail not okay here -->
Fellowship: NDSEG <!-- Name of the fellowship, if applicable. If none, leave blank. Leave out the word "Fellowship" -->
Headshot: /images/people/botvinnik_olga_headshot.jpeg <!-- Location of the person's square headshot -->
Template: person <!-- don't touch this! if it doesn't say "person" here then they don't get a page :( -->
```
