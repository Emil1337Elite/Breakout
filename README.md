# README.md for Breakout

## Description

This project is written in Python and the purpose is to recreate the classic arcade game Breakout.

## Built with

### Languages

Python - the project itself is written in Python.

Markdown - the readme is written with markdown.

### Libraries

pygame - used to display graphics and run the program

## Requirements

- Pygame 3.7+

- pygame module

## Installation

This project is tested in Python 3.7+. To install Python yo can visit (https://www.python.org/downloads/)

The program also requires the pygame library to be installed. Python 3.7+ is required to install pygame, followed by the following command written in the Command Prompt:

```cmd
pip install pygame
```

## Code conventions

- Follows PEP-8 standard

- Variables and functions with multiple words are seperated with underscores to improve readability (snake case).

- Classes are written in camel case.

## Usage

Press run to run the program, a new window will then open and display the game. The platform is controlled by moving the mouse. The game is over when all blocks are gone or the ball hits the bottom of the screen.

## Example

- How the game looks while running

<img width="600" alt="image" src="https://user-images.githubusercontent.com/94603590/168470496-75607dfd-f2fb-4f83-b973-084af1a24d2b.PNG">


## To do

- [x] Add ball sprite
- [x] Add block sprite
- [x] Add platform sprite
- [x] Add collision
- [x] Add movement of ball and platform
- [x] Add controls for platform
- [x] Add win state
- [x] Add Game Over
- [ ] To add if i have time
    - [x] Add score counter
    - [x] Add high score table
    - [ ] Add start screen
    - [ ] Add multi-colored blocks
    - [ ] Add diffrent types of bounce

## Changelog

### Version 1.0.0

#### Changed or added

Added sprites for ball and blocks.

***

### Version 1.0.1

#### Changed or added

Added sprite for player platform.

***

### Version 1.0.2

#### Changed or added

Added platform movement

Changed controls from the arrow keys to mouse control

***
### Version 1.0.3

#### Changed or added

Added collision on the ball, walls and platform

Added ball movement

***

### Version 1.0.4

#### Changed or added

Added a game over screen

Added the graphic for the score counter

***

### Version 1.0.5

#### Changed or added

Added functioning score counter

Added block collision 

Added win state and screen when all blocks are gone

***

### Version 1.0.6

#### Changed or added

Added a highscore function that reads the highscore from a file

***

### Version 1.0.7

#### Changed or added

Fixed a bug where the ball would get stuck bouncing vertically

***

## Contribution

No contributions allowed.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

Emil Ahrnstedt Öster - Discord: CRUST#7392 - emil.osterahrnstedt@gmail.com

## Acknowledgements

[Tutorial for how to add sprites in pygame](https://www.youtube.com/watch?v=hDu8mcAlY4E)