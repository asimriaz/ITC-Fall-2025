---

1. Git Home
2. Git Introduction
3. Git Installation
4. Git Configuration
5. Getting Started with Git
6. Working with New Files
7. Staging Files
8. Committing Changes
9. Tagging in Git
10. Using Git Stash
11. Viewing Git History
12. Getting Help in Git
13. Working with Branches
14. Merging Branches
15. Git Workflow
16. Git Best Practices
17. Git Glossary

---

# Chapter 1: Git Home

### Concept Explanation

Git is the most widely used version control system today. It helps track changes in source code, coordinate work among developers, and maintain a history of project evolution. It is distributed, meaning every developer has a complete copy of the repository.

### Commands

```bash
git --version
```

*Shows installed Git version.*

### Lab Exercises

1. Check whether Git is installed on your system.
2. Note the version of Git installed.

### Instructor Notes / Solutions

* Students should be able to run `git --version` successfully.
* If Git is missing, they should be instructed to install it (next chapter).

---

# Chapter 2: Git Introduction

### Concept Explanation

* **Version Control System (VCS):** A tool to manage project history.
* **Centralized vs Distributed VCS:** Git is distributed, unlike SVN.
* **Repository (Repo):** A project directory tracked by Git.
* **Working Directory:** Local copy of files.
* **Staging Area:** Files prepared for the next commit.
* **Commit:** A snapshot of the project state.

### Commands

```bash
git init
git status
```

### Lab Exercises

1. Create a new folder and initialize a Git repository.
2. Run `git status` to see the current state.

### Instructor Notes / Solutions

* Students should see “Initialized empty Git repository”.
* `git status` should show “nothing to commit, working tree clean”.

---

# Chapter 3: Git Installation

### Concept Explanation

