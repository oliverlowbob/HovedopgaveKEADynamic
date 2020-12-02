## Environments & Branches
* `master` - Used for production, it should be the most stable branch. Merges commits from hotfix, develop and release branches.
* `develop` -  Used for staging, default branch, contains latest features and fixes
* `feature-*` - These branches are short lived as they only exist while a specific feature is being developed. Usually does not merge any commits unto it, unless there is another feature derived from it.
* `hotfix-*` - Used to fix pressing issues that are found in production. hotfix branches merge directly to master.
* `bugfix-*` - Used to fix bugs found that either exist in develop but have not made it into production, or that do exist in production but can wait until the next release. These branches merge into develop.
* `refactor-*` - branches for semantic changes

### Feature branches flow
feature branch should be started from `develop` and merged back.

Create feature branch from develop head

```
$ # update your local repository with latest changes
$ git fetch origin

$ # create feature branch from develop head
$ git checkout -b feature-you-will-do origin/develop
```

1. Create a Pull Request when feature implementation done
2. Make sure all the required test passes
3. If automatic PR merging not available, merge `develop` into your branch (remember to delete branch after merge)

### Hotfix/Bugfix branches flow 
A production hotfix is very similar to a full-scale release except that you do your work in a branch taken directly off of master. Hotfixes are useful in cases where you want to patch a bug in a released version, but develop has unreleased code in it already.
`hotfix` branch should be started from `master` and must be merged back to `master` and `develop`

#### Hotfix branch
1. Create `hotfix` branch from `master`
```
$ # update your local repository with latest changes
$ git fetch origin

$ # create hotfix branch
$ git checkout -b hotfix-what-you-fixed origin/master
```

2. When hotfix is done go through merging process via pull request to `master`
3. When pull request closed, make sure to merge the `hotfix` to `develop` as well

#### Bugfix branch
Should fix bugs found that either exist in develop but have not made it into production
`bugfix` branch should be started from `develop` and must be merged back to `develop`

1. Create `bugfix` branch from `develop`
```
$ # update your local repository with latest changes
$ git fetch origin

$ # create bugfix branch
$ git checkout -b bugfix-what-you-fixed origin/develop
```

2. When bugfix is done go through merging process via pull request to `develop`
