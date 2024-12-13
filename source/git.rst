
.. image:: images/git-logo.jpg
   :width: 100

Git
###

* find a file::

    git log --all -- <file> which will return commits
    git branch -a --contains <commit>

* default branch::

    git config --global init.defaultBranch main

* cannot push to a remote branch that is currently checked out unless you have::

    git config receive.denyCurrentBranch updateInstead
    otherwise create bare repo with git init --bare  //but can't check out branch it's like github

* remove a file or modify it in an old commit::

    git rebase -i HEAD~3 // make sure you have an extra commit older than you want to modify

    in the interactive screen choose edit on the commit you want to edit
    then remove the file git rm --cached or modify file

    git add it and git commit --amend
    git rebase --continue

    if you have plenty comits use filter-branch or filter-repo

    git filter-branch --force -- index-filter 'git rm --cached --ignore-unmatch path/to/file' --prune-empty --tag-name-filter cat -- --all
    git filter-repo --path path/to/file -- invert-paths
    git push --force --all

* commit hash color::

    git config diff.color.commit <your color>

* git submodules::

    in .gitmodules file

    [submodule "trantor"]
            path = trantor
            url = https://github.com/an-tao/trantor.git
            branch = master

    [submodule "DOMPurify"]
            path = DOMPurify
            url = https://github.com/cure53/DOMpurify.git
            branch = master

    update modules with
    git submodule update
    cd submodule
    git pull
    or
    git submodule foreach git pull origin master
    or git submodule update --remote --merge

    git submodule status
    git submodule add https://github.com/cure53/DOMPurify.git DOMPurify

* tags::

    git tag -a release-v1.0
    git push origin tag release-v1.0

* remove an old commit and git rebase::

    You can try with git rebase -i.

    Following the example you used in your question and assuming A is in the remote repo but B, C, D and E are not, after using git rebase you will get an screen like this:

    pick 67a8df7 B
    pick 47a6947 C
    pick a55540f D
    pick 68b51d5 E

    Then you will need to edit commit E line like this:

    pick 67a8df7 B
    pick 47a6947 C
    pick a55540f D
    edit 68b51d5 E

    Finally, remove the line that you want, commit your changes and use git rebase --continue to go on.

* change remote repo::

    git remote set-url origin https://github.com/trist007/darkterminal.git

* show hidden chars in git diff white space errors::

    git diff --ws-error-highlight=all

* handle new line chars cross platform::

    git config --global core.autocrlf true
