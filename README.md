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
