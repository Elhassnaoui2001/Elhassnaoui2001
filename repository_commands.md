# Repository Commands and Actions

## Common Git Commands

### Clone a Repository
```bash
git clone <repository_url>
```
### Create a Branch
```bash
git branch <branch_name>
git checkout <branch_name>
```
### Commit Changes
```bash
git add <file_name>
git commit -m "<commit_message>"
```
### Push Changes
```bash
git push origin <branch_name>
```
### Create and Merge Pull Requests (on GitHub UI)
- Navigate to your repository.
- Select "Pull Requests".
- Click "New Pull Request" and follow on-screen instructions.

### Fetch Changes from Remote
```bash
git fetch
```
### Pull Changes
```bash
git pull origin <branch_name>
```
### View Repository Status
```bash
git status
```
### View Commit Logs
```bash
git log
```

## Notes
1. Keep your repository organized by following a clear branching strategy.
2. Write meaningful commit messages.
3. Regularly fetch and merge changes from remote to stay up-to-date.
4. Use `.gitignore` to exclude files/folders from being added to the repository.