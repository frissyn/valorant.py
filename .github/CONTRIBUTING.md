# Contributing to **valorant.py**

Thanks for taking the time to contribute to `valorant.py`! It makes the library better. 👍

These guidelines will walk you through the necessary steps to ensure your contribution is up to standards and is easy to test and integrate.

### Submitting an Issue ⚠️ :octocat:

If you want to ask a question about the library, please do so through one of the proper channels, not in the issue tracker.

Keep in mind the following guidelines:

+ Don't open duplicate issues! These will be closed and you'll be referred to the existing one.
+ If submitting a bug report about exceptions or errors, please include the **entire** traceback, otherwise the issue might be unsolvable without further information.
+ Please provide enough information to make the issue workable. This includes:
    + A **summary** of the bug or issue report.
    + How to **reproduce** the error.
    + Explain what you **expected** to happen.
    + Give us your **enviornment** information (Python version, `valorant.py` version, etc.)


### Opening a Pull Request 📝 :octocat:

Opening a Pull Request means you've made or are going to make code/documentation changes to the library.

Please make sure to read these guidelines thorougly; failing to meet some of the rules will mean more work for everyone involved!

**Setting up your enviornment:**

1. [Fork](https://github.com/frissyn/valorant.py/fork) the `valorant.py` respository.
2. Clone your forked repository. `git clone https://github.com/{username}/valorant.py`
3. Create a new feature branch. `git checkout -b new-feature`

    **NOTE:** Please do **not** commit any changes to the `master` or `dev` branch. Create a new branch with a name that fits the changes you are making.

4. Commit your changes. `git commit -a -m 'Add some feature'`
5. Push to origin. `git push origin new-feature`

**Installing local changes:**

If you want to test your local changes to `valorant.py`, run `pip install -e .` from the working directory. This ensures that setuptools and the standard installation process runs smoothly. You may have to uninstall previous versions of `valorant.py`.

**Running tests:**

**Before** opening a new pull request, ensure all library tests pass by running `bash bin/test`, or `python -m tests` if not on a Unix system.

If your changes are not covered by these tests, make you have tested them by hand and that they work as desired.

**Opening the Request:**

When creating a pull request, please request to merge into the `dev` branch, **not** the `master` branch. The `master` branch is for the latest **stable** version, so working changes must not be made to that branch.

![image](https://user-images.githubusercontent.com/62220201/161568817-c55b5211-c7a8-4c19-9544-6b7c9d8e45d7.png)
