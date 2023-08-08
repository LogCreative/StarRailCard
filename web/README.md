## StarRailCard-web

A static web page generator for StarRailCard.

> [StarRailCard](https://github.com/DEViantUA/StarRailCard) has an active update on PyPI, but not on GitHub.
> 
> This repo has some fixes on optimizing the experience for Chinese users, whose related issue has been reported on [Issue #1](https://github.com/DEViantUA/StarRailCard/issues/1).
> 
> Still looking forward to see more feature development on the upstream package.

<img width="669" alt="preview" src="https://github.com/LogCreative/StarRailCard/assets/61653082/731cd519-0d3c-4a6d-a63e-f04c91263ade">


## Usage

You should install the package the normal way to install the dependencies.
```
pip install starrailcard
```
will install the current latest, but the web module here will use the modified package in the parent directory directly.


And run the script, pass the uid as the argument:
```bash
python main.py -u 109814396
```
If you want to change the language, for example, to Chinese (Simplified), then use:
```bash
python main.py -u 109814396 -l cn
```
You could get more help by
```bash
python main.py -h
```

After the generation, you could open `railcard.html` directly to preview the result. You could directly deploy those files to your website. Click the avatar to display the detail of different characters.