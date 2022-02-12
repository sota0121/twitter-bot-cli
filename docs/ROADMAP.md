# ROADMAP

## v0.1.0

- Create Bot basic architecture
  - set Data (csv)
  - functions deploy script
  - ... but excluding trigger

## v0.2.0

Make Pip package, and send tweet from cli.

- User Features
  - ~~Enable to exec `pip install`~~
  - Add command twitter-bot-cli called `tbc`
    - ~~ `tbc send` tweets by bot. ~~
- DevOps
  - Create test, deploy workflows


## v0.3.0

Enable you to setup with cli.

- User Features
  - Easy to operate twitter api secrets
    - `tbc config --secret $CONFIG_FILE_PATH`
    - load config file and set secrets to envval


## v0.4.0

Enable you to select tweet message from table in cloud.

- User Features
  - set tweets list file (local, Cloud Storage, Google Spreadsheet)
  - save into `.tbcconfig.yml > src`
    - `src.type`: local, gcs, gspread
    - `src.id`: "./XXX.csv", "gcs://XXXX", "akuokakokjbakd308tq0"
  - ※ mv `.env.yaml` --> `.tbcconfig.yml > environments: []`
  - setting `.tbcconfig.yml` with sub command
    - `tbc config --src-type local --src ./data/tweets-tbl.csv`
      - set source info to config file
    - `tbc config --create`
      - create config file


## v0.5.0

Enable you to get image from link.

- User Features
  - Get media to send from link (local, web, gcs, gdrive)
  - `tbc send -m "Hello Twitter with Image!!" --img-link "https://XXX.jpg"`



## Future

- Enable you to update tweet table with command.
  - `tbc add -m "Hello Twitter!" --src-type web  --img-link "https://XXXX.YYY"`
  - `tbc add -m "Hello Twitter!" --src-type gcs  --img-link "gcs://XXXX.YYY"`
  - `tbc add -m "Hello Twitter!" --src-type local  --img-link "./data/img/XXX.jpg"`


