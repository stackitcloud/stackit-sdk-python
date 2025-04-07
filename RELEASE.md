# Release

## Release cycle

A release of the whole SDK should be created at least every 2 weeks. 

## Release creation

### Single service

The SDK is split into all the different STACKIT [services](https://github.com/stackitcloud/stackit-sdk-python/tree/main/services), each of them having their own version numbers.

**Checklist before releasing a single service**

- [ ] Changelog entries were added to the `CHANGELOG.md` in the root directory of the repository (see [here](https://github.com/stackitcloud/stackit-sdk-python/blob/608176ab8cdfa60a3cfb09da49de0b1aba5fea84/CHANGELOG.md))
- [ ] Changelog entries were added to the `CHANGELOG.md` file of the service to be released (see e.g. [here](https://github.com/stackitcloud/stackit-sdk-python/blob/608176ab8cdfa60a3cfb09da49de0b1aba5fea84/services/dns/CHANGELOG.md))
- [ ] Version number of the `pyproject.toml` of the service was adjusted (see e.g. [here](https://github.com/stackitcloud/stackit-sdk-python/blob/608176ab8cdfa60a3cfb09da49de0b1aba5fea84/services/dns/pyproject.toml))

**Releasing a single service**

1. As soon as a PR is merged to the main branch, which bumps the version of a service in it's `pyproject.toml` file, a release for this service will be created [automatically](https://github.com/stackitcloud/stackit-sdk-python/actions/workflows/cd.yaml).
    - This means a git tag will be created: `services/<SERVICE-NAME>/vX.X.X`. E.g. for the `sqlserverflex` service version `v1.0.1` the git tag would be named `services/sqlserverflex/v1.0.1`

### Whole SDK

**Checklist before releasing the whole SDK**

- [ ] Date was set/updated in the `CHANGELOG.md` file in the root directory of the repository (see [here](https://github.com/stackitcloud/stackit-sdk-python/blob/608176ab8cdfa60a3cfb09da49de0b1aba5fea84/CHANGELOG.md))

**Releasing the whole SDK**

> [!IMPORTANT]
> Consider informing / syncing with the team before creating a new release.

1. Check out latest main branch on your machine
2. Create git tag: `git tag release-YYYY-MM-DD`
3. Push the git tag: `git push origin --tags`
4. Copy the changelog entries for the new release from the `CHANGELOG.md` file in the root directory of the repository (see [here](https://github.com/stackitcloud/stackit-sdk-python/blob/608176ab8cdfa60a3cfb09da49de0b1aba5fea84/CHANGELOG.md)) to your clipboard.
5. Go to the [releases page](https://github.com/stackitcloud/stackit-sdk-python/releases) on GitHub and create a new release. Select the git tag you just created.
6. Before creating the GitHub release, add the *Highlights* heading at the top of the markdown description and paste the changelog entries from your clipboard (see [previous releases](https://github.com/stackitcloud/stackit-sdk-python/releases/tag/release-2025-03-27) to see what it should look like). Then create and publish the GitHub release.

