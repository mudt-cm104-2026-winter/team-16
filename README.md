# Team project
Our project name: Car rating app. (Potentially Carate)

## What this is


Car rating app

A simple car ratings app where you add a car and a rating from 1 to 10. 
It also creates a table with the cars and the ratings which are put by the user.


## How to run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The entries are kept in memory: after a restart the list is empty again.

## Team

<!-- One row per person: GitHub username and what you mainly take care of.
No real names: this repository is public. -->

| GitHub | Role |
|S3MXL|Pull Request Review, Branch Merge, README Changes|
|sshieru|Python Programming, Pull Request Review|
|maruskinshere|Changes to README, Changelog, Pull Request Review|
## How we work

<!-- How your team uses Git. For example:
- one branch per issue, named after it: `12-add-glossary`
- every pull request needs one approval from another team member
- the author merges after the approval
- every pull request adds a line to CHANGELOG.md
-->

## Sources

<!-- One entry per source, added on the day you use it:
- 2026-11-05: <title or link>, used for <what>
-->

## Use of AI

AI helped us to change the code in the template to adapt the app to our idea
