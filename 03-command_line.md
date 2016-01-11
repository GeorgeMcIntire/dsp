# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

cd **directory name**: Changes Directory. Can only change to directories that are children of working directory. 

cd ..: Moves working directory up one.

pwd: Stands for "Print Working Directory". Useful because when you're deep in your code, you can forget what directory you're and this simple command can solve that for you.

cat **file 1** > **file 2**: Replaces the content of file 2 with the content of file 1.

cat **file 1** >> **file 2**: Appends the content of file 1 onto the content of file 2.

alias: Quite literal in its meaning, allows you to creat a shortcut or "alias" for a certain command.

cp **file** **directory**: CoPies contents a file to a directory.
  cp * **directory**: CoPies all files into a directory
  cp *.txt: CoPies all text files into a directory
  cp g*: CoPies all files that begin with letter g into a directory.
  
grep **string** **text file**: "Global Regular Expression Print" Searches string in a text file and returns results.
  grep - i: Makes command case insensitive

ls: Simple command that ListS all the contents of your current directory

mkdir **directory**: MaKes a new DIRectory.

mv **file** **directory**: MoVes a file into a directory

rm **file**: ReMoves file from a directory

rmdir **directory**: Deletes or ReMoves DIRectory. Only works when directory is empty.

sort **file**: Literal command in that it SORTs the content of a file.

touch **file**: Creates a new file in your working directory.




---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls lists all the content in your working directory.
ls -a goes beyond ls by listing all the hidden files and directories in your working directory. Files that start with . are hidden. -a is also known as an option.
ls -l list all the contents of the working directory in long format.
ls -lh list all the content in "human readable format."

---


---

What does `xargs` do? Give an example of how to use it.

It's an unix command line that executes standard input lines. grep is an example of a xarg.

---

