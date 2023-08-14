# Code repository for AK-201-426 (Data Science)

This is a collection of all jupyter notebook including the scratch library,
based on (Gruz, 2019).

Some modification to the scratch library:
- Modularizing all the Python files in scratch library into classes
- Remove nested functions
- Use `numpy.randomn.default_rng()` for pseudo-random number generator
- Consistency in matplotlib command to plot a figure. Instead using
  sequence of `plt.`, we prefer to use a pair of `fig`, `ax` and
  update `ax` instance with plot of the data
- Some URLs restructuring their websites in 2023, so the HTML tag selection
  is revised.

Some issues and to do lists:
- [x] ~~In NLP chapter and section of "Word Vector", we didn't achieve a closed
  result to the result in the textbook. Maybe we need to test 
  the `TextEmbedding` layer (or `Embedding` layer)~~.    
  [Solve this by checking training data creation. In 
  `targets.apppend(vocab.one_hot_encode(word))` the correct one
  from the textbook is `targets.append(vocab.one_hot_encode(nearby_word))`]  

- Several section in some chapters are skipped due to the limited time
  delivering the material to the students. 

## Tutorial to set Git in your computer
Ths tutorial is for Windowss' user. I didn't provide for Linux users, because
most of the students used Windows as their operating systems.

### Installing Git application
- First, install Git application for Windows from [git-scm.com](https://git-scm.com/download/win).
  Choose "Standalone Installer" - 64-bit (it is very rare for 32-bit
  laptop now, but choose based on your architecture). Follow the given instruction
  or you can look at [this step-by-step tutorial](https://phoenixnap.com/kb/how-to-install-git-windows) 
  by phonenixap.com

- After you have Git application in you computer, open VSCode and 
  create a new terminal by click in the menu "Terminal > New Terminal".
  In the below window, it will appear a new terminal. Then type 
  ```
  git --version
  ```
  It must return a version of your Git application. If it is not, you should
  re-check your installation steps. 

### SSH connection 
To connect automatically between your GitHub account and your computer
(or your VSCode), you have to set SSH key in your computer.
This tutorial follows from GitHub documentation on 
[Generate new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) and
[Add a new SSH key to GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). We assume that you never
create any SSH key before. If you already have the key, we suggest that you should
make a new one.

- Open Git Bash and type the following configuration. You should
  replace the email address with your GitHub email address
  ```
  ssh-keygen -t ed25519 -C "your_email@example.com"
  ```

- When the Git Bash asking the following question: 
  ```
  > Enter a file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):
  ```
  type with the path inside the parentheses and replace id with any id
  that you can easily identify. For example
  ```
  > Enter a file in which to save the key (/c/Users/LENOVO/.ssh/id_ed25519): /c/Users/LENOVO/.ssh/github_ed25519
  ```

- Enter passphrase when Git Bash asking to enter paraphrase. You should
  remember this paraphrases. If you forget it, you may recreate and set again SSH key
  from the beginning.

- Add your SSH key to the ssh-agent by typing the following two commands
  in Git Bash (replace id with your ID from the previous step, in our
  example our ID is "github")
  ```
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519
  ```

- Copy the SSH public key to the clipboard. Type the following command in 
  Git Bash (replace id with your ID from the previous step, in our   
  example our ID is "github")
  ```
  clip < ~/.ssh/id_ed25519.pub
  ``

- Go to "Setting" in your GitHub account (you can fin the "Setting" menu
  by clicking your profile photo). In the "Access" section of the sidebar,
  click SSH and GPG keys.

- Click New SSH key or Add SSH Key. In the "Title" field, add a 
  descriptive label for the new key. For example, if you're using
  a personal laptop, you might call this key "Personal laptop"

- In the "Key" field, paste your public key (press Ctrl + V, because
  you have already stored the public key in your clipboard). Then click 
  Add SSH key.

- Now you can use command such as "git clone" and "git pull" to 
  copy and retrieve any GitHub repository. 
  
- If you find some error like this:
  ```
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  ```
  type the following command in Git Bash: `ssh-keygen -R github.com`

## References
- (Gruz, 2019) - Data science from scratch, 2nd. Ed.