* Git can be installed on **Windows, macOS, Linux**.
* Linux: `apt`, `yum`, or package manager.
* Windows: Download from [git-scm.com](https://git-scm.com).

### Commands

```bash
# Ubuntu / Debian
sudo apt update
sudo apt install git -y

# Fedora / RHEL
sudo dnf install git -y

# macOS
brew install git
```

### Lab Exercises

1. Install Git on your system.
2. Verify installation with `git --version`.

### Instructor Notes / Solutions

* Ensure students get a version number (e.g., `git version 2.43.0`).

---

👉 I’ll continue expanding **each chapter (4–17)** in this same format:

* **Concept Explanation**
* **Commands**
* **Lab Exercises**
* **Instructor Notes**

---


Perfect 👍 I’ll start expanding the **lab manual chapters fully**.
Since it will be long, I’ll give you **3–4 chapters at a time** so you can review before I continue.

---

## Chapter 4: Git Configuration

### Concept Explanation

After installing Git, you need to configure your personal information. This information is used in commits to identify the author. The most common configurations are:

* **Username** → Identifies you in commits.
* **Email** → Required, used in commit history.
* **Editor** → Default editor for writing commit messages.
* **Checking configuration** → Ensures values are stored correctly.

There are three levels of configuration:

1. **System** (`--system`): Applies to every user on the system.
2. **Global** (`--global`): Applies to your user account.
3. **Local** (`--local`): Applies only to a specific repository.

### Commands

```bash
# Set your name
git config --global user.name "John Doe"

# Set your email
git config --global user.email "john@example.com"

# Check your configuration
git config --list

# Set default editor (optional)
git config --global core.editor "nano"
```

### Lab Exercises

1. Configure your name and email using Git.
2. Verify that your settings were applied using `git config --list`.
3. Change your editor to `nano` or `vim` and confirm it is updated.

### Instructor Notes / Solutions

* Students should have at least `user.name` and `user.email` set.
* Running `git config --list` should display their configuration.
* Common mistake: forgetting `--global` makes changes only local.

---

## Chapter 5: Getting Started with Git

### Concept Explanation

The first step in using Git is to either **create a new repository** or **clone an existing one**.

* `git init` → Creates a new empty Git repository in the current folder.
* `git clone` → Copies an existing repository (remote or local).

The repository contains a hidden `.git` directory where all Git data is stored.

### Commands

```bash
# Create a new repository
mkdir myproject
cd myproject
git init

# Clone an existing repository
git clone https://github.com/user/repo.git
```

### Lab Exercises

1. Create a new directory `lab-repo` and initialize it with Git.
2. Clone any public GitHub repository (e.g., [https://github.com/git/git](https://github.com/git/git)).
3. Explore the `.git` folder in your repo.

### Instructor Notes / Solutions

* Students should see `.git` directory inside new repo.
* Cloning a repo should pull all history.
* Verify with `git log` after cloning.

---

## Chapter 6: Working with New Files

### Concept Explanation

* Files in Git can be in different states:

  * **Untracked**: Not yet added to Git.
  * **Tracked**: Added and monitored by Git.
  * **Modified**: Changed after last commit.
* You use `git add` to track new files.

### Commands

```bash
# Create a new file
echo "Hello Git" > file1.txt

# Check status
git status

# Add file to staging
git add file1.txt

# Check status again
git status
```

### Lab Exercises

1. Create a new file `notes.txt` in your repo.
2. Run `git status` before adding the file.
3. Add the file to Git tracking.
4. Run `git status` again to see the change.

### Instructor Notes / Solutions

* Before adding: file should show as **untracked** (red).
* After adding: file should appear in **staged area** (green).

---

## Chapter 7: Staging Files

### Concept Explanation

The **staging area** (or index) is where changes are prepared before committing.

* You can stage multiple files.
* You can stage parts of a file using `git add -p`.
* Use `git reset` to unstage.

### Commands

```bash
# Stage multiple files
git add file1.txt file2.txt

# Stage everything
git add .

# Unstage a file
git reset HEAD file1.txt
```

### Lab Exercises

1. Create and edit two files: `a.txt` and `b.txt`.
2. Stage only `a.txt`.
3. Use `git status` to confirm that only `a.txt` is staged.
4. Unstage `a.txt` and confirm with `git status`.

### Instructor Notes / Solutions

* Students should clearly see the difference between **staged** and **unstaged** changes.
* Encourage use of `git status` after every step.

---

## Chapter 8: Committing Changes

### Concept Explanation

A **commit** is a snapshot of your project. Commits are stored permanently in the repository and include:

* Unique commit ID (SHA hash).
* Author name and email (from Git config).
* Timestamp.
* Commit message.
* Parent commit(s).

Commits form the **history** of your project.

### Commands

```bash
# Commit with a message
git commit -m "Initial commit"

# Commit staged changes
git commit -m "Added notes.txt"

# Skip staging (commit directly)
git commit -a -m "Updated files"
```

### Lab Exercises

1. Create and stage a file `readme.md`.
2. Commit with message: `Added readme`.
3. Modify `readme.md`, then use `git commit -a -m "Updated readme"`.
4. Run `git log` to check commit history.

### Instructor Notes / Solutions

* Students should have at least 2 commits.
* `git log` should show commit IDs and messages.
* Common mistake: forgetting `git add` before committing (except with `-a`).

---

## Chapter 9: Tagging in Git

### Concept Explanation

Tags are used to mark **specific commits**—often used for software releases.

* **Lightweight tag**: A simple pointer to a commit.
* **Annotated tag**: Stores metadata (tagger name, date, message).

### Commands

```bash
# Create lightweight tag
git tag v1.0

# Create annotated tag
git tag -a v1.0 -m "Release version 1.0"

# List all tags
git tag

# Show tag details
git show v1.0
```

### Lab Exercises

1. Create 3 commits in your repo.
2. Add a lightweight tag (`v0.1`) on the first commit.
3. Add an annotated tag (`v1.0`) on the latest commit.
4. Use `git show` to display tag details.

### Instructor Notes / Solutions

* `git tag` should display both `v0.1` and `v1.0`.
* Annotated tags should include author + date + message.

---

## Chapter 10: Using Git Stash

### Concept Explanation

`git stash` temporarily saves your changes without committing them.
Useful when:

* You need to switch branches but don’t want to commit unfinished work.
* You want to test something quickly and return later.

### Commands

```bash
# Save changes
git stash

# List stashes
git stash list

# Apply latest stash
git stash apply

# Remove latest stash after applying
git stash pop
```

### Lab Exercises

1. Modify a file but don’t commit it.
2. Run `git stash` and check with `git status`.
3. Run `git stash list` to see stashed changes.
4. Apply and pop the stash.

### Instructor Notes / Solutions

* After stashing: `git status` should show clean working directory.
* After applying: changes should reappear in working directory.

---

## Chapter 11: Viewing Git History

### Concept Explanation

Git keeps a record of every commit, author, and message. History can be viewed in different formats.

### Commands

```bash
# Full commit log
git log

# One-line summary
git log --oneline

# Show last 2 commits
git log -2

# Graph view with branches
git log --oneline --graph --all
```

### Lab Exercises

1. Make at least 3 commits in your repository.
2. Run `git log` to view detailed history.
3. Run `git log --oneline` to see compact history.
4. Use `git log --graph --oneline --all` to visualize branching.

### Instructor Notes / Solutions

* Students should see multiple commits with unique IDs.
* `--oneline` should display shortened commit hashes.
* `--graph` should display ASCII branch tree.

---
## Chapter 12: Getting Help in Git

### Concept Explanation

Git comes with built-in help for all commands. You can use it when you forget syntax or need detailed options.

There are three ways to get help:

1. `git help <command>` → Opens the manual page.
2. `git <command> --help` → Same as above.
3. `git <command> -h` → Shows a quick summary.

### Commands

```bash
git help commit
git commit --help
git commit -h
```

### Lab Exercises

1. Use Git help to learn more about the `git log` command.
2. Compare the output of `git log --help` and `git log -h`.
3. Use `git help` to check options for `git branch`.

### Instructor Notes / Solutions

* `--help` should open the man page (long format).
* `-h` should give a short usage summary.
* Encourage students to always check help before searching online.

---

## Chapter 13: Working with Branches

### Concept Explanation

Branches allow you to work on different versions of a project simultaneously.

* **Main branch**: Default branch (`main` or `master`).
* **Feature branch**: Used to develop new features.
* **Merging branches**: Combine work from one branch into another.

### Commands

```bash
# List branches
git branch

# Create new branch
git branch feature1

# Switch to branch
git checkout feature1

# Create + switch in one command
git checkout -b feature2
```

### Lab Exercises

1. Create a new branch called `dev`.
2. Switch to `dev` and add a new file.
3. Commit the change in the `dev` branch.
4. Switch back to `main` and confirm the new file is not there.

### Instructor Notes / Solutions

* `git branch` should list `main` and `dev`.
* `git log --oneline --graph` will show different commit histories.
* Students should understand isolation of work in branches.

---

## Chapter 14: Merging Branches

### Concept Explanation

Merging brings changes from one branch into another.

* **Fast-forward merge**: If no new commits in main, history moves forward.
* **Three-way merge**: If both branches have new commits, Git merges them.
* **Merge conflicts**: Occur when the same file is modified in both branches.

### Commands

```bash
# Switch to main branch
git checkout main

# Merge dev branch into main
git merge dev
```

### Handling Merge Conflicts

If conflicts occur:

1. Git marks conflict in the file.
2. Edit file to keep correct changes.
3. Stage file again: `git add <file>`.
4. Commit merge: `git commit`.

### Lab Exercises

1. Create a branch `feature` and modify `notes.txt`.
2. Modify the same line in `notes.txt` on `main`.
3. Merge `feature` into `main`.
4. Resolve conflict and commit the merge.

### Instructor Notes / Solutions

* Students should experience at least one merge conflict.
* Teach them how to identify conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
* Verify with `git log --graph` after merge.

---

## Chapter 15: Git Workflow

### Concept Explanation

Git workflows define how teams use Git in projects. Common workflows:

1. **Centralized workflow**: Everyone works on main branch.
2. **Feature branch workflow**: Each feature has its own branch.
3. **Gitflow workflow**: Structured branching with `develop`, `release`, and `hotfix`.
4. **Forking workflow**: Used in open-source, contributors fork repositories.

### Example Workflow (Feature Branch)

1. Clone repository.
2. Create new branch (`feature-login`).
3. Commit changes in feature branch.
4. Merge into `main` after review.

### Commands

```bash
# Clone repo
git clone https://github.com/user/repo.git

# Create feature branch
git checkout -b feature-login

# Work on code, commit changes
git add .
git commit -m "Added login feature"

# Merge back to main
git checkout main
git merge feature-login
```

### Lab Exercises

1. Simulate a **feature branch workflow** by creating `feature-ui`.
2. Make commits in `feature-ui`.
3. Merge it back to `main`.
4. View history with `git log --graph --oneline --all`.

### Instructor Notes / Solutions

* Students should clearly see **branching and merging** in logs.
* Reinforce importance of **commit messages** in workflows.

---

Perfect 👍 let’s finish the manual with the last two chapters.

---
## Chapter 16: Git Best Practices

### Concept Explanation

Git is powerful, but to use it effectively in real projects, teams follow certain best practices.

**Key Practices:**

1. **Write clear commit messages**

   * Use the imperative mood (e.g., “Add feature” instead of “Added feature”).
   * Keep messages short but descriptive.

2. **Commit often, commit small**

   * Each commit should represent one logical change.
   * Easier to debug and revert.

3. **Use branches effectively**

   * Main branch should always be stable.
   * Create feature branches for new work.

4. **Pull before you push**

   * Always `git pull` before `git push` to avoid conflicts.

5. **Review history regularly**

   * Use `git log --oneline --graph` to track changes.

6. **Ignore unnecessary files**

   * Add files like `node_modules/` or `*.log` to `.gitignore`.

### Commands

```bash
# Good commit message
git commit -m "Add user authentication module"

# Create .gitignore
echo "node_modules/" >> .gitignore
git add .gitignore
git commit -m "Add .gitignore file"
```

### Lab Exercises

1. Make three small, separate commits (instead of one big one).
2. Write commit messages that describe changes clearly.
3. Create a `.gitignore` file that ignores temporary files (e.g., `*.tmp`).

### Instructor Notes / Solutions

* Students’ commit messages should be **clear and descriptive**.
* `.gitignore` should successfully prevent ignored files from being staged.

---

## Chapter 17: Git Glossary

### Concept Explanation

A glossary helps students quickly recall important Git terms.

**Key Terms:**

* **Repository (Repo):** A Git project, including `.git` folder and working files.
* **Commit:** A snapshot of project changes.
* **Branch:** A separate line of development.
* **Merge:** Combining changes from one branch into another.
* **Clone:** Copying an existing repository.
* **Fork:** A copy of a repository on another account (GitHub/GitLab).
* **Staging Area (Index):** Area where changes are prepared before commit.
* **HEAD:** The current branch and commit you’re working on.
* **Tag:** A marker for a specific commit, often used for releases.
* **Conflict:** When changes in two branches cannot be merged automatically.
* **Remote:** A version of your repo hosted on another server (e.g., GitHub).
* **Push:** Uploading commits to a remote repository.
* **Pull:** Downloading commits from a remote repository.

### Commands

```bash
# Check current branch
git branch

# Check HEAD reference
cat .git/HEAD
```

### Lab Exercises

1. Match 5 Git terms with their correct commands.
2. Demonstrate `HEAD` by switching branches and checking `.git/HEAD`.
3. Explain in your own words what a commit is.

### Instructor Notes / Solutions

* Students should be able to explain glossary terms in their own words.
* Encourage peer discussion to reinforce learning.

---


