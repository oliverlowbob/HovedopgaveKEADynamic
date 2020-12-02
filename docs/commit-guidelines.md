## Commit message guidelines
1. Limit the subject line to 50 characters.
2. Capitalize only the first letter in the subject line.
3. Don't put a period at the end of the subject line.
4. Put a blank line between the subject line and the body.
5. Wrap the body at 72 characters.
6. Use the imperative mood.
7. Describe what was done and why, but not how.

**The 50-character title limit**\
There are two reasons you should limit the git subject line to 50 characters. First of all, when others sift through your sea of commits, a 50-character title allows them to quickly determine the purpose of the commit.

Second, it forces the developer to really think about the work they just performed and to succinctly describe it. If a developer can't describe the purpose of the commit in 50 characters or less, it's a good indication that they aren't committing enough, they put far too much into a single commit or they don't really have a good idea of the problem they tried to solve or the feature they wanted to create. If you develop incrementally and commit often, it shouldn't be a problem to describe a commit in 50 characters or less.

**Controlled capitalization**\
In terms of format, capitalize the first letter of the subject line but don't force unnecessary capitalization anywhere else. Other developers might use case-sensitive tools to search for a given entry in the commit log, and you don't want to complicate the process and have a search fail because you used 'The' instead of 'the' somewhere in the prose.

**Watch your grammar and typesetting**\
Think of your subject line in comparison to newspaper headlines. Neither a git subject line nor a newspaper headline should end with a period.

The optional body of a git commit may contain periods. In fact, if you have a body paragraph in your commit, it should follow all the standard rules of well-formed grammar and typesetting.

In terms of formatting, there should always be an empty line between the subject line and the body. This space allows for various git tools to effectively format commit histories. When asked for a concise git history, many tools will print out just the first line of each commit. When you keep this separate from the body, you'll make the git commit history easier to work with.

**The 72-character limit**\
Another one of the rules on how to write a git commit message properly is to limit the body width to 72 characters. Now, this doesn't mean setting your text editor to word wrap at 72. This git commit message guideline means you have to concertedly add a carriage return when the body of your commit message approaches 72 characters.

**How to write git commit messages imperatively**\
If you want to write a git commit message properly, you should use the imperative mood. This means you need to eliminate the temptation to use gerunds or past tense in your subject lines. Don't write a git commit subject line that talks about what you did, or what you are doing. Instead, describe what was done.

```
Fixed the bug // bad

Fixing the bug // bad

Fix the bug // good
```

The imperative mood is the one git commit message guideline that developers tend to violate most often. A good rule of thumb is that a git commit message can be appended to the statement "If applied, this commit will …." The resulting sentence should make grammatical sense. As you can see from the following three examples, gerunds and past tense commits fail the test, while the imperative tense does not:

```
If applied, this commit will Fixed the bug

If applied, Fixing the bug

If applied, Fix the bug
```

There is a certain degree of ethnocentricity built into this rule. It works well for English speakers, but doesn't necessarily translate to other languages. Furthermore, there are certainly corner cases where a nonsensical commit message might actually work grammatically in this scenario. Generally speaking, it's a good test that can help developers avoid mistakes when they craft their git commit subject lines.

**The git commit body**\
Not every git commit needs a body. Sometimes a descriptive subject line is sufficient, but if you want more detail, you can add a body.

The goal of a commit message is to concisely explain what and why, so that other developers on the team can quickly go through the git log and figure out the purpose of a particular commit. There is no need to go into extra details pertaining to how a given problem was fixed, or what was done to implement a new feature. If those details are needed, a developer can simply do a diff on the code and look at the actual code changes.

However, a commit message footer is the place to add Jira ticket references or other commits that are pertinent to the current commit. These pieces of information are often useful, but they tend to read awkwardly in the subject line. At the same time, don't get lazy and simply quote a Jira ticket instead of providing a good git commit message. If you say, 'Go look at Jira ticket 8154,' this doesn't provide immediate context for someone going through the git log.
