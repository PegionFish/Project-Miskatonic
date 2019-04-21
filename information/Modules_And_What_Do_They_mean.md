# Operation Miskatonic Instruction Document No.2 Modules and What do they mean

# WARNGING
Due to the maintainer of this project uses Chinese as his/her mother language, Chinese version of the instruction files should be consider as what the maintainer wants to express.
The maintainer have done all he/she can do to make Chinese version and English version as similar as possible. So if you have ever found any mistakes, please email to boblao0714@gmail.com or report a issue.  

# 警告
鉴于此项目的创立者和主要维护者使用中文作为母语，在本项目中，中文版本的说明文档将会是最精确表达我想法的文档。
我已经竭尽全力尽量缩小中英文版本之差距，如果你发现任何问题/疏漏请联系我的email或者提交一个issue。

## Modules and what do they mean
In this project, I decided to make all features as indenpent modules. Which means, as the story writer, you should know what all these modules means and when/how to use them.

### How to use a module
You should use this module by following code:

> from module.dice import *  

or

>import module.dice

in these codes, the word "Dice" can be any module that YOU want to use. But certain modules SHOULD not be overused in-game to give player a great gaming experinece. But, this is your choice anyway and I would not be a jerk to ruin your day. Just make sure that you have enough ability to control the whole game. And, it is always be welcomed to write your own module - just make sure that you disturbed your game with all the files that are not in the repo itself.

## 模块和它们的用途

在这个项目中，我决定把它开发成一个模块化的引擎。这意味着，作为一个故事写手，你需要知道何时何地利用这些模块以及它们的功能。

### 如何使用一个模块

你需要用以下的代码导入模块:

> from module.dice import *

或者

>import module.dice

在这些代码里，“dice”可以被替换成任何你想使用的模块。但是为了保证整体游戏体验，有一些的模块不应该在游戏中被过度使用。当然了，模块的使用由你决定，但是你需要确定你有足够的能力去控制剧情的走向。而且，与此同时，只要保证你会把自行编写的模块和游戏一起发布，自行编写需要的模块永远是被欢迎的。

### Dice

The dice.py is a module that controls all your roll results. How many dices being used and how many faces the dice have is all decided by you - which means that you can have a 1d1 dice or a 100d100 dice, all your choice.

### dice

dice.py是一个控制你所有roll点的模块。你可以在游戏中自行决定使用多少骰子以及每个骰子的面数。这意味着，你既可以做一个1d1的骰子，也可以做一个100d100的骰子，一切看你决定。

### story

The story.py is a module that reads story from your file, and do all the things from your file. This module is the HEART of this project, and thus you shouldn't do any modification to it unless you know what you are doing. 

###  story

story.py是一个用于从你写的文件中读取游戏内容并且进行操作的模块。它是这个项目的核心，所以如果你不知道你在做什么，请不要修改这个模块。

### player

The player.py is a module that controls your "Invesgator card". When the game starts, it will automaticlly read the card from the file and save when the game is saved/exited.  
The Invesgator Card is saved at /player.

### player

player.py是一个控制调查员卡的模块。它在游戏开始时读取调查员卡，在游戏结束/保存时将卡的内容保存。  
调查员卡的内容储存在 /player 文件夹里。

# CREATOR
THIS IS A POLARIS CLUB PROJECT  

Join us : boblao0714@gmail.com 