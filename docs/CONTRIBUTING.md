## Git standards

### Branches

The name structure of the branch is next: [feature|bug|doc|dev]/[number-of-the-issue]-[name-of-the-branch]

Example: ```dev/2-field```

- `feature` prefix is for feature branch
- `bug` prefix is for the branch that will fix the bug
- `doc` prefix is for the branch that will update the documentation
- `dev` prefix is for some general task that is neither feature nor a bug

Example: ```git branch feature/1-Field```
To switch to new branch: ```git checkout feature/1-Field```

### Commits

For commit messages we're using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) standard.

Use the syntax below in the pull request description or any commit message within the PR:

```fix: update constant #ISSUE_NUMBER```

Replace #ISSUE_NUMBER with the actual issue number. GitHub will automatically link the PR to the issue and close it when the PR is merged.


## Code style

### PEP8
PEP8 is the official style guide for Python code, promoting consistency and readability.
[Full document](https://peps.python.org/pep-0008)
