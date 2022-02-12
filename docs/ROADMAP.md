# ROADMAP

## v0.1.0

status: `done`

- Create Bot basic architecture
  - set Data (csv)
  - functions deploy script
  - ... but excluding trigger

## v0.2.0

status: `done`

Make Pip package, and send tweet from cli.

- User Features
  - ~~Enable to exec `pip install`~~
  - Add command twitter-bot-cli called `tbc`
    - ~~ `tbc send` tweets by bot. ~~
- DevOps
  - Create test, deploy workflows


## v0.3.0

status: `wip`

Enable you to setup with cli.

- User Features
  - Easy to operate twitter api secrets
    - `tbc send --config xxxx.yml`
    - create `.tbcconfig` and use this one as a default config file
    - ~~`tbc config --secret $CONFIG_FILE_PATH`~~
    - ~~load config file and set secrets to envval~~
- Patches
  - change `tbc send` --> `tbc bot send`
  - add `tbc config list`, `tbc config get`, `tbc config set -f`


## v0.4.0

status: `todo`

Enable you to select tweet message from local csv file.

- add `tbc bot send --sel-rand`
- add `tbc bot send --sel-rand --src xx.csv`
- add `tbc bot send --sel-seq N`
- add `tbc bot send --sel-seq N --src xx.csv`

- support the csv file below

```bash
# tweet-table.csv
idx,text,  tweeted,imageName
0,  hello, 0,      img/yyy.png
1,  hey,   0,      img/zzz.png
```

## v0.5.0

status: `todo`

Enable you to get image from link.

- Get media to send from link (local, web, gcs, gdrive)
  - `tbc bot send -m "Hello Twitter with Image!!" -i "https://xxx.png"`

- support the csv file below

```bash
# tweet-table.csv
idx,text,  tweeted,imageName
0,  hello, 0,      https://yyy.png
1,  hey,   0,      https://zzz.png
```


## Future

- Analysis Dashboard
  - `tbc analysis server`: run server for dashboard on localhost
  - `tbc analysis fetch`: fetch analysis data from twitter server
