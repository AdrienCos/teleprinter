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

From Telegram, send a file to the bot. You will see the following messages in your terminal:
```
    Downloaded file file.txt
    Printing file file.txt
```

where `file.txt` is the name of file you sent. It will then print the file using the [`lpr`](http://man7.org/linux/man-pages/man1/lpr.1.html) command.

## Todo

* Add a confirmation to the printing request, to make sure we do not print by mistake
* Add an option to specify the number of copies desired
* Remove the document once it has been printed
* Add support for image files 