# Conventional With Data

A branch of conventionalish with an added `data` prefix.

Patch Commitizen's Conventional Commits implementation with additional prefixes.

```
QUESTIONS = [
    ("fix", "A bug fix", "x", PATCH),
    ("feat", "A new feature", "f", MINOR),
    ("data", "Changes to non-code input (data, blog content, models, etc.)", "a", PATCH),
    ("docs", "Documentation only changes", "d", None),
    ("style", "Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.)", "s", None),
    ("refactor", "A code change that neither fixes a bug nor adds a feature", "r", PATCH),
    ("perf", "A code change that improves performance", "p", PATCH),
    ("test", "Adding missing or correcting existing tests", "t", None),
    ("build", "Changes that affect the build system or external dependencies (example scopes: pip, docker, npm)", "b", None),
    ("ci", "Changes to our CI configuration files and scripts (example scopes: GitLabCI)", "c", None)
]
```

By default, Commitizen will use its Conventional Commits implementation, so when you run `cz commit`, you will get a choice of 

* `fix:`
* `feat:`
* `docs:`
* `style:`
* `refactor:`
* `perf:`
* `test:`
* `build:`
* `ci:`

Commitizen has a robust system for building your own commit patterns, and it's great if you want to start from scratch. But if you want to make a small change to the defaults and keep the nice prompts, commit-message linting, and changelog-building provided by Commitizen, you will have to create or update six patterns or regexps. This script inherits from ConventionalCommitsCz and patches in new choices and associated properties. FWIW, despite the *ish* in the name conventional*ish*, these changes will still meet the Conventional Commits standard (at least as much as Commitizen does) as long as the `feat:` and `fix:` prefixes remain.

Should you want to accomplish this by hand:

1. inherit from ConventionalCommitsCz
2. overload `.questions()`  *# for commit prompts*
3. overload `.schema_pattern()`  *# for commit-message linting*

*Will your addition affect versioning?*

4. overload `.bump_pattern`  *# for commitizen bump*
5. overload `.bump_map`  *# for commitizen bump*
6. overload `.commit_parser`  *# for commitizen changelog*
7. overload `.change_type_map`  *# for commitizen changelog* 
8. overload `.changelog_pattern`  *# for commitizen changelog*

## Usage

To make these changes using a script:

1. clone this project into your project root
2. edit the `QUESTIONS` value at the top of `questions.py`. The default value will give near-identical behavior to the Commitizen default.
3. install conventionalish in your project venv (`poetry add .\conventionalish`; `pip install .\conventionalish`; ...) or upload to PyPi with a new name.
4. run with `cz -n cz_conventionalish` or add the following to `pyproject.toml`

~~~
[tool.commitizen]
name = "cz_conventionalish"
~~~

## Troubleshooting, Q&A

**I updated the file, but Commitizen doesn't recognize the changes.**

This is an installed package, depending how you installed it, you may need to:

1. delete any `commitizenish/build` or `commitizenish/egg-info` directories
2. uninstall
3. reinstall

**How can I change the project name (`conventionalish`)?**

1. change the name of this folder after you clone it
2. update the line `name="conventionalish"` in `conventionalish/pyproject.toml` to `name="new_folder_name"`

**How can I change the commit-rule name (`cz_conventionalish`)?**

1. change the filename `conventionalish/cz_conventionalish.py` to `conventionalish/cz_new_name.py`
2. change the line `{ include = "cz_conventionalish.py" }` in `conventionalish/pyproject.toml` to `{ include = "cz_new_name.py" }`

## Author
Shay Hill (shay_public@hotmail.com)
