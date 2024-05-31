# Hangman

![Hangman responsive image](images/responsive.png)

I have developed a hangman game in Python that is played in the terminal. In this game, you compete against the computer, and it offers three difficulty levels: easy, medium, and hard. 

The objective is to guess the hidden word one letter at a time. The computer randomly selects a word, and you guess letters one by one. Correct guesses reveal the letter's position(s) in the word, while incorrect guesses add to the hangman diagram. 

You win by successfully guessing all letters in the word before the hangman diagram is fully drawn, and you lose if you fail to guess the word before the hangman diagram is completed. 

Visit the deployed game [here](https://hangman-terminal-game-84634e4afa2f.herokuapp.com/).

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Project Layout diagram](#project-goals)
    2. [Project Goals](#project-goals)
    3. [Implementation](#implentation)
    3. [Color Scheme](#color-scheme)
2. [Features](#features)
    1. [General](#general)
    2. [Welcome Message](#welcome)
    3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Programs Used](#libraries-and-programs-used)
4. [Testing](#testing)
    1. [Code Validation](#code-validation)
    2. [Tools Testing](#tools-testing)
    3. [Manual Testing](#manual-testing)
5. [Finished Product](#finished-product)
6. [Deployment](#deployment)
    1. [GitHub Pages](#github-pages)
7. [Credits](#credits)
    1. [Content](#content)
    3. [Code](#code)
8. [Acknowledgements](#acknowledgements)

***

## User Experience (UX)

### Project Layout diagram

![Project Layout diagram](images/diagram.png)

### Project Goals

- I want to develop a Hangman game that's effortless to play and straightforward to navigate.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - The game provides clear guidance at every step. Initially, it prompts users to view instructions by typing either Y or N (lowercase is acceptable). Such options are consistently available throughout the game. Users can also select difficulty levels, and all previously chosen letters are visible to them.

- I want to ensure that the user can play the game as many times as they wish.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - Upon completion of the game, the user is presented with the choice to replay by typing either Y or N (lowercase is acceptable).

- I want the user to be able to select from different difficulty levels.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - I've included a separate file(words.py) categorizing words into three groups: easy, medium, and hard. At the beginning of the game, users will be prompted to choose from these options by typing either "easy," "medium," or "hard," and the game will select words accordingly from the relevant list.

- I want the user to have access to all pertinent information during gameplay, including their guesses, remaining attempts, and the Hangman image.
    - Was this achieved?
        - Yes
    - How was this achieved?
        - Once the game commences, the Hangman image will be displayed. As the user starts and selects a letter, if it's correct, they'll be notified and the letter will be added to a list of guessed letters. In case of an incorrect choice, the user will be informed, and the letter will be added to the guessed letters section. Additionally, the Hangman's parts will begin to be added.

### Implementation

- At the outset of this project, I started by outlining the basic design depicted in the Project Layout Diagram. This layout served as the blueprint for the final game upon completion. Initially, I sought guidance from various YouTube videos and step-by-step guides to construct the fundamental game without incorporating difficulty levels or comprehensive instructions. After establishing this foundation, I proceeded to expand upon it, gradually refining the game to align with the initial project design.


### Color Scheme

- I have created a class of colours to choose from and I have added to the code where required. I have referenced [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code) to get the relevant codes and I have used this as reference throughout. 

- In the initial sections, Cyan and Blue hues were employed for introductory and instructional messages, as well as for indicating difficulty levels. Green was chosen to convey correctness or positive outcomes, while red was reserved for signaling incorrect guesses or negative feedback.

![ANSI Image](images/colours.png)


## Features

### Game Start

* This screen appears at the beggining of the game, welcoming the user and giving the option to see the instructions.

![Game Start](images/welcome.png)

### Difficulty Screen

* This screen appears at the beggining of the game, welcoming the user and giving the option to see the instructions.

![Game Start](images/welcome.png)


## Technologies Used

### Languages Used

* Python(https://en.wikipedia.org/wiki/Python_(programming_language))


### Libraries and Programs Used


* [GitPod](https://gitpod.io/)
    - GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/)
    - GitHub was used to store the project after pushing.

* [Am I Responsive?](http://ami.responsivedesign.is/#)
    - Am I Responsive was used to for the beggining image at the beggining of this README

* [W3C Markup Validator](https://validator.w3.org/)
    - W3C Markup Validator was used to validate the HTML code.

[Back to top ⇧](#table-of-contents)


## Testing


### Code Validation

* 



    

### Tools Testing

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)


### Manual Testing

* Common Elements Testing

    - General

    Feature | Outcome | Pass/Fail
    --- | --- | ---
    Responsive design | The game can be played on mobile, tablet and Desktop | Pass

    - Game Section

    Feature | Outcome | Pass/Fail
    --- | --- | ---
    Rock Button | Brings up the correct image of a rock for both players. | Pass


[Back to top ⇧](#table-of-contents)

### Validator errors



## Finished Product

### Game Page

![finished product]()



## Deployment

* This website was developed using [GitPod](https://www.gitpod.io/), which was then committed and pushed to GitHub using the GitPod terminal.

Put more on deployment in here

## Credits 

* 

### Content

- 
   

### Code

- 

[Back to top ⇧](#table-of-contents)

## Acknowledgements

- 

[Back to top ⇧](#table-of-contents)
