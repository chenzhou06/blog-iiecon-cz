Title: Publish Pelican Output Pages to Gitcafe
Date: 2015-05-13
Category: Programming
Tags: development

This site is powered by [Pelican](http://docs.getpelican.com), which is a very
popular static site generator written in [Python](https://www.python.org).

I have spent a lot of time in configuration to automate the procedure of site
generated.

There are a lot of references can be found in the Pelican's document site.
However, their help is limited due to the fact that their instruction
is mainly focused on the area out of China. At least, Github is exposed to a
high probability of being rejected by Chinese Government, so I couldn't host my
site on [Github Pages](https://pages.github.com). I chose an alternative in China --
[GitCafe](https://gitcafe.com).

## Configure Your Repository in GitCafe
Different with Github, your site must be stored in a branch named as
"gitcafe-pages" and the name of the repository must be as same as the account
name.

I just added the output folder to git repository, not whole pelican fold as
the Pelican's documentation did.

## Automation by Make

If you initiate your Pelican files by `pelican-quickstart`, you have a chance
to select a way to automate operations. I chose automation by `Make`, so
a `Makefile` is generated in my site folder.

There are a lot of operation can be automated by `make`. Just type `make help`
in your site fold to see more information. If you host your site at github pages,
no calibration is needed. `make github` is the right command in most cases once
the site has been generated and you have configured git repository in output
folder correctly.

For gitcafe users, we need to modify the `Makefile` to automatically push files
in the output folder to the remote repository. Add these lines to `Makefile`:

```{.Makefile}
gitcafe:
    cd $(OUTPUTDIR) && git add --all && git commit -m "generate site" && git push origin gitcafe-pages
```
`OUTPUTDIR` would have been specified already by the quickstart procedure.
Now, you can publish your site by type `make gitcafe`!!

For more information, you can refer to
[Pelican's documation](http://docs.getpelican.com/en/latest/publish.html).

Thanks.
