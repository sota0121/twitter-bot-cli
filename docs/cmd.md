# Command Reference

- `tbc`
  - [ ] `config`: config file is `.tbcconfig.yml`
    - [ ] `get`: Print the value of a given configuration key
    - [ ] `list`: Print a list of configuration keys and values
    - [ ] ~~ `set`: Update configuration with a value for the given key ~~
  - [ ] `bot`
    - [ ] `send`: send tweet
      - [ ] `-c` / `--config`: config file path (default: `.tbcconfig.yml`)
      - [x] `-m`: text content from arg
      - [x] `-m` & `-i`: text and image content from arg
      - `-mf`: This option will be removed in future
      - [ ] `--sel-rand`: randomized selection from tweet table
      - [ ] `--sel-rand` & `--src`: randomized selection from `src` table
      - [ ] `--sel-seq`: select a specific record from tweet table
      - [ ] `--sel-seq` & `--src`: select a specific record from `src` table
    - [ ] `add-src`: add src path
      - [ ] `--type`: src type (e.g. local, gcs, gspread). (default: local)
  - [ ] `analysis`
    - [ ] `fetch`: fetch info from twitter
    - [ ] `server`: run dashboard server on localhost


