Astolfo Discord BOT!

requeriments:

```py
git+https://github.com/Rapptz/discord.py
dnspython==1.16.0
PyNaCl==1.3.0
async-timeout==3.0.1
youtube-dl==2020.03.24
```

buildpacks:

```bash
heroku buildpacks:add https://github.com/codeinteger6/heroku-buildpack-libopus.git
heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
```