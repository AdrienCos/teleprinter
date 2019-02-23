# Teleprinter

This is a Telegram bot that upon receiption of a file will immediately print it on the machine's default printer (by using the `lpr` command). 

It uses the `python-telegram-bot` package to interface with the Telegram API.

## Usage

From inside the project repository:
```
    pipenv install
```

Create a file called `token` that contains your [Telegram Bot API token](https://core.telegram.org/bots#6-botfather) and place it in the project repository. 

Run the python script: 
```
    pipenv run python main.py
```

From Telegram, send a file to the bot. You will see the following message in your terminal:
```
    If you want me to print this file, reply to it with the /print command
```

To confirm the printing request, reply to your message with the `/print` command. By default, the print job will print one double-sided copy. You can change that by adding arguments to you command:
* `n copies` will print `n` copies of the file
* `simple sided` or `single sided` will print single sided

You will then receive a answer from the bot saying: 
```
    Printing file file.ext
```

where `file.ext` is the name of file you sent. It will then print the file using the [`lp`](https://linux.die.net/man/1/lp) command.

## Todo

* Remove the document once it has been printed
* Add a way to cancel a printing job
