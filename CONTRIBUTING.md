# Contributing

- If you find a bug, please report it on the issue page, note that you believe that you can fix it and follow the below guidelines.

- If you want to suggest a feature, create an issue describing that feature, and attempt to implement it obeying the below guidelines.

## Guidelines

### Bugs and Features

- Create a branch with under your name. If it is for a project, make it a sub-branch of that project.

- For each bug/feature, create a sub-branch with the issue number for that bug/feature (issue-nnnn).

- Fix your bug, or add your feature.

- Test it (see the testing section). If necessary, write your own tests.

- Having completed your tests, create a pull request with the branch of your name, then pull request that with its parent branch. The pull request should be linked to in the original issue, and should be added to the project page. 

### Testing

- Ensure all code can be successfully linted with pylint.

- If you are editing app.py's API, then use [Imsomnia](https://www.imsomnia.rest) or similar applications. Also, ensure all functionality in previous versions still works as it should (if you've fixed a bug in this functionality, then it probably does, but test it anyway.)

- Ensure all functionality remains intact or improved.

- Your branch **must** have a similar UX to the main branch to be considered.

### Releases

Releases happen either after 5 high priority issues are fixed, or when a project ends. A release's pull request should be the last one in its project. Between projects, if 5 features are added, a release should be created following the below guidelines. If not, these features are to be considered part of the new project.

1. Ensure all tests are met. There should be a maximum of 10 low priority bugs.

2. Create a separate branch for your release, that is based off main.

3. In app.py, set debug to False in when `app.run()` is called.

4. Delete any unnecessary files/folders, multiline comments (that aren't docstrings), unused variables (that don't impact on the code), etc.

5. Test again.

6. Compress the flask-messenger folder into these formats:

     - .zip

     - .tar.xz
     
     - .7z

7. Place these compressed formats into the release folder.

8. Create a pull request, with a list of changes (a shortened summary of all commits since the last release.)

9. Let @Adoria298 create a release.
