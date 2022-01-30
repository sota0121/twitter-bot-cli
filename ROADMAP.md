# ROADMAP

## v1.0.0-beta

- Create Bot basic architecture
  - set Data (csv)
  - functions deploy script
  - ... but excluding trigger

## v1.0.0

- User Features
  - Enable to exec `pip install`
  - Add command twitter-bot-cli called `tbc`
    - `tbc run` executes bot.
- DevOps
  - Create test, deploy workflows


## v2.0.0

- Add sub command of `tbc`
  - Setting auth-keys
    - `tbc set-keys $CONFIG_FILE_PATH`
  - Adding tweet
    - `tbc add -t "Hello Twitter!" --img-link "https://XXXX.YYYY"`
    - `tbc add -f tweets-list.csv`

