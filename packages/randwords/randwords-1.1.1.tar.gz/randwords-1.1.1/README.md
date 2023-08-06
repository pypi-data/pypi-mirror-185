# randwords
Random word and string generators written in Python

## Installation

`python -m pip install randwords`

## Examples:

`python randwords 6` : Get 6 random words from the included `words` file

`python randwords -f ~/mywords 6` : Get 6 random words from a file at `~/mywords`

`python randwords -l 6` : Get 6 random words an convert them to lowercase

`python randwords -A 6` : Get 6 random words and remove non-ASCII characters

`python randwords -a 6` : Get 6 random words and remove apostrophes

## Development setup

Travis CI CLI needs to be installed to manage .travis.yml

https://github.com/travis-ci/travis.rb#installation

Secrets are stored in .travis.yml via:

```
travis encrypt --add deploy.username <username>
travis encrypt --add deploy.password <password>
```
